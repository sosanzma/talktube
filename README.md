# TalkTube

TalkTube is a repository that facilitates generating transcripts from YouTube videos and allows for QA (Question and Answer) functionality using a Retrieval-Augmented Generation (RAG) model integrated with large language models (LLMs).

## Features

- **Transcription Generation**: Automatically generate accurate transcripts from YouTube videos.
- **Retrieval-Augmented Generation (RAG)**: Utilize advanced RAG techniques to enhance the QA process.
- **QA with LLMs**: Ask questions and get precise answers based on the transcriptions using large language models.
- **Easy Integration**: Seamlessly integrate the QA functionality into your projects.

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