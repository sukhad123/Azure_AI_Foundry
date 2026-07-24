# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Structure

Learning repository for Azure AI Foundry. Two main learning areas:

```
01_sdk_selection_and_api/
  ├── lesson.md          # SDK selection, token sizing, cost optimization
  ├── azure-index.md     # Azure AI Search & embeddings comprehensive guide
  ├── embeeding.md       # Quick reference (detailed content in azure-index.md)
  └── call_api.py        # Example: Azure OpenAI API call with authentication

02_rag_hybrid_search/
  ├── lesson.md          # RAG on PDFs with hybrid search (BM25 + vector)
  └── code.py            # [To be implemented] RAG example code
```

## Running Python Examples

```bash
# Set up environment
python -m venv venv
venv\Scripts\activate

# Install Azure SDK dependencies
pip install openai azure-identity
```

**azure_openai_call/call_api.py:**
```bash
python azure_openai_call/call_api.py
```
Requires Azure credentials and valid endpoint/deployment names (update placeholders before running).

## Key Architecture Notes

**azure_openai_call/** covers SDK decision-making:
- Lesson documents trade-offs between Foundry SDK, OpenAI SDK, and Anthropic SDK
- Includes token sizing reference (1 token ≈ 4 characters ≈ 0.75 words)
- Example code uses `DefaultAzureCredential()` for auth

**RAG_PDF/** covers retrieval patterns:
- Lesson covers hybrid search concepts (BM25 + vector embeddings)
- Documents Azure AI Search components: Index, Indexer, Data Source, Skillset
- Semantic search setup notes (enable identity, deploy models, assign roles)
