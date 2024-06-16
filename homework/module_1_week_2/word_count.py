def word_count(file_path):
  with open(file_path, 'r') as f:
    lines = f.read().lower().split()
  count = {}
  for word in lines:
    if word in count:
      count[word] += 1
    else:
      count[word] = 1
  return count

# gdown https://drive.google.com/uc?id=1IBScGdW2xlNsc9v5zSAya548kNgiOrko
file_path = '/Users/kimtuyen/PycharmProjects/homework/module1_week_2/P1_data.txt'
print(word_count ( file_path ))