def sliding_window(num_list, k):
  max_values = []
  for i in range(len(num_list) - k + 1):
    window = num_list[i:i + k]
    max_values.append(max(window))
  return max_values

print(sliding_window([3, 4, 5, 1, -44 , 5 ,10, 12 ,33, 1],3))

## Test cases
##  Basic functionality
def test_sliding_window_basic():
  """Tests the sliding window function with a simple list and window size."""
  input_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
  window_size = 3
  expected_output = [5, 5, -44, 5, 10, 12, 33]
  assert sliding_window(input_list, window_size) == expected_output

## Empty lists
def test_sliding_window_empty_list():
  """Tests the function with an empty list."""
  input_list = []
  window_size = 3
  expected_output = []
  assert sliding_window(input_list, window_size) == expected_output

## 
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



