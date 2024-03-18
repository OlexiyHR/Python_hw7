from app.io.input import input_text_from_console, read_text_from_file, read_text_from_file_with_pandas
from app.io.output import output_to_console, output_to_file


def main():
    # Calling functions to retrieve text
    console_text = input_text_from_console()
    file_text = read_text_from_file("data/input.txt")
    pandas_text = read_text_from_file_with_pandas("data/input.txt")

    # Printing text results to console using output function
    output_to_console(console_text)
    output_to_console(file_text)
    output_to_console(pandas_text)

    # Writing text to file using output function
    output_to_file("data/output.txt", console_text)
    output_to_file("data/output.txt", file_text)
    output_to_file("data/output.txt", pandas_text)


if __name__ == "__main__":
    main()
