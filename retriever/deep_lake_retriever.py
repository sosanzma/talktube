from langchain.vectorstores import DeepLake
from langchain.embeddings.openai import OpenAIEmbeddings

def create_retriever(docs, org_id, dataset_name):
    embeddings = OpenAIEmbeddings(model='text-embedding-ada-002')
    dataset_path = f"hub://{org_id}/{dataset_name}"
    db = DeepLake(dataset_path=dataset_path, embedding_function=embeddings)
    db.add_documents(docs)
    retriever = db.as_retriever()
    retriever.search_kwargs['distance_metric'] = 'cos'
    retriever.search_kwargs['k'] = 4
    return retriever
