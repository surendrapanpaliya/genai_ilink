
from sentence_transformers import SentenceTransformer

_model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

def embed(texts: list[str]) -> list[list[float]]:
    # Returns a list of 384-d vectors (L2-normalized by the model)
    return _model.encode(texts, normalize_embeddings=True).tolist()
