def sliding_window(num_list, k):
    if k < 0:
        raise ValueError("k is not negative")
    n = len(num_list)
    if n == 0:
        return []
    rg = n
    max_values = []
    if k > n:
        max_values.append(max(num_list))
        return max_values

    rg = n - k + 1

    for i in range(rg):
        window = num_list[i:i + k]
        max_values.append(max(window))
    return max_values


print(sliding_window([3, 4, 5, 1, -44, 5, 10, 12, 33, 1], 3))
