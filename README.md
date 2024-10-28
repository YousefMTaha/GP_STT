# Speech-to-Text Pipeline with Whisper and Common Voice Dataset

This project implements a speech-to-text model using OpenAI's Whisper architecture, specifically leveraging the "whisper-large-v3" model for high-quality transcription. The pipeline is designed to utilize GPU if available, defaulting to CPU otherwise.

## Features

- Automatic Speech Recognition (ASR) using Whisper.
- Supports GPU acceleration if available.
- Configured for English language transcription.
- Removes unnecessary metadata from the dataset for optimized performance.

# Model Links

Official Website
```bash
https://openai.com/index/whisper
```

Huggingface
```bash
https://huggingface.co/openai/whisper-large-v3
```

## Evaluation's Dataset

```bash
https://huggingface.co/datasets/mozilla-foundation/common_voice_17_0
```

# Installation

First, clone the repo:

```bash
git clone https://github.com/YousefMTaha/GP-STT
```

Second, create python virtual environment and activate it:

```bash
python3 -m venv venv
.\venv/Scripts/activate.
```

Third, install the required dependencies by running one of these two commands:

```bash
pip install jiwer flask torch librosa datasets evaluate torchaudio transformers huggingface_hub 'accelerate>=0.26.0'
```

Or

```bash
pip install jiwer
pip install flask
pip install torch
pip install librosa
pip install datasets
pip install evaluate
pip install torchaudio
pip install transformers
pip install huggingface_hub
pip install 'accelerate>=0.26.0'
```
