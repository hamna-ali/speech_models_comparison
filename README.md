# 🗣️ Speech Models Comparison (Whisper vs Vosk vs SpeechRecognition)

This repository demonstrates and compares three popular speech-to-text tools in Python:
- **Whisper** by OpenAI (offline, deep learning-based)
- **Vosk** (offline, lightweight Kaldi-based)
- **SpeechRecognition** with Google Web Speech API (online)

Each tool is tested on the same audio file (`audio_2.m4a`) for:
- 🗣️ **Speech Recognition**
- 📄 **Transcription** (English)
- 🌐 **Translation** (to French via `googletrans`)

---


# 🔧 Install dependencies:
- pip install -r requirements.txt

---

# 📊 Goals of This Project
- Compare accuracy, setup, and limitations of Whisper, Vosk, and SpeechRecognition

- Evaluate translation quality using googletrans

- Demonstrate a complete pipeline from audio to multilingual output

---

# ✅ Notes
- Whisper prints a warning if run on CPU (safe to ignore):
- UserWarning: FP16 is not supported on CPU; using FP32 instead

- Vosk logs can be suppressed by redirecting stderr or setting log level

- You can replace audio_2.m4a with your own audio clips (ensure clear English speech)

