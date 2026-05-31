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
- `[module_name].md`: Individual markdown files, each detailing a specific Odoo module.

This setup aims to transform raw Odoo module code into an intelligent, evolving documentation system.