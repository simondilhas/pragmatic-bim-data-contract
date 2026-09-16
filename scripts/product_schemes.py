"""Notation prefix to SKOS scheme IRI base for the abstract product vocabularies.

Shared by the classification generators and by the (unpublished) cost tooling under
`temp/cost/scripts/`, so both resolve a product notation to the same concept IRI.
"""

from __future__ import annotations

SCHEME_IRI_PREFIXES = {
    "SWP-": "https://example.org/abstract/wall-separator-product/",
    "SSP-": "https://example.org/abstract/slab-separator-product/",
    "DCP-": "https://example.org/abstract/door-connector-product/",
    "WICP-": "https://example.org/abstract/window-connector-product/",
    "FCP-": "https://example.org/abstract/floor-covering-product/",
    "WCP-": "https://example.org/abstract/wall-covering-product/",
    "CCP-": "https://example.org/abstract/ceiling-covering-product/",
    "FaCP-": "https://example.org/abstract/facade-covering-product/",
    "RCP-": "https://example.org/abstract/roof-covering-product/",
    "FDP-": "https://example.org/abstract/foundation-product/",
    "CLP-": "https://example.org/abstract/column-product/",
    "BMP-": "https://example.org/abstract/beam-product/",
    "SRP-": "https://example.org/abstract/stair-product/",
    "RAP-": "https://example.org/abstract/railing-product/",
}


def notation_to_iri(notation: str) -> str:
    for prefix, base in SCHEME_IRI_PREFIXES.items():
        if notation.startswith(prefix):
            return f"{base}{notation}"
    return notation
