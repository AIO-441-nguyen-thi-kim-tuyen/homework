def count_chars(string):
  count = {}
  for char in string:
    if char in count:
      count[char] += 1
    else:
      count[char] = 1
  return count


string = 'Happiness'
print(count_chars ( string ))