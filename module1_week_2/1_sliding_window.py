def sliding_window(num_list, k):
  max_values = []
  for i in range(len(num_list) - k + 1):
    window = num_list[i:i + k]
    max_values.append(max(window))
  return max_values

print(sliding_window([3, 4, 5, 1, -44 , 5 ,10, 12 ,33, 1],3))