from config import OPENAI_API_KEY, ACTIVELOOP_TOKEN
import os
from download.youtube_downloader import download_mp4_from_youtube
from transcribe.transcriber import transcribe_video
from config import ACTIVELOOP_ID, OPEN_SOURCE_MODEL
from process.text_processor import split_text
from retriever.deep_lake_retriever import create_retriever
from qa.qa_system import setup_qa_system, is_relevant_answer

urls = ["https://www.youtube.com/watch?v=v4T1oknATGU", "https://www.youtube.com/watch?v=cjs7QKJNVYM"]


if os.path.exists('data/text_2videos.txt'):
    print("The file text_2videos.txt already exists. Reading its content.")
    with open('data/text_2videos.txt', 'r') as file:
        text = file.read()
else:
    videos_details = download_mp4_from_youtube(urls, 1)
    results = []
    for video in videos_details:
        result = transcribe_video(video[0])
        results.append(result)
        print(f"Transcription for {video[0]}:\n{result}\n")
    all_transcriptions = "\n\n".join(results)
    with open('data/text_2videos.txt', 'w') as file:
        file.write(all_transcriptions)
    with open('data/text_2videos.txt', 'r') as file:
        text = file.read()

docs = split_text(text)
retriever = create_retriever(docs, ACTIVELOOP_ID, "talktube_video1", open_model=OPEN_SOURCE_MODEL)

# Choose the model you want to use, e.g., "llama3" for ChatOllama, "openai" for OpenAI
model_name = "llama3" if OPEN_SOURCE_MODEL else "openai"
qa = setup_qa_system(retriever, model_name=model_name)

questions = [
    "Summarize the mentions of Google according to their AI program.",
    "What are the key points discussed about OpenAI?",
    "There is some inversion advice given?",
    "What are the main topics of the second video?",
    "Will it rain tomorrow?"
]

for question in questions:
    answer = qa.run(question)
    if not is_relevant_answer(question, answer):
        answer = "I don't know the answer to that question."
    print(f"Question: {question}\nAnswer: {answer}\n")