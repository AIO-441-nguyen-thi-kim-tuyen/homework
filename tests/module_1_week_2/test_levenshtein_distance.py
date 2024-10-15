from homework.module_1_week_2.levenshtein_distance import levenshtein_distance


def test_levenshtein_distance_basic():
    """Tests the function with simple string pairs."""
    test_cases = [
        ("yu", "you", 1),
        ("kitten", "sitting", 3),
        ("", "hello", 5),
        ("hello", "", 5),
    ]

    for source, target, expected_distance in test_cases:
        distance = levenshtein_distance(source, target)
        assert distance == expected_distance


def test_levenshtein_distance_empty_strings():
    """Tests the function with empty strings."""
    assert levenshtein_distance("", "") == 0


def test_levenshtein_distance_single_char_difference():
    """Tests the function with strings differing by one character."""
    assert levenshtein_distance("cat", "cot") == 1
    assert levenshtein_distance("walk", "talk") == 1


def test_levenshtein_distance_insertion_deletion():
    """Tests the function with insertion and deletion edits."""
    assert levenshtein_distance("sleep", "slept") == 2  # Deletion  & Insertion


def test_levenshtein_distance_larger_strings():
    """Tests the function with longer strings (optional)."""
    source = "algorithm"
    target = "algorithmic"
    expected_distance = 2
    assert levenshtein_distance(source, target) == expected_distance
