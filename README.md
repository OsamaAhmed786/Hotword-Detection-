# 🚨 Hotword Detection (Emergency Trigger)

A simple **hotword detection system in Python** that listens to the microphone input and triggers an emergency action whenever a specific keyword (hotword) is spoken.  
Similar to wake word systems like **"Hey Siri"** or **"Alexa"**.

---

## 🔹 Features
- Listens continuously for a custom hotword (default: **"emergency"**).
- Works offline using [SpeechRecognition](https://pypi.org/project/SpeechRecognition/).
- Easy to integrate with your application (e.g., trigger alerts, send SMS, call APIs).
- Lightweight and beginner friendly.

---

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/hotword-detection.git
   cd hotword-detection
2. Create and activate a virtual environment (recommended):
    ```
    python -m venv venv
    venv\Scripts\activate   # On Windows
    source venv/bin/activate # On Mac/Linux

3. Install dependencies:
   ```
   pip install -r requirements.txt

## ▶️ Usage

Run the script:

    python main.py


Speak the hotword ("emergency") into your microphone.
If detected, it will trigger an alert:

    Listening for hotword... (say 'emergency')
    Heard: emergency
    🚨 Emergency Hotword Detected! 🚨

## ⚡ Customization

Change the hotword:

    HOTWORD = "help"


Replace the action with your custom code (e.g., API call, send SMS, trigger alarm):

    if HOTWORD in text:
        # your emergency action here
        send_sms()

## 🚀 Future Improvements

Add support for multiple hotwords.

Integrate with Picovoice Porcupine for more accurate wake word detection.

Run fully offline without Google SpeechRecognition API.

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## 📜 License
MIT License © 2025

## 👨‍💻 Author
Developed by Osama Ahmed 🚀
