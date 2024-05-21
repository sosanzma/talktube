from config import OPENAI_API_KEY, ACTIVELOOP_TOKEN
from download.youtube_downloader import download_mp4_from_youtube
from transcribe.transcriber import transcribe_video
from config import ACTIVELOOP_ID
from process.text_processor import split_text
from retriever.deep_lake_retriever import create_retriever
from qa.qa_system.py import setup_qa_system, is_relevant_answer

urls = ["https://www.youtube.com/watch?v=v4T1oknATGU", "https://www.youtube.com/watch?v=cjs7QKJNVYM"]

if os.path.exists('text_2videos.txt'):
    print("The file text_2videos.txt already exists. Reading its content.")
    with open('text_2videos.txt', 'r') as file:
        text = file.read()
else:
    videos_details = download_mp4_from_youtube(urls, 1)
    results = []
    for video in videos_details:
        result = transcribe_video(video[0])
        results.append(result)
        print(f"Transcription for {video[0]}:\n{result}\n")
    all_transcriptions = "\n\n".join(results)
    with open('text_2videos.txt', 'w') as file:
        file.write(all_transcriptions)
    with open('text_2videos.txt', 'r') as file:
        text = file.read()

docs = split_text(text)
retriever = create_retriever(docs, "sosanzma", "youtube_qa")
qa = setup_qa_system(retriever)

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
