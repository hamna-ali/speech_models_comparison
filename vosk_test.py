import os
import wave
import asyncio
from vosk import Model, KaldiRecognizer
from pydub import AudioSegment
from googletrans import Translator  # type: ignore
import json

# Setup paths
script_dir = os.path.dirname(os.path.abspath(__file__))

# Input & output audio
input_path = os.path.join(script_dir, "audio_2.m4a")
wav_path = os.path.join(script_dir, "converted_audio_vosk.wav")

# Convert .m4a to .wav (mono, 16kHz for Vosk)
audio = AudioSegment.from_file(input_path)
audio = audio.set_channels(1).set_frame_rate(16000)
audio.export(wav_path, format="wav")

# Use Vosk model from C:\Ai_ML\whisper_vosk
model_path = os.path.abspath(os.path.join(script_dir, "..", "vosk-model-small-en-us-0.15"))
if not os.path.exists(model_path):
    print(f"❌ Vosk model not found at: {model_path}")
    exit()

model = Model(model_path)
recognizer = KaldiRecognizer(model, 16000)

# Transcribe
wf = wave.open(wav_path, "rb")
print()
print("Audio file loaded:", wav_path)
print("Recognizing audio...")

results = []
while True:
    data = wf.readframes(4000)
    if len(data) == 0:
        break
    if recognizer.AcceptWaveform(data):
        res = json.loads(recognizer.Result())
        results.append(res.get("text", ""))

# Final result
final_res = json.loads(recognizer.FinalResult())
results.append(final_res.get("text", ""))

# Combine transcription
english_text = " ".join(results).strip()
print("Transcription (English):", english_text)

# Translate to French
async def translate_text(text):
    if text:
        translator = Translator()
        translated = await translator.translate(text, src='en', dest='fr')
        print("Translation (French):", translated.text)

if english_text:
    asyncio.run(translate_text(english_text))
