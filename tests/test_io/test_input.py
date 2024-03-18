from app.io.input import read_text_from_file, read_text_from_file_with_pandas


# Create temporary files with content
sample_text_file = "sample.txt"
with open(sample_text_file, "w") as file:
    file.write("Sample text\n Line 2\n Line 3")

# Create a file with special characters
    special_file = "special_file.txt"
    with open(special_file, "w") as special:
        special.write("Line with $pecial characters")

void_file = "void.txt"
with open(void_file, 'w') as void:
    pass

    # Test cases for read_text_from_file function
    def test_read_text_from_file1():
        assert read_text_from_file(sample_text_file) == "Sample text\n Line 2\n Line 3"


    def test_read_text_from_file2():
        # Test reading content from a non-existent file
        assert read_text_from_file("non_existent_file.txt") == "File not found."


    def test_read_text_from_file3():
        # Test reading content from a void file
        assert read_text_from_file(void_file) == ""


    def test_read_text_from_file_with_pandas1():
        assert read_text_from_file_with_pandas(sample_text_file) == "Sample text\n     Line 2\n     Line 3"


    def test_read_text_from_file_with_pandas2():
        # Test reading content from a non-existent file
        assert read_text_from_file_with_pandas("non_existent_file.txt") == "File not found."


    def test_read_text_from_file_with_pandas3():
        # Test reading content from a void file
        assert read_text_from_file_with_pandas(special_file) == "Line with $pecial characters"
