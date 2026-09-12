from llama_index.core import VectorStoreIndex
from llama_index.core import SimpleDirectoryReader
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.readers.file import PyMuPDFReader

embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en")

print("Loading PDF...")
loader = PyMuPDFReader()
documents = loader.load(file_path="./docs/steve_jobs.pdf")

print(f"Loaded {len(documents)} pages")
print("Sample text:", documents[0].text[:300])

print("Chunking and indexing...")
index = VectorStoreIndex.from_documents(
    documents,
    embed_model=embed_model,
    show_progress=True
)

index.storage_context.persist("./storage")
print("Index saved.")