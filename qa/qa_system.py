from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain import OpenAI, LLMChain


def setup_qa_system(retriever):
    prompt_template = """Use the following pieces of transcripts from a video to answer the question in bullet points and summarized.
    If you don't know the answer, just say that you don't know, don't try to make up an answer.

    {context}

    Question: {question}
    Summarized answer in bullet points:"""

    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )

    llm = OpenAI(model_name="gpt-3.5-turbo-16k", temperature=0)
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
