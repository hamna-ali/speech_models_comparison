import speech_recognition as sr
from pydub import AudioSegment
from googletrans import Translator  # type: ignore
import asyncio

# Step 1: Convert audio to WAV
audio = AudioSegment.from_file("audio_2.m4a")
audio.export("converted_audio.wav", format="wav")

# Step 2: Transcribe the audio
recognizer = sr.Recognizer()
with sr.AudioFile("converted_audio.wav") as source:
    audio_data = recognizer.record(source)

try:
    english_text = recognizer.recognize_google(audio_data)
    print("Transcription (English):", english_text)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio.")
    english_text = None
except sr.RequestError as e:
    print(f"Could not request results; {e}")
    english_text = None

# Step 3: Translate using async (Googletrans 4.0.2+)
async def translate_text(text):
    if text:
        translator = Translator()
        translated = await translator.translate(text, src='en', dest='fr')
        print("Translation (French):", translated.text)

# Run the async translation
if english_text:
    asyncio.run(translate_text(english_text))
