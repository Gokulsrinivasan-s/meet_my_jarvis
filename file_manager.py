import os

# =====================================================
# HOME DIRECTORY
# =====================================================

HOME = os.path.expanduser("~")


# =====================================================
# GET DESKTOP PATH
# =====================================================

def get_desktop_path():
    """
    Return Desktop path.
    Supports normal Desktop and OneDrive Desktop.
    """

    paths = [
        os.path.join(HOME, "Desktop"),
        os.path.join(HOME, "OneDrive", "Desktop")
    ]

    for path in paths:
        if os.path.exists(path):
            return path

    return os.path.join(HOME, "Desktop")


# =====================================================
# SEARCH FILE
# =====================================================

def search_file(filename):
    """
    Search files in the user's PC.
    """

    results = []

    for root, dirs, files in os.walk(HOME):

        for file in files:

            if filename.lower() in file.lower():

                results.append(
                    os.path.join(root, file)
                )

    return results


# =====================================================
# CREATE FOLDER
# =====================================================

def create_folder(folder_name):
    """
    Create a folder on Desktop.
    """

    desktop = get_desktop_path()

    folder_path = os.path.join(
        desktop,
        folder_name
    )

    if not os.path.exists(folder_path):

        os.makedirs(folder_path)

        return True

    return False


# =====================================================
# CREATE TEXT FILE
# =====================================================

def create_text_file(file_name):
    """
    Create a text file on Desktop.
    """

    if not file_name.endswith(".txt"):
        file_name += ".txt"

    desktop = get_desktop_path()

    file_path = os.path.join(
        desktop,
        file_name
    )

    with open(file_path, "w", encoding="utf-8") as file:

        file.write("Created by Jarvis AI Assistant")

    return file_path


# =====================================================
# OPEN FILE USING PATH
# =====================================================

def open_file(path):
    """
    Open file using full path.
    """

    if os.path.exists(path):

        os.startfile(path)

        return True

    return False


# =====================================================
# OPEN FILE BY NAME
# =====================================================

def open_file_by_name(file_name):
    """
    Search and open a file by name.
    """

    for root, dirs, files in os.walk(HOME):

        for file in files:

            if file_name.lower() in file.lower():

                full_path = os.path.join(
                    root,
                    file
                )

                os.startfile(full_path)

                return True

    return False


# =====================================================
# OPEN FOLDER BY NAME
# =====================================================

def open_folder_by_name(folder_name):
    """
    Search and open a folder by name.
    """

    for root, dirs, folders in os.walk(HOME):

        for folder in folders:

            if folder.lower() == folder_name.lower():

                full_path = os.path.join(
                    root,
                    folder
                )

                os.startfile(full_path)

                return True

    return False