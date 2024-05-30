from langchain.prompts import PromptTemplate, ChatPromptTemplate
from langchain.chains import RetrievalQA
from langchain import OpenAI, LLMChain
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import  StrOutputParser
from langchain_community.chat_models import ChatOllama
from langchain_community.embeddings import OllamaEmbeddings


def setup_qa_system(retriever, model_name="openai", temperature=0.2):
    prompt_template = """Use the following pieces of transcripts from a video to answer the question in bullet points and summarized.
    If you don't know the answer, just say that you don't know, don't try to make up an answer.
    If the question  is asked in other language, you  must answer in those language too.

    {context}

    Question: {question}
    Summarized answer in bullet points:"""

    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )

    if model_name == "openai":
        llm = OpenAI(model_name="gpt-3.5-turbo-16k", temperature=temperature)
    else:
        llm = ChatOllama(model=model_name, temperature=temperature)

    chain_type_kwargs = {"prompt": PROMPT}

    qa = RetrievalQA.from_chain_type(
        llm=llm, chain_type="stuff", retriever=retriever, chain_type_kwargs=chain_type_kwargs
    )
    return qa


def is_relevant_answer(question, answer):
    irrelevant_keywords = ["I don't know", "no answer", "not sure"]
    for keyword in irrelevant_keywords:
        if keyword.lower() in answer.lower():
            return False
    return True
