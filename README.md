# TalkTube

TalkTube is a repository that facilitates generating transcripts from YouTube videos and allows for QA (Question and Answer) functionality using a Retrieval-Augmented Generation (RAG) model integrated with large language models (LLMs).

## Features

- **Transcription Generation**: Automatically generate accurate transcripts from YouTube videos.
- **Retrieval-Augmented Generation (RAG)**: Utilize advanced RAG techniques to enhance the QA process.
- **QA with LLMs**: Ask questions and get precise answers based on the transcriptions using large language models.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/talktube.git
```

### Installing ffmpeg for Whisper

Whisper requires `ffmpeg` for audio processing. The following commands show the installation process on Mac and Ubuntu operating systems.

#### MacOS (requires [Homebrew](https://brew.sh/))

```bash
brew install ffmpeg
```


#### Ubuntu 

```bash
sudo apt install ffmpeg
```


### Windows 


You can read the following article if you're working on an operating system that hasn't been mentioned earlier
 (like Windows). It contains comprehensive, step-by-step instructions on [How to install ffmpeg](https://www.hostinger.com/tutorials/how-to-install-ffmpeg).

### Configuration

You need to configure the environment variables with your API keys and other necessary values. Set the following environment variables:

#### Linux/MacOS:
```bash
export OPENAI_API_KEY='your_openai_api_key'
export ACTIVELOOP_TOKEN='your_activeloop_token'
export ACTIVELOOP_ID='your_activeloop_id'
export OPEN_SOURCE_MODEL='False'  # Set to 'True' to use an open-source model
```

#### Windows (PowerShell):
```bash
$env:OPENAI_API_KEY='your_openai_api_key'
$env:ACTIVELOOP_TOKEN='your_activeloop_token'
$env:ACTIVELOOP_ID='your_activeloop_id'
$env:OPEN_SOURCE_MODEL='False'  # Set to 'True' to use an open-source model
```

Replace ``YOUR_OPENAI_API_KEY``, ``YOUR_ACTIVELOOP_TOKEN``, and ``YOUR_ACTIVELOOP_ID`` with your actual API keys and ActiveLoop ID.
Set ``OPEN_SOURCE_MODEL`` to ``True`` if you want to use an open-source model like LLaMA, or ``False`` to use the OpenAI model.

### Example Usage

Below is an example of running the script using the provided YouTube URLs. The outputs demonstrate the use of the OpenAI model:

#### Sample Questions and Answers

**Question:** Summarize the mentions of Google according to their AI program.  
**Answer:**
- Google has been a prolific publisher of academic papers in the field of AI, even before merging with DeepMind.
- The merger of Google Brain and DeepMind created a powerful force in publishing papers at conferences.
- However, Google has now changed its AI strategy.
- The recent Google I.O. event revealed that Google plans to incorporate generative AI into various applications.
- Jeff Hinton, a prominent figure in AI, has left Google and expressed concerns about the dangers of AI.
- OpenAI, another AI company, has suffered significant financial losses.
- Overall, Google's AI program has undergone changes and developments.

**Question:** What are the key points discussed about OpenAI?  
**Answer:**
- The launch of OpenAI's chat GPT had a significant impact on the AI industry.
- OpenAI kept up with Google by reading their scientific papers.
- Transformers are a foundational part of the latest AI technology, and the concept originated from a Google study.
- Google researchers now prioritize getting their work into products before publishing, whereas before they were encouraged to publish first.
- OpenAI's claim that they read Google's Transformers paper is questioned.
- OpenAI released h2o GPT, an open-source model with different parameter sizes.
- OpenAI also released LLM Studio, a framework for fine-tuning large language models.
- OpenAI released a dataset of annotated drawings for research purposes.

**Question:** Is there any investment advice given?  
**Answer:**
- The speaker mentions that if they had to start again with under $1 million, they could make a 50% annual return.
- The question asks what method or methods the speaker would use to achieve that return if they had money to invest on a full-time basis.
- The options mentioned include flipping through 20,000 pages of Moody's Manual or similar publications, using two-fine-stick robots, hunting for great companies at a fair price, or a combination of both with opportunity costs as the final arbiter.
- The speaker states that in their particular case, they would choose to go through the 20,000 pages.
- The rest of the transcript is unrelated to the question.

**Question:** What are the main topics of the second video?  
**Answer:**
- The second video discusses a research paper by DeepMind about robo soccer and the capabilities of end-to-end reinforcement learning.
- The speaker mentions the cute appearance of the robots and the astounding adaptive behavior they exhibit.
- They compare the movement of these robots to that of Boston Dynamics robots, which are typically hard-coded.
- The speaker also mentions visiting a lab at ETH that is also working on robo soccer.
- The paper is titled "Learning Agile Soccer Skills for Bipedal Robot with Deeper Reinforcement Learning" and includes a video of someone pushing over the robots.

**Question:** Will it rain tomorrow?  
**Answer:**
- The question asked is not related to whether it will rain tomorrow.
- The answer to the question is not provided in the given transcript.
