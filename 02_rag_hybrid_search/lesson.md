## RAG on PDF Files - Lesson

### Overview
Building Retrieval-Augmented Generation (RAG) system over 152-page PDF documents using Azure AI Search.

### Key Architecture

**Hybrid Search Approach:**
- **BM25 (Keyword Search):** Traditional full-text search for exact matches
- **Vector Search:** Semantic search using embeddings
- **Combined:** Both methods together for comprehensive retrieval

### Implementation Steps

1. **Indexing:** Set up Azure AI Search index for PDF content
2. **Embedding:** Vectorize document chunks with Azure embedding models
3. **Query:** Use hybrid search to retrieve relevant documents
4. **Retrieval:** Feed retrieved context to LLM for generation

### Related Resources
- See `../01_sdk_selection_and_api/azure-index.md` for Azure AI Search setup
- See `../01_sdk_selection_and_api/lesson.md` for SDK selection and cost optimization
