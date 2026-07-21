## SDK Selection & Token Sizing Guide

### Token Size Reference

**One token ≈ 4 English characters ≈ 0.75 words**

- Min `max_output_tokens`: **16** (reasoning models need headroom for internal tokens before output)
- Practical minimums: ~50 tokens for a sentence, ~200–300 for a paragraph
- Complex generation (code, queries, structured output): ~150–500+ tokens depending on complexity
- Test with the [OpenAI tokenizer](https://platform.openai.com/tokenizer)

**Token counting by SDK:**

```python
# OpenAI SDK
import tiktoken
enc = tiktoken.encoding_for_model("gpt-4")
token_count = len(enc.encode(your_prompt))

# Anthropic SDK
# Use Claude API response usage field (returned in each response)
# or estimate: Claude uses ~1.33x OpenAI token counts
```

---

### SDK Comparison Table

| SDK                    | What it's for                                                                                                                                                                       | Endpoint                                                                    | Best for                          |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------- |
| **Foundry SDK**        | Thin-client SDK over all Foundry project APIs. Access to Foundry Models and platform tools (file search, code interpreter, web search, memory, SharePoint, WorkIQ, Fabric IQ, MCP). | `https://<resource-name>.services.ai.azure.com/api/projects/<project-name>` | Agents, project-scoped tools, RLS |
| **Agent Framework**    | Hosted agents and multi-agent systems. The `foundry` package depends on Foundry SDK. Run in your own process or as Foundry Hosted Agents.                                          | Responses API in the project endpoint, via `FoundryChatClient`.             | Multi-agent systems, serverless   |
| **OpenAI SDK**         | Full OpenAI API surface, including embeddings. Best latency and maximum OpenAI compatibility.                                                                                       | `https://<resource-name>.openai.azure.com/openai/v1`                        | Fast calls, embeddings, GPT models |
| **Anthropic SDK**      | Anthropic Claude models deployed in Foundry.                                                                                                                                        | `https://<resource-name>.services.ai.azure.com/anthropic`                   | Claude models, complex reasoning  |
| **Foundry Tools SDKs** | Prebuilt solutions (Vision, Speech, Content Safety, Document Intelligence, Language, Translator, Azure AI Search).                                                                 | Tool-specific endpoints.                                                    | Specialized AI services          |

---

### When to Use Each SDK

#### **Foundry SDK**
Use when:
- Building agents with platform tools (memory, web search, code interpreter, MCP)
- You need project-scoped row-level security (RLS) and data isolation
- Running evaluations or tracing in Foundry
- Accessing multiple Foundry models through one endpoint

**Trade-off:** Slightly higher latency than direct OpenAI SDK (goes through project layer).

---

#### **OpenAI SDK** (`/openai/v1`)
Use when:
- **Embeddings required** (project endpoint doesn't support embeddings yet)
- **Maximum latency** is critical (direct endpoint, no project routing overhead)
- **Cost sensitive** (slightly lower token costs, direct model access)
- Full OpenAI API compatibility needed (Chat Completions, fine-tuning, etc.)

**Trade-off:** No access to Foundry-exclusive tools; no project-level RLS.

---

#### **Anthropic SDK**
Use when:
- Working exclusively with Claude models deployed in Foundry
- Complex reasoning required (code generation, multi-step extraction, analysis)
- Claude-specific features needed (extended thinking, tool use patterns)

**Response format differs from OpenAI:**
```python
# OpenAI: response.output_text
# Claude: response.content[0].text
```

---

#### **Agent Framework**
Use when:
- Building multi-agent systems in code
- Want to deploy agents as Foundry Hosted Agents (auto-scaling, managed endpoint)
- Need orchestration across multiple models or tools

---

#### **Foundry Tools SDKs**
Use when:
- Document Intelligence: Extracting text/tables from PDFs or documents
- Content Safety: Analyzing user inputs for harmful content
- Vision: Analyzing images or visual content
- Speech: Speech-to-text or text-to-speech capabilities
- Language: Retiring March 31, 2029 — migrate to Foundry models instead

**Best for:** Specialized AI services. Not required for general text-to-SQL or reasoning tasks.

---

### Cost Optimization Tips

- **Haiku models** are ~2x cheaper than Sonnet → use for simple, low-reasoning tasks
- **Claude Sonnet** offers best reasoning/speed/cost trade-off → use for extraction and complex generation
- **Opus** is most expensive → reserve for highest-reasoning demands or when Sonnet times out

**Watch out for:**
- Rate limits per model (different quota per SDK)
- Token counting differences (Claude ≈ 1.33x OpenAI; use actual API response usage)
- Error handling differs slightly between SDKs
- Response structure: OpenAI returns `response.output_text`; Claude returns `response.content[0].text`

---

### Estimating Token Budgets

Use `tiktoken` to measure actual token counts before deployment:

```python
import tiktoken

# For OpenAI models
enc = tiktoken.encoding_for_model("gpt-4")
tokens = len(enc.encode(your_prompt))

# For Claude models
# Use the response usage field from the API or estimate:
# Claude tokens ≈ 1.33 × OpenAI token count (approximate)
```

**Typical token allocations:**
- Simple routing/classification: ~50–150 tokens (input + output)
- Extraction with context: ~300–800 tokens
- Complex generation (code, queries, structured output): ~500–1500 tokens
- Keep prompts + reference docs under 2,000 tokens total for optimal performance

---

### Key Takeaways

| Scenario | SDK | Endpoint | Why |
|----------|-----|----------|-----|
| Fast routing, low-cost | OpenAI | `/openai/v1` | Low latency, affordable |
| Complex reasoning tasks | Anthropic | `/anthropic` | Claude's superior reasoning |
| Embeddings | OpenAI | `/openai/v1` | Only endpoint that supports it |
| Project tools (memory, RLS) | Foundry | `/api/projects/{...}` | Project-scoped isolation |
| Serverless agents | Agent Framework | Project endpoint | Managed scaling |