from speak import speak
from listen import listen
from commands import execute_command


def print_banner():
    print("=" * 60)
    print("         JARVIS AI ASSISTANT")
    print("=" * 60)


def main():

    print_banner()

    speak("Hello Gokul. I am Jarvis. How can I help you?")

    while True:

        try:

            command = listen()

            if not command:
                continue

            should_continue = execute_command(command)

            if not should_continue:
                break

        except KeyboardInterrupt:

            print("\nJarvis stopped by user.")

            speak("Goodbye Gokul.")

            break

        except Exception as e:

            print(f"Error: {e}")

            speak("Sorry, something went wrong.")


if __name__ == "__main__":
    main()