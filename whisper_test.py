import whisper
import os
import asyncio
from googletrans import Translator  # type: ignore

# Load model
model = whisper.load_model("base")

# Set up paths
script_dir = os.path.dirname(os.path.abspath(__file__))
audio_path = os.path.join(script_dir, "audio_2.m4a")

# 🟡 Load audio separately (this logs internally)
audio = whisper.load_audio(audio_path)
audio = whisper.pad_or_trim(audio)

# Get mel spectrogram
mel = whisper.log_mel_spectrogram(audio).to(model.device)

# 🟢 Now print before actual recognition
print("Recognizing audio...", flush=True)

# Detect language (optional)
_, probs = model.detect_language(mel)
# print(f"Detected language: {max(probs, key=probs.get)}")

# Decode
options = whisper.DecodingOptions()
result = whisper.decode(model, mel, options)

english_text = result.text.strip()
print("Transcription (English):", english_text)

# Translate to French
async def translate_text(text):
    if text:
        translator = Translator()
        translated = await translator.translate(text, src='en', dest='fr')
        print("Translation (French):", translated.text)

if english_text:
    asyncio.run(translate_text(english_text))
