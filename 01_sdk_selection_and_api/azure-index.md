## Azure AI Search & Embeddings Guide

### Core Concepts

#### Index
- Defines searchable fields with properties: key, searchable, filterable, sortable, facetable, retrievable
- Acts as the data store for queries

#### Indexer
- Extracts data from data sources (e.g., Azure Storage)
- Processes documents through skillsets
- Configurable parsing mode: JSON for structured data

#### Data Source
- Connection to data (Azure Storage, databases, etc.)
- Specifies what data to ingest

#### Skillset
- Adds processing capabilities to documents
- Vectorization: Converts text to embeddings for semantic search
- Other capabilities: Content Safety, Language detection, etc.

### Semantic Search Setup

**Why Azure AI Search?**
Quickly retrieve any data from a large dataset with semantic understanding.

**Setup Steps:**
1. Enable identity-based authentication on Azure AI Search
2. Deploy embedding models in Azure Foundry (text-embedding-3 small/large)
3. Add new role assignment: "Cognitive Services OpenAI User" role
4. Enable Semantic Ranker in search settings
5. Add vectorizer skillset to your indexer

### Embeddings & Vector Search

**Embedding:** Vector representation of text meaning
- Used for semantic search (search by meaning, not just keywords)
- Enables hybrid search: BM25 (keyword) + Vector (semantic)

**Cosine Similarity:**
- Measures vector similarity (-1 = opposite, 1 = identical)
- Azure AI Search finds points in similar directions

### Configuration Notes

- **Replicas:** Start with 1 for learning, scale up for production
- **Parsing Mode:** Use JSON for structured document parsing
- **Alias:** Can create query aliases for semantic search
- **Production Auth:** Enable semantic ranker; use identity-based authentication