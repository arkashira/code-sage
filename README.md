# CodeSage Engine
A lightweight, pure‑Python engine that parses a Go monorepo, counts lines per file, and builds an index.
Designed to ingest a 1 M LOC repository in under 30 seconds on an 8‑core VM, keep memory usage below 2 GB, and allow re‑triggering without restarting.

## Features
- **Fast ingestion**: walks the repo tree, counts lines in `.go` files.
- **Re‑triggerable**: each `ingest()` call clears previous state.
- **Low memory footprint**: only stores a simple dictionary of file paths to line counts.
- **Pure standard library**: no external dependencies at runtime.
