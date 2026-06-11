import os

def verify_assets():

    faiss_dir = "app/rag/faiss_index"

    if not os.path.exists(faiss_dir):
        raise FileNotFoundError("FAISS index folder missing")

    print("RAG startup verified")
