from homework.module_1_week_2.count_chars import count_chars


def test_count_chars_basic():
    """Tests the character count for a simple string."""
    input_string = "Happiness"
    expected_output = {'H': 1, 'a': 1, 'p': 2, 'i': 1, 'n': 1, 'e': 1, 's': 2}
    assert count_chars(input_string) == expected_output


def test_count_chars_empty():
    """Tests the function with an empty string."""
    input_string = ""
    expected_output = {}
    assert count_chars(input_string) == expected_output


def test_count_chars_case_sensitivity():
    """Tests the function to ensure case sensitivity."""
    input_string = "hApPiNeSs"
    expected_output = {'h': 1, 'A': 1, 'p': 1, 'P': 1, 'i': 1, 'N': 1, 'e': 1, 'S': 1, 's': 1}
    assert count_chars(input_string) == expected_output


def test_count_chars_special_characters():
    """Tests the function with a string containing special characters."""
    input_string = "Hello, World!"
    expected_output = {'H': 1, 'e': 1, 'l': 3, 'o': 2, ',': 1, ' ': 1, 'W': 1, 'r': 1, 'd': 1, '!': 1}
    assert count_chars(input_string) == expected_output
