# Question 1
def max_kernel(num_list, k):
    result = []

    for i in range(len(num_list) - k + 1):
        window = num_list[i:i + k]
        result.append(max(window))
    return result


# Question 2
def character_count(word):
    character_statistic = {}

    for char in word:
        if char in character_statistic:
            character_statistic[char] += 1
        else:
            character_statistic[char] = 1

    return character_statistic


# Question 3
# !gdown https://drive.google.com/uc?id=1IBScGdW2xlNsc9v5zSAya548kNgiOrko
def count_word(file_path):
    counter = {}

    # Your Code Here
    with open(file_path, 'r') as f:
        data = f.read().lower().split()
    for word in data:
        if word in counter:
            counter[word] += 1
        else:
            counter[word] = 1
    # End Code Here

    return counter


#  Question 4

def levenshtein_distance(token1, token2):
    if not token1:
        return len(token2)
    if not token2:
        return len(token1)

    # Create a matrix to store the distances between prefixes.
    distances = [[0 for _ in range(len(token2) + 1)] for _ in range(len(token1) + 1)]

    # Initialize the first row and column of the matrix.
    for i in range(len(token1) + 1):
        distances[i][0] = i
    for j in range(len(token2) + 1):
        distances[0][j] = j

    # Fill in the rest of the matrix.
    for i in range(1, len(token1) + 1):
        for j in range(1, len(token2) + 1):
            if token1[i - 1] == token2[j - 1]:
                cost = 0
            else:
                cost = 1
            distances[i][j] = min(
                distances[i - 1][j] + 1,  # deletion
                distances[i][j - 1] + 1,  # insertion
                distances[i - 1][j - 1] + cost  # substitution
            )

    # The last element of the matrix is the Levenshtein distance.
    distance = distances[len(token1)][len(token2)]

    return distance


# Question 5
def check_the_number(N):
    list_of_numbers = []
    result = ""
    for i in range(1, 5):
        # Su dung append them i vao trong list_of_number
        list_of_numbers.append(i)
    if N in list_of_numbers:
        results = " True "
    if N not in list_of_numbers:
        results = " False "
    return results


# Question 6
def my_function_6(data, max, min):
    result = []
    for i in data:
        # Neu i < min thi them min vao result
        if i < min:
            result.append(min)
        elif i > max:
            result.append(max)
        else:
            result.append(i)
    return result


# Question 7

def my_function_7(x, y):
    # Su dung extend de noi y vao x
    x.extend(y)
    return x


# Question 8
def my_function_8(n):
    min_value = n[0]
    for num in n:
        if num < min_value:
            min_value = num
    return min_value


# Question 9
def my_function_9(n):
    max_value = n[0]
    for num in n:
        if num > max_value:
            max_value = num
    return max_value


# Question 10
def My_function_10(integers, number=1):
    return any(
        # Your code here : Thuc hien duyet tung phan tu trong integers , so sanh
        # tung phan tu voi number , neu bang nhau tra ve True , khac nhau tra ve false
        # vi du: integers = [1 , 2 , 3] , number = 2 , ban se tao ra list [False , True , False ]
        [num == number for num in integers]
    )


# Question 11
def my_function_11(list_nums=[0, 1, 2]):
    var = 0
    for i in list_nums:
        var += i
    return var / len(
        list_nums)  # Your code here : Tra ve gia tri trung binh cua list bang cach chia var cho so luong phan tu trong list_mums


# Question 12
def my_function_12(data):
    var = []
    for i in data:
        # Neu i chia het cho 3 thi them i vao list var
        if i % 3 == 0:
            var.append(i)
    return var


# Question 13
def my_function_13(y):
    var = 1
    while (y > 1):
        var = var * y
        y -= 1
    return var


# Question 14
def my_function_14(x):
    return x[::-1]


# Question 15
def function_helper_15(x):
    # Neu x >0 tra ve 'T', nguoc lai tra ve 'N'
    if x > 0:
        return 'T'
    else:
        return 'N'


def my_function_15(data):
    res = [function_helper_15(x) for x in data]
    return res


# Question 16
def function_helper_16(x, data):
    for i in data:
        # Neu x == i thi return 0
        if x == i:
            return 0
    return 1


def my_function_16(data):
    res = []
    for i in data:
        if function_helper_16(i, res):
            res.append(i)
    return res
