from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from llama_index.core import StorageContext, load_index_from_storage
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.groq import Groq

import os

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise RuntimeError("GROQ_API_KEY is not set. Run: $env:GROQ_API_KEY=\"your_key\"")


app = FastAPI()

# Allow React frontend to talk to this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load index once when server starts — not on every request
print("Loading index...")
embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en")
storage_context = StorageContext.from_defaults(persist_dir="./storage")
index = load_index_from_storage(storage_context, embed_model=embed_model)

llm = Groq(
    model="openai/gpt-oss-120b",
    api_key=GROQ_API_KEY
)

query_engine = index.as_query_engine(
    llm=llm,
    similarity_top_k=3
)

print("Ready!")

# Request body shape
class ChatRequest(BaseModel):
    message: str

# Chat endpoint
@app.post("/chat")
def chat(req: ChatRequest):
    response = query_engine.query(req.message)

    # Pull the source chunks too
    sources = []
    for node in response.source_nodes:
        sources.append({
            "text": node.text[:200],
            "score": round(node.score, 4)
        })

    return {
        "reply": str(response),
        "sources": sources
    }

# Health check
@app.get("/")
def root():
    return {"status": "running"}