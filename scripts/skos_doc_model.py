#!/usr/bin/env python3
"""Parse SKOS vocabularies and mapping TTL files into documentation data models."""

from __future__ import annotations

import html
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any
from urllib.parse import unquote, urlparse

from rdflib import Graph, Literal, Namespace, URIRef
from rdflib.namespace import DCTERMS, RDF, SKOS

SKOS_CORE = Namespace("http://www.w3.org/2004/02/skos/core#")
DCTERMS_DATASET = URIRef("http://purl.org/dc/terms/Dataset")

SCHEME_META_PREDICATES = (
    DCTERMS.title,
    DCTERMS.identifier,
    DCTERMS.issued,
    DCTERMS.creator,
    DCTERMS.description,
    DCTERMS.license,
    DCTERMS.source,
    SKOS.prefLabel,
    SKOS.definition,
)

CONCEPT_LITERAL_PREDICATES = (
    SKOS.prefLabel,
    SKOS.definition,
    SKOS.scopeNote,
    SKOS.altLabel,
    DCTERMS.description,
)

IGNORE_MAPPING_PREDICATES = {
    RDF.type,
    DCTERMS.title,
    DCTERMS.description,
    DCTERMS.references,
    DCTERMS.issued,
    DCTERMS.identifier,
    DCTERMS.creator,
    DCTERMS.license,
    DCTERMS.source,
    SKOS.prefLabel,
    SKOS.definition,
    SKOS.inScheme,
    SKOS.topConceptOf,
    SKOS.hasTopConcept,
    SKOS.broader,
    SKOS.narrower,
    SKOS.notation,
    SKOS.altLabel,
    SKOS.scopeNote,
    DCTERMS.subject,
}


@dataclass
class LangStrings:
    values: dict[str, str] = field(default_factory=dict)

    def langs(self) -> list[str]:
        return sorted(self.values)

    def get(self, lang: str) -> str:
        return self.values.get(lang, "")


@dataclass
class ConceptDoc:
    iri: str
    local_name: str
    notation: str
    pref_label: LangStrings = field(default_factory=LangStrings)
    definition: LangStrings = field(default_factory=LangStrings)
    scope_note: LangStrings = field(default_factory=LangStrings)
    broader: list[str] = field(default_factory=list)
    narrower: list[str] = field(default_factory=list)
    is_top_concept: bool = False


@dataclass
class VocabularyDoc:
    slug: str
    title: str
    source_path: Path
    scheme_iri: str
    meta: dict[str, LangStrings] = field(default_factory=dict)
    concepts: list[ConceptDoc] = field(default_factory=list)
    langs: list[str] = field(default_factory=list)

    def concept_by_notation(self) -> dict[str, ConceptDoc]:
        return {c.notation: c for c in self.concepts}


@dataclass
class MappingLink:
    source_prefix: str
    source_notation: str
    predicate: str
    target_prefix: str
    target_notations: list[str]


@dataclass
class MappingDoc:
    slug: str
    title: str
    source_path: Path
    dataset_iri: str
    meta: dict[str, LangStrings] = field(default_factory=dict)
    links: list[MappingLink] = field(default_factory=list)


def load_graph(path: Path) -> Graph:
    graph = Graph()
    graph.parse(path, format="turtle")
    return graph


def local_name(term: URIRef) -> str:
    text = str(term)
    if text.startswith("_:"):
        return text[2:]
    parsed = urlparse(text)
    fragment = unquote(parsed.fragment)
    if fragment:
        return fragment
    path = parsed.path.rstrip("/")
    if path:
        return unquote(path.rsplit("/", 1)[-1])
    return text


def prefix_for_term(term: URIRef, graph: Graph) -> str:
    try:
        namespace = graph.namespace_manager.compute_qname(str(term))[0]
        if namespace != "":
            return namespace
    except Exception:
        pass
    iri = str(term)
    if "#" in iri:
        return iri.rsplit("#", 1)[0].rsplit("/", 1)[-1]
    return urlparse(iri).netloc.split(".")[0] or "concept"


def notation_for_concept(graph: Graph, concept: URIRef) -> str:
    for _, _, notation in graph.triples((concept, SKOS.notation, None)):
        if isinstance(notation, Literal):
            return str(notation)
    return local_name(concept).replace("_", "-")


