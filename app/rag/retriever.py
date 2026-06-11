from app.rag.vectorstore import get_db


def retrieve_context(
    query: str,
    k: int = 4
):

    docs = get_db().similarity_search(query, k=k)

    context = "\n".join(
        doc.page_content
        for doc in docs
    )

    return context
