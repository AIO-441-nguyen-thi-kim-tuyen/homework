import os

import pytest

from homework.module_1_week_2.word_count import word_count


def test_word_count_basic():
    """Tests the word count for a simple file."""
    # Create a temporary test file with known content
    with open("test_file.txt", "w") as f:
        f.write("This is a test sentence. Here are more words.")

    expected_output = {
        "this": 1,
        "is": 1,
        "a": 1,
        "test": 1,
        "sentence": 1,
        "here": 1,
        "are": 1,
        "more": 1,
        "words": 1
    }

    word_counts = word_count("test_file.txt")
    print(word_counts)
    assert word_counts == expected_output

    # Remove the temporary test file after the test
    os.remove("test_file.txt")


def test_word_count_empty_file():
    """Tests the function with an empty file."""
    with open("empty_file.txt", "w") as f:
        pass  # Empty file

    expected_output = {}

    word_counts = word_count("empty_file.txt")
    assert word_counts == expected_output

    # Remove the temporary test file after the test
    os.remove("empty_file.txt")


def test_word_count_nonexistent_file():
    """Tests the function with a non-existent file."""
    # Expected to raise a FileNotFoundError
    with pytest.raises(FileNotFoundError):
        word_count("nonexistent_file.txt")


def test_word_count_case_insensitivity():
    """Tests the function to check if it's case-insensitive."""
    # Create a temporary test file with mixed case words
    with open("mixed_case.txt", "w") as f:
        f.write("This Is A MiXeD cAsE TeXt.")

    expected_output = {
        "this": 1,
        "is": 1,
        "a": 1,
        "mixed": 1,
        "case": 1,
        "text": 1,
    }

    word_counts = word_count("mixed_case.txt")
    assert word_counts == expected_output

    # Remove the temporary test file after the test
    os.remove("mixed_case.txt")