def collect_lang_strings(graph: Graph, subject: URIRef, predicate: URIRef) -> LangStrings:
    result = LangStrings()
    for _, _, obj in graph.triples((subject, predicate, None)):
        if isinstance(obj, Literal):
            lang = obj.language or "und"
            result.values[lang] = str(obj)
    return result


def collect_scheme_meta(graph: Graph, scheme: URIRef) -> dict[str, LangStrings]:
    meta: dict[str, LangStrings] = {}
    for predicate in SCHEME_META_PREDICATES:
        strings = collect_lang_strings(graph, scheme, predicate)
        if strings.values:
            meta[predicate.split("/")[-1].split("#")[-1]] = strings
    for _, pred, obj in graph.triples((scheme, None, None)):
        if pred in SCHEME_META_PREDICATES:
            continue
        if isinstance(obj, URIRef) and pred in (DCTERMS.license, DCTERMS.source):
            key = local_name(pred) if isinstance(pred, URIRef) else str(pred).split("/")[-1]
            entry = meta.setdefault(key, LangStrings())
            entry.values["und"] = str(obj)
    return meta


def all_langs_from_meta(meta: dict[str, LangStrings]) -> list[str]:
    langs: set[str] = set()
    for strings in meta.values():
        langs.update(strings.langs())
    langs.discard("und")
    return sorted(langs)


def all_langs_from_concepts(concepts: list[ConceptDoc]) -> list[str]:
    langs: set[str] = set()
    for concept in concepts:
        for strings in (concept.pref_label, concept.definition, concept.scope_note):
            langs.update(strings.langs())
    langs.discard("und")
    return sorted(langs)


def parse_vocabulary(path: Path, *, slug: str, title: str) -> VocabularyDoc:
    graph = load_graph(path)
    scheme_nodes = list(graph.subjects(RDF.type, SKOS.ConceptScheme))
    if not scheme_nodes:
        raise ValueError(f"No skos:ConceptScheme found in {path}")
    scheme = scheme_nodes[0]
    if not isinstance(scheme, URIRef):
        raise ValueError(f"Unexpected scheme node in {path}")

    meta = collect_scheme_meta(graph, scheme)
    concepts: list[ConceptDoc] = []

    top_concepts = {
        notation_for_concept(graph, tc)
        for tc in graph.objects(scheme, SKOS.hasTopConcept)
        if isinstance(tc, URIRef)
    }
    top_concepts.update(
        notation_for_concept(graph, tc)
        for tc in graph.subjects(SKOS.topConceptOf, scheme)
        if isinstance(tc, URIRef)
    )

    for concept in graph.subjects(RDF.type, SKOS.Concept):
        if not isinstance(concept, URIRef):
            continue
        notation = notation_for_concept(graph, concept)
        broader = [
            notation_for_concept(graph, b)
            for b in graph.objects(concept, SKOS.broader)
            if isinstance(b, URIRef)
        ]
        narrower = [
            notation_for_concept(graph, n)
            for n in graph.objects(concept, SKOS.narrower)
            if isinstance(n, URIRef)
        ]
        concepts.append(
            ConceptDoc(
                iri=str(concept),
                local_name=local_name(concept),
                notation=notation,
                pref_label=collect_lang_strings(graph, concept, SKOS.prefLabel),
                definition=collect_lang_strings(graph, concept, SKOS.definition),
                scope_note=collect_lang_strings(graph, concept, SKOS.scopeNote),
                broader=broader,
                narrower=narrower,
                is_top_concept=notation in top_concepts,
            )
        )

    concepts.sort(key=lambda c: c.notation)
    langs = sorted(set(all_langs_from_meta(meta)) | set(all_langs_from_concepts(concepts)))

    return VocabularyDoc(
        slug=slug,
        title=title,
        source_path=path,
        scheme_iri=str(scheme),
        meta=meta,
        concepts=concepts,
        langs=langs,
    )


def predicate_label(predicate: URIRef) -> str:
    name = local_name(predicate)
    if name:
        return name
    return str(predicate).rsplit("/", 1)[-1]


