import os
import subprocess
import webbrowser
import urllib.parse
import pywhatkit


# =====================================================
# OPEN APPLICATIONS
# =====================================================

def open_chrome():

    paths = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
    ]

    for path in paths:

        if os.path.exists(path):
            os.startfile(path)
            return True

    return False


def open_vscode():

    paths = [

        rf"C:\Users\{os.getlogin()}\AppData\Local\Programs\Microsoft VS Code\Code.exe",

        r"C:\Program Files\Microsoft VS Code\Code.exe"

    ]

    for path in paths:

        if os.path.exists(path):

            os.startfile(path)

            return True

    try:

        subprocess.Popen(["code"])

        return True

    except Exception:

        return False


def open_notepad():

    subprocess.Popen(["notepad"])


def open_calculator():

    subprocess.Popen(["calc"])


def open_file_explorer():

    subprocess.Popen(["explorer"])


# =====================================================
# WINDOWS FOLDERS
# =====================================================

def open_folder(folder):

    path = os.path.join(

        os.path.expanduser("~"),

        folder

    )

    if os.path.exists(path):

        os.startfile(path)

        return True

    return False


# =====================================================
# CLOSE APPLICATIONS
# =====================================================

def close_chrome():

    os.system("taskkill /F /IM chrome.exe")


def close_vscode():

    os.system("taskkill /F /IM Code.exe")


def close_notepad():

    os.system("taskkill /F /IM notepad.exe")


def close_calculator():

    os.system("taskkill /F /IM Calculator.exe")

    os.system("taskkill /F /IM CalculatorApp.exe")


def close_file_explorer():

    os.system("taskkill /F /IM explorer.exe")

    os.system("start explorer.exe")


# =====================================================
# YOUTUBE
# =====================================================

def open_youtube():

    webbrowser.open("https://www.youtube.com")


def play_youtube_song(song):

    pywhatkit.playonyt(song)


def open_youtube_channel(channel):

    query = urllib.parse.quote(channel)

    url = f"https://www.youtube.com/results?search_query={query}"

    webbrowser.open(url)


# =====================================================
# GOOGLE SEARCH
# =====================================================

def google_search(query):

    query = urllib.parse.quote(query)

    url = f"https://www.google.com/search?q={query}"

    webbrowser.open(url)


# =====================================================
# WEBSITES
# =====================================================

def open_gmail():

    webbrowser.open("https://mail.google.com")


def open_github():

    webbrowser.open("https://github.com")


def open_linkedin():

    webbrowser.open("https://www.linkedin.com")


def open_chatgpt():

    webbrowser.open("https://chat.openai.com")


# =====================================================
# PC CONTROL
# =====================================================

def shutdown_pc():

    os.system("shutdown /s /t 5")


def restart_pc():

    os.system("shutdown /r /t 5")


def lock_pc():

    os.system("rundll32.exe user32.dll,LockWorkStation")