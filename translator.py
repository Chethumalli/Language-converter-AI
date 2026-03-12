import speech_recognition as sr
from deep_translator import GoogleTranslator

def translate_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("🎤 Speak in any language...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("Detected Speech:", text)

        translated = GoogleTranslator(source='auto', target='en').translate(text)

        print("Translated to English:", translated)

        return text, translated

    except Exception as e:
        print("Error:", e)
        return None, None


if __name__ == "__main__":
    translate_speech()