def parse_mapping(path: Path, *, slug: str, title: str) -> MappingDoc:
    graph = load_graph(path)
    dataset_nodes = list(graph.subjects(RDF.type, DCTERMS_DATASET))
    if not dataset_nodes:
        raise ValueError(f"No dcterms:Dataset found in {path}")
    dataset = dataset_nodes[0]
    if not isinstance(dataset, URIRef):
        raise ValueError(f"Unexpected dataset node in {path}")

    meta = collect_scheme_meta(graph, dataset)
    links: list[MappingLink] = []

    for subj, pred, obj in graph:
        if pred in IGNORE_MAPPING_PREDICATES:
            continue
        if not isinstance(subj, URIRef):
            continue
        if subj == dataset:
            continue
        if isinstance(obj, Literal):
            continue

        targets: list[URIRef] = []
        if isinstance(obj, URIRef):
            targets = [obj]
        elif hasattr(obj, "__iter__"):
            continue

        if not targets:
            continue

        source_prefix = prefix_for_term(subj, graph)
        source_notation = notation_for_concept(graph, subj)

        target_notations = [notation_for_concept(graph, target) for target in targets]

        links.append(
            MappingLink(
                source_prefix=source_prefix,
                source_notation=source_notation,
                predicate=predicate_label(pred),
                target_prefix=prefix_for_term(targets[0], graph),
                target_notations=target_notations,
            )
        )

    links.sort(key=lambda link: (link.source_notation, link.predicate, ",".join(link.target_notations)))
    return MappingDoc(
        slug=slug,
        title=title,
        source_path=path,
        dataset_iri=str(dataset),
        meta=meta,
        links=links,
    )


def has_hierarchy(vocab: VocabularyDoc) -> bool:
    return any(c.broader or c.narrower for c in vocab.concepts)


def build_mermaid_hierarchy(vocab: VocabularyDoc) -> str:
    """Build a Mermaid class diagram from broader/narrower relations."""
    by_notation = vocab.concept_by_notation()
    edges: set[tuple[str, str]] = set()
    for concept in vocab.concepts:
        for child_notation in concept.narrower:
            if child_notation in by_notation:
                edges.add((concept.notation, child_notation))
        for parent_notation in concept.broader:
            if parent_notation in by_notation:
                edges.add((parent_notation, concept.notation))

    if not edges:
        return ""

    def node_id(code: str) -> str:
        return "n_" + "".join(ch if ch.isalnum() else "_" for ch in code)

    def node_label(notation: str) -> str:
        concept = by_notation.get(notation)
        label = concept.pref_label.get("en") or concept.notation if concept else notation
        return f"{notation}: {label}".replace('"', "'")

    children = {child for _, child in edges}
    parents = {parent for parent, _ in edges}
    roots = sorted(parents - children)

    adjacency: dict[str, list[str]] = {}
    for parent, child in edges:
        adjacency.setdefault(parent, []).append(child)

    def collect_edges_from_root(root: str) -> set[tuple[str, str]]:
        result: set[tuple[str, str]] = set()
        stack = [root]
        visited: set[str] = set()
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            for child in adjacency.get(node, []):
                result.add((node, child))
                stack.append(child)
        return result

    all_notations: set[str] = set()
    for root in roots:
        for parent, child in collect_edges_from_root(root):
            all_notations.add(parent)
            all_notations.add(child)

    lines = ["```mermaid", "classDiagram", "direction TB"]
    for notation in sorted(all_notations):
        lines.append(f'class {node_id(notation)}["{node_label(notation)}"]')
    for root in roots:
        root_edges = collect_edges_from_root(root)
        for parent, child in sorted(root_edges):
            lines.append(f"{node_id(parent)} <|-- {node_id(child)}")
    lines.append("```")
    return "\n".join(lines)


def escape_html(text: str) -> str:
    return html.escape(text, quote=True)


def default_lang(langs: list[str]) -> str:
    if "en" in langs:
        return "en"
    return langs[0] if langs else "en"


LANG_FIELDS = (
    ("label", "Label", lambda c: c.pref_label),
    ("definition", "Definition", lambda c: c.definition),
    ("scope_note", "Scope note", lambda c: c.scope_note),
)


