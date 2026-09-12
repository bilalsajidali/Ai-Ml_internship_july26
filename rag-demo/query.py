from llama_index.core import StorageContext, load_index_from_storage
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.groq import Groq

import os

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise RuntimeError("GROQ_API_KEY is not set. Run: $env:GROQ_API_KEY=\"your_key\"")


# Load the saved index from disk
print("Loading index...")
embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en")
storage_context = StorageContext.from_defaults(persist_dir="./storage")
index = load_index_from_storage(storage_context, embed_model=embed_model)

# Hook up Groq LLM
llm = Groq(
    model="openai/gpt-oss-120b",
    api_key=GROQ_API_KEY
)

# Build the query engine
query_engine = index.as_query_engine(
    llm=llm,
    similarity_top_k=3   # retrieve top 3 most relevant chunks
)

# Ask a question about your PDF
print("Querying...\n")
response = query_engine.query("when was apple founded?")

print("Answer:", response)

# Also print which chunks it used
print("\n--- Sources used ---")
for i, node in enumerate(response.source_nodes):
    print(f"\nChunk {i+1} (score: {round(node.score, 4)}):")
    print(node.text[:200], "...")