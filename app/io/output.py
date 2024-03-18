import pandas as pd


def output_to_console(text):
    """
    Function to output text to the console.

    Args:
        text (str): The text to be output to the console.
    """
    print(text)


def output_to_file(file_path, text):
    """
    Function to output text to a file using Python's built-in capabilities.

    Args:
        file_path (str): The path to the file.
        text (str): The text to be written to the file.
    """
    try:
        with open(file_path, 'w') as file:
            file.write(text)
    except IOError:
        print("Error: Unable to write to the file.")


def output_to_file_with_pandas(file_path, text):
    """
    Function to output text to a file using the pandas' library.

    Parameters:
        file_path (str): The path to the file.
        text (str): The text to be written to the file.
    """
    try:
        with open(file_path, 'ц') as file:
            file.write(pd.DataFrame({'Text': [text]}).to_string(index=False, header=False))
    except IOError:
        print("Error: Unable to write to the file.")
