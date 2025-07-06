import speech_recognition as sr
from pydub import AudioSegment
from googletrans import Translator # type: ignore

# Step 1: Convert audio to WAV (speech_recognition doesn't support m4a directly)
audio = AudioSegment.from_file("audio_2.m4a")
audio.export("converted_audio.wav", format="wav")

# Step 2: Initialize recognizer
recognizer = sr.Recognizer()

# Step 3: Load and transcribe the audio
with sr.AudioFile("converted_audio.wav") as source:
    audio_data = recognizer.record(source)

try:
    # Transcription (Speech to Text)
    english_text = recognizer.recognize_google(audio_data)
    print("Transcription (English):", english_text)

    # Translation (English to French)
    translator = Translator()
    translated = translator.translate(english_text, src='en', dest='fr')
    print("Translation (French):", translated.text)

except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio.")
except sr.RequestError as e:
    print(f"Could not request results; {e}")
