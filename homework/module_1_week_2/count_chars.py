def count_chars(s):
    count = {}
    for char in s:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return count


s = 'Happiness'
print(count_chars(s))
