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

Last, install the required dependencies by running one of these two commands:

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

## Run project

First, run AppRouter.py file

```bash
python AppRouter.py
```

Then, check if your file run successfully or not by try this IP: ('http://127.0.0.1:5001') in your browser.

Send your voice to the model using POST method use this IP ('http://127.0.0.1:5001/stt')

If you use android or ios emulater you can use this IP ('http://10.0.2.2:5001/stt')