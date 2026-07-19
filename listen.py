import speech_recognition as sr


def listen():
    recognizer = sr.Recognizer()

    recognizer.pause_threshold = 1
    recognizer.energy_threshold = 300

    with sr.Microphone() as source:

        print("\nListening...")

        recognizer.adjust_for_ambient_noise(source, duration=2)

        try:
            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=8
            )

        except sr.WaitTimeoutError:
            print("No speech detected.")
            return ""

    try:

        print("Recognizing...")

        text = recognizer.recognize_google(
            audio,
            language="en-IN"
        )

        print("You:", text)

        return text.lower()

    except sr.UnknownValueError:
        print("Sorry, I couldn't understand.")
        return ""

    except sr.RequestError:
        print("Internet connection problem.")
        return ""

    except Exception as e:
        print("Error:", e)
        return ""