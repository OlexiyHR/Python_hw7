import pandas as pd


def input_text_from_console():
    """
    Function to input text from the console.

    Returns:
        str: The text entered from the console.
    """
    return input("Enter text from the console: ")


def read_text_from_file(file_path):
    """
    Function to read text from a file using Python's built-in capabilities.

    Parameters:
        file_path (str): The path to the file.

    Returns:
        str: The content of the file.
            If the file is not found, returns the string "File not found.".
    """
    try:
        with open(file_path, 'r') as file:
            text = file.read()
        return text
    except FileNotFoundError:
        return "File not found."


def read_text_from_file_with_pandas(file_path):
    """
    Function to read text from a file using the pandas' library.

    Parameters:
        file_path (str): The path to the file.

    Returns:
        str: The content of the file as a string.
        If the file is not found, returns the string "File not found.".
    """
    try:
        data = pd.read_csv(file_path, header=None)
        return data.to_string(index=False, header=False)
    except FileNotFoundError:
        return "File not found."