def render_concepts_table_html(vocab: VocabularyDoc) -> str:
    if not vocab.langs:
        return ""

    default = default_lang(vocab.langs)
    lines: list[str] = [
        f'<div class="pbs-vocab-concepts" data-default-lang="{escape_html(default)}" '
        f'data-active-lang="{escape_html(default)}">',
        '<div class="pbs-lang-switcher" role="group" aria-label="Language">',
    ]
    for lang in vocab.langs:
        lines.append(
            f'<button type="button" class="pbs-lang-btn" data-lang="{escape_html(lang)}">'
            f"{escape_html(lang.upper())}</button>"
        )
    lines.extend(["</div>", "<table>", "<thead>", "<tr>"])
    lines.append("<th>Notation</th>")
    lines.append("<th>Broader</th>")
    for lang in vocab.langs:
        for field_key, field_title, _ in LANG_FIELDS:
            lines.append(
                f'<th class="pbs-lang-col" data-lang="{escape_html(lang)}" '
                f'data-field="{field_key}">{field_title}</th>'
            )
    lines.extend(["</tr>", "</thead>", "<tbody>"])

    for concept in vocab.concepts:
        broader = ", ".join(concept.broader)
        lines.append("<tr>")
        lines.append(f"<td>{escape_html(concept.notation)}</td>")
        lines.append(f"<td>{escape_html(broader)}</td>")
        for lang in vocab.langs:
            for field_key, _, getter in LANG_FIELDS:
                value = getter(concept).get(lang)
                lines.append(
                    f'<td class="pbs-lang-col" data-lang="{escape_html(lang)}" '
                    f'data-field="{field_key}">{escape_html(value)}</td>'
                )
        lines.append("</tr>")

    lines.extend(["</tbody>", "</table>", "</div>"])
    return "\n".join(lines)


def format_meta_section(meta: dict[str, LangStrings], langs: list[str]) -> list[str]:
    lines: list[str] = []
    for key in sorted(meta):
        strings = meta[key]
        if key in ("license", "source") and "und" in strings.values:
            lines.append(f"- **{key}:** {strings.values['und']}")
            continue
        for lang in langs:
            value = strings.get(lang)
            if value:
                lines.append(f"- **{key} ({lang}):** {value}")
        if not langs:
            for lang, value in sorted(strings.values.items()):
                lines.append(f"- **{key} ({lang}):** {value}")
    return lines


def render_vocabulary_markdown(vocab: VocabularyDoc) -> str:
    lines: list[str] = [
        f"# {vocab.title}",
        "",
        f"Source: [`{vocab.source_path.name}`](sources/{vocab.slug}.ttl)",
        "",
        "## Scheme",
        "",
    ]
    lines.extend(format_meta_section(vocab.meta, vocab.langs))
    lines.append("")

    if has_hierarchy(vocab):
        mermaid = build_mermaid_hierarchy(vocab)
        if mermaid:
            lines.extend(["## Hierarchy", "", mermaid, ""])

    lines.extend(["## Concepts", "", render_concepts_table_html(vocab), ""])
    return "\n".join(lines)


def render_mapping_markdown(mapping: MappingDoc) -> str:
    lines: list[str] = [
        f"# {mapping.title}",
        "",
        f"Source: [`{mapping.source_path.name}`](sources/mapping-{mapping.slug}.ttl)",
        "",
        "External target labels are not shipped in this repository; only codes and IRIs are shown.",
        "",
        "## Dataset",
        "",
    ]
    langs = all_langs_from_meta(mapping.meta)
    lines.extend(format_meta_section(mapping.meta, langs))
    lines.extend(["", "## Links", "", "| Source | Relation | Targets |", "| --- | --- | --- |"])

    for link in mapping.links:
        source = f"`{link.source_prefix}:{link.source_notation}`"
        targets = ", ".join(f"`{link.target_prefix}:{t}`" for t in link.target_notations)
        lines.append(f"| {source} | `{link.predicate}` | {targets} |")

    lines.append("")
    return "\n".join(lines)


def load_catalog(catalog_path: Path) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    import yaml

    data = yaml.safe_load(catalog_path.read_text(encoding="utf-8")) or {}
    vocabs = data.get("vocabularies", [])
    mappings = data.get("mappings", [])
    if not isinstance(vocabs, list) or not isinstance(mappings, list):
        raise ValueError(f"Invalid catalog format: {catalog_path}")
    return vocabs, mappings
