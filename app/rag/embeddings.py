import os
from langchain_huggingface import HuggingFaceEmbeddings

#token=os.getenv("HF_TOKEN")

_embedding_model = None


def get_embedding_model():
    global _embedding_model

    if _embedding_model is None:
        _embedding_model = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2",
            encode_kwargs={"normalize_embeddings": True}
        )

    return _embedding_model


def embed_text(texts):
    model = get_embedding_model()
    return model.embed_documents(texts)