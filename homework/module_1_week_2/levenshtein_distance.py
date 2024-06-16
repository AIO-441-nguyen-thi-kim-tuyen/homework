def levenshtein_distance(source, target):
  if not source:
    return len(target)
  if not target:
    return len(source)

  # Create a matrix to store the distances between prefixes.
  distances = [[0 for _ in range(len(target) + 1)] for _ in range(len(source) + 1)]

  # Initialize the first row and column of the matrix.
  for i in range(len(source) + 1):
    distances[i][0] = i
  for j in range(len(target) + 1):
    distances[0][j] = j

  # Fill in the rest of the matrix.
  for i in range(1, len(source) + 1):
    for j in range(1, len(target) + 1):
      if source[i - 1] == target[j - 1]:
        cost = 0
      else:
        cost = 1
      distances[i][j] = min(
          distances[i - 1][j] + 1,  # deletion
          distances[i][j - 1] + 1,  # insertion
          distances[i - 1][j - 1] + cost  # substitution
      )

  # The last element of the matrix is the Levenshtein distance.
  return distances[len(source)][len(target)]


source = 'yu'
target = 'you'
distance = levenshtein_distance(source, target)
print(f'The Levenshtein distance between "{source}" and "{target}" is {distance}')


source = 'kitten'
target = 'sitting'
distance = levenshtein_distance(source, target)
print(f'The Levenshtein distance between "{source}" and "{target}" is {distance}')