from langchain.vectorstores import DeepLake
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain_community.embeddings import OllamaEmbeddings


def create_retriever(docs, org_id, dataset_name, open_model=True, distance_metric = 'cos', k = 4 ):
    if open_model:
        embeddings = OllamaEmbeddings(model='llama3')
    else:
        embeddings = OpenAIEmbeddings(model='text-embedding-ada-002')

    dataset_path = f"hub://{org_id}/{dataset_name}"
    db = DeepLake(dataset_path=dataset_path, embedding_function=embeddings)
    db.add_documents(docs)
    retriever = db.as_retriever()
    retriever.search_kwargs['distance_metric'] = distance_metric
    retriever.search_kwargs['k'] = k
    return retriever
