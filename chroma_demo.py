
import chromadb
from chromadb.config import Settings
from embedder import embed

# 1) Start a persistent client (./chroma_db folder will be created)
client = chromadb.PersistentClient(path="./chroma_db", settings=Settings(anonymized_telemetry=False))

# 2) Create or get a collection; set cosine distance (common for text)
col = client.get_or_create_collection(
    name="docs",
    metadata={"hnsw:space": "cosine"}
)

# 3) Sample data
docs = [
    "RAG combines retrieval with generation to answer questions.",
    "GitHub Copilot accelerates coding with AI suggestions.",
    "PostgreSQL with pgvector enables vector similarity search.",
    "Chroma is a lightweight local vector database.",
    "Transformers use attention instead of recurrence."
]
ids = [f"d{i}" for i in range(len(docs))]
embs = embed(docs)

# 4) Upsert into Chroma
col.upsert(
    ids=ids,
    documents=docs,
    embeddings=embs,
    metadatas=[{"source": "demo"} for _ in docs],
)

# 5) Query: semantic search
query = "How do I search semantically in Postgres?"
qvec = embed([query])[0]
res = col.query(query_embeddings=[qvec], n_results=3)

print("Query:", query)
for i, (doc_id, doc_txt) in enumerate(zip(res["ids"][0], res["documents"][0]), 1):
    print(f"{i}. {doc_id} -> {doc_txt}")
