# LLM Odoo Module Wiki

This repository implements Andrej Karpathy's "LLM Wiki" pattern to create a persistent, LLM-maintained, and compounding knowledge base specifically for Odoo 19 modules.

## Concept: The LLM Wiki Pattern

The core idea, as described by Andrej Karpathy, is to move beyond simple Retrieval-Augmented Generation (RAG) from raw documents. Instead, an LLM incrementally builds and maintains a structured, interlinked collection of markdown files (the "wiki") that sits between the user and the raw source code. The LLM reads new information, extracts key insights, and integrates them into the existing wiki, updating relevant pages, flagging contradictions, and continually refining the synthesis of knowledge. This creates a persistent artifact that grows richer over time, reducing the need for an LLM to "rediscover" knowledge repeatedly.

## Purpose of this Repository

This `wiki_module_odoo` repository serves as the knowledge base for the Odoo 19 ERP monorepo. Its primary goals are:

1.  **Structured Documentation:** Provide clear, consistent, and easily navigable documentation for each Odoo module, detailing its purpose, features, dependencies, and key technical components.
2.  **LLM-Maintainable:** The documentation is designed to be generated and maintained by an AI agent (like myself) following a predefined `schema.md` and `ingest` workflow.
3.  **Enhanced Understanding:** Facilitate a deeper understanding of the complex Odoo ecosystem for human developers, allowing them to quickly grasp module functionalities and interconnections.
4.  **Agent Collaboration:** Enable other AI agents to query and contribute to this structured knowledge base, improving their ability to perform tasks within the Odoo codebase.
5.  **Version Control:** Leverage Git for version history, collaboration, and easy sharing of the wiki content.

## Repository Structure

- `README.md`: This file, explaining the project concept and purpose.
- `schema.md`: Defines the structure and rules for documenting individual Odoo modules.
- `index.md`: A central catalog of all documented modules with links to their respective pages.
- `log.md`: An append-only chronological record of all operations performed on the wiki.
- `<module_name>/index.md`: Individual markdown files, each detailing a specific Odoo module.
- `scripts/`: Index builder + retrieval used by the `wiki-query` skill.
- `.claude/skills/wiki-query/`: Claude Code skill for querying this wiki (shipped with the repo).
- `.index/`: Generated retrieval index (`chunks.json` + `meta.json`).

This setup aims to transform raw Odoo module code into an intelligent, evolving documentation system.

## Querying the wiki (for colleagues)

This repo is self-contained for **querying** — you do **not** need the Odoo source code.

1. Clone this repo and open it in Claude Code (this folder is the project root).
2. Ask questions in natural language — the `wiki-query` skill triggers automatically
   (e.g. *"ce modul face export către SAGA?"*, *"care module extind `account.move`?"*).

Under the hood it runs a deterministic retrieval over an index built from the markdown pages:

```bash
python3 scripts/wiki_index.py            # (re)build the index — needs only the .md pages
python3 scripts/wiki_search.py "export SAGA" -k 5    # rank relevant modules
```

Retrieval is **hybrid**: lexical by default (zero network), and semantic via embeddings if
enabled in `scripts/wiki_index.py` (then run `wiki_index.py --embed`). The embedding model and
dimension are recorded in `.index/meta.json` so the query side always matches the ingest side.

## Maintaining the wiki (ingestion)

Generating/updating pages reads the actual module source, so **ingestion runs from the Odoo
monorepo**, not from this standalone repo — use the `wiki-module` skill there. It writes the
`<module>/index.md` pages here and rebuilds `.index/`. Commit and push this repo afterwards so
colleagues get the refreshed knowledge base.