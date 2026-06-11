from langchain_community.vectorstores import FAISS
from app.rag.embeddings import get_embedding_model

VECTOR_DB_PATH = "app/rag/faiss_index"

_db = None


def get_db():
    global _db

    if _db is None:
        embedding_model = get_embedding_model()

        _db = FAISS.load_local(
            VECTOR_DB_PATH,
            embedding_model,
            allow_dangerous_deserialization=True
        )

    return _db
    #Without it, modern LangChain often throws:
    #ValueError:
    # The de-serialization relies loading a pickle file.