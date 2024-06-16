## Test cases

# Import the function to be tested

import pytest  # Import pytest for tests
from homework.module_1_week_2.sliding_window import sliding_window


def test_sliding_window_basic():
    """Tests the sliding window function with a simple list and window size."""
    input_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
    window_size = 3
    expected_output = [5, 5, 5, 5, 10, 12, 33, 33]
    assert sliding_window(input_list, window_size) == expected_output


def test_sliding_window_empty_list():
    """Tests the function with an empty list."""
    input_list = []
    window_size = 3
    expected_output = []
    assert sliding_window(input_list, window_size) == expected_output


def test_sliding_window_large_window():
    """Tests the function with a window size larger than the list length."""
    input_list = [1, 2, 3]
    window_size = 5
    expected_output = [3]
    assert sliding_window(input_list, window_size) == expected_output


def test_sliding_window_negative_window():
    """Tests the function with a negative window size."""
    input_list = [1, 2, 3]
    window_size = -2
    with pytest.raises(ValueError):  # Expect a ValueError for negative window size
        sliding_window(input_list, window_size)


# Configure pytest-cov to track coverage for the sliding_window function
# pytest_plugins = ['pytest_cov']
# cov_source = ['homework']  # Replace with the directory containing your function

# # Run tests with coverage report (optional, adjust report type as needed)
# if __name__ == '__main__':
#     pytest.main(['-m', 'test_sliding_window', '--cov-report', 'html'])
