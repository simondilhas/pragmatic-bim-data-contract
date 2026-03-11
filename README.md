# pragmatic-bim-schema

An open-source project for defining and using a pragmatic BIM schema.

## Why

After creating many data models, the same design questions keep coming up.
This project exists to capture those recurring decisions in one practical schema
that can be reused and evolved instead of reinvented each time.

## Project Structure

- `schema/pragmatic_bim_schema.yaml`: Main schema definition.
- `schema/enum_localizations.yaml`: Enum label/localization metadata.
- `converter/`: Converter module for transforming data to and from the schema.

## Goals

- Keep schema definitions clear and easy to evolve.
- Enable conversion workflows around a single source of truth schema.
- Stay simple and practical for real-world usage.

## Getting Started

1. Clone the repository.
2. Explore the schema files in `schema/`.
3. Use or implement converter logic in `converter/` as needed by your workflow.

## Contributing

Contributions are welcome.

- Open an issue for bugs or feature proposals.
- Keep pull requests focused and small where possible.
- Add or update documentation when behavior changes.

## License

This project is licensed under the MIT License. See `LICENSE` for details.
