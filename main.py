import speech_recognition as sr
import sys
sys.stdout.reconfigure(encoding='utf-8')


# Define your hotword
HOTWORD = "Hey brave haven"

def listen_for_hotword():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    print("Listening for hotword... (say 'emergency')")

    with mic as source:
        recognizer.adjust_for_ambient_noise(source)  # background noise adjust
        while True:
            try:
                audio = recognizer.listen(source)
                text = recognizer.recognize_google(audio).lower()
                print("Heard:", text)

                if HOTWORD in text:
                    print("Emergency Hotword Detected! ")
                    # yahan apna trigger action likho (SMS, API call, etc.)
                    break

            except sr.UnknownValueError:
                # Agar speech samajh na aaye
                continue
            except sr.RequestError:
                print("API unavailable.")
                break

if __name__ == "__main__":
    listen_for_hotword()
