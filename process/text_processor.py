from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document

def split_text(text):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, chunk_overlap=0, separators=[" ", ",", "\n"]
    )
    texts = text_splitter.split_text(text)
    docs = [Document(page_content=t) for t in texts]
    return docs
