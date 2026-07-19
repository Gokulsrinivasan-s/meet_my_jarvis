import pyttsx3

# Initialize the speech engine
engine = pyttsx3.init()

# Configure voice
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

# Speech rate
engine.setProperty("rate", 170)

# Volume (0.0 to 1.0)
engine.setProperty("volume", 1.0)


def speak(text):
    """
    Convert text to speech.
    """
    print(f"Jarvis: {text}")
    engine.say(text)
    engine.runAndWait()