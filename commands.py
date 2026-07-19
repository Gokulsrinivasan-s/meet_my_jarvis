from speak import speak
from brain import ask_ai

from apps import (
    open_chrome,
    open_vscode,
    open_notepad,
    open_calculator,
    open_file_explorer,
    open_folder,

    close_chrome,
    close_vscode,
    close_notepad,
    close_calculator,
    close_file_explorer,

    open_youtube,
    play_youtube_song,
    open_youtube_channel,
    google_search,
    open_gmail,
    open_github,
    open_linkedin,
    open_chatgpt,

    shutdown_pc,
    restart_pc,
    lock_pc
)

from file_manager import (
    search_file,
    create_folder,
    create_text_file
)


def execute_command(command):

    command = command.lower().strip()

    # -------------------------
    # Basic Commands
    # -------------------------

    if "hello" in command:

        speak("Hello Gokul")

    elif "how are you" in command:

        speak("I am doing great")

    elif "your name" in command:

        speak("My name is Jarvis")

    # -------------------------
    # Open Applications
    # -------------------------

    elif "open chrome" in command:

        speak("Opening Chrome")
        open_chrome()

    elif "open vscode" in command or "open visual studio code" in command:

        speak("Opening Visual Studio Code")
        open_vscode()

    elif "open notepad" in command:

        speak("Opening Notepad")
        open_notepad()

    elif "open calculator" in command:

        speak("Opening Calculator")
        open_calculator()

    elif "open file explorer" in command:

        speak("Opening File Explorer")
        open_file_explorer()

    # -------------------------
    # Close Applications
    # -------------------------

    elif "close chrome" in command:

        speak("Closing Chrome")
        close_chrome()

    elif "close vscode" in command or "close visual studio code" in command:

        speak("Closing Visual Studio Code")
        close_vscode()

    elif "close notepad" in command:

        speak("Closing Notepad")
        close_notepad()

    elif "close calculator" in command:

        speak("Closing Calculator")
        close_calculator()

    elif "close file explorer" in command:

        speak("Restarting File Explorer")
        close_file_explorer()

    # -------------------------
    # Website Commands
    # -------------------------

    elif "open youtube" in command:

        speak("Opening YouTube")
        open_youtube()

    elif command.startswith("play "):

        song = command.replace("play", "").strip()

        if song:

            speak(f"Playing {song}")
            play_youtube_song(song)

        else:

            speak("Please tell the song name.")

    elif command.startswith("open youtube channel"):

        channel = command.replace("open youtube channel", "").strip()

        if channel:

            speak(f"Opening {channel} channel")
            open_youtube_channel(channel)

        else:

            speak("Please tell the channel name.")

    elif command.startswith("search"):

        query = command.replace("search", "").strip()

        if query:

            speak(f"Searching Google for {query}")
            google_search(query)

        else:

            speak("Please tell me what to search.")

    elif "open gmail" in command:

        speak("Opening Gmail")
        open_gmail()

    elif "open github" in command:

        speak("Opening GitHub")
        open_github()

    elif "open linkedin" in command:

        speak("Opening LinkedIn")
        open_linkedin()

    elif "open chat g p t" in command or "open chatgpt" in command:

        speak("Opening ChatGPT")
        open_chatgpt()

    # -------------------------
    # Folder Commands
    # -------------------------

    elif "open downloads" in command:

        speak("Opening Downloads")
        open_folder("Downloads")

    elif "open documents" in command:

        speak("Opening Documents")
        open_folder("Documents")

    elif "open desktop" in command:

        speak("Opening Desktop")
        open_folder("Desktop")

    # -------------------------
    # File Management
    # -------------------------

    elif command.startswith("find"):

        filename = command.replace("find", "").strip()

        speak(f"Searching for {filename}")

        result = search_file(filename)

        if result:

            speak("I found your file")

            for file in result[:10]:
                print(file)

        else:

            speak("File not found")

    elif command.startswith("create folder"):

        folder_name = command.replace("create folder", "").strip()

        folder_name = folder_name.replace("named", "")
        folder_name = folder_name.replace("name is", "").strip()

        if folder_name:

            if create_folder(folder_name):

                speak("Folder created successfully")

            else:

                speak("Folder already exists")

        else:

            speak("Please tell the folder name")

    elif command.startswith("create file"):

        file_name = command.replace("create file", "").strip()

        file_name = file_name.replace("named", "")
        file_name = file_name.replace("name is", "").strip()

        if file_name:

            path = create_text_file(file_name)

            print("Created:", path)

            speak("File created successfully on Desktop")

        else:

            speak("Please tell me the file name")

    # -------------------------
    # System Control
    # -------------------------

    elif "shutdown" in command:

        speak("Shutting down computer")
        shutdown_pc()

    elif "restart" in command:

        speak("Restarting computer")
        restart_pc()

    elif "lock pc" in command or "lock computer" in command:

        speak("Locking computer")
        lock_pc()

    # -------------------------
    # Exit
    # -------------------------

    elif (
        "exit jarvis" in command
        or "close jarvis" in command
        or command == "exit"
        or "bye" in command
    ):

        speak("Goodbye Gokul")

        return False

    # -------------------------
    # AI Fallback
    # -------------------------

    else:

        speak("Let me think")

        answer = ask_ai(command)

        print("\nJarvis:\n")
        print(answer)

        speak(answer)

    return True