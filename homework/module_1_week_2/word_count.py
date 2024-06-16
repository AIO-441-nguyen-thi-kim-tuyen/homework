def standardize(data):
    data = data.replace('-', ' ')
    data = data.replace(',', ' ')
    data = data.replace('.', ' ')
    data = data.lower()
    data = data.split()
    return data


def word_count(file_path):
    with open(file_path, 'r') as f:
        data = standardize(f.read())

    count = {}
    for word in data:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count

# gdown https://drive.google.com/uc?id=1IBScGdW2xlNsc9v5zSAya548kNgiOrko
# file_path = 'P1_data.txt'
# print(word_count(file_path))
