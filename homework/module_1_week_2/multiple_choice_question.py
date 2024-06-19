# Question 1
def max_kernel(num_list, k):
    result = []

    # Your Code Here
    for i in range(len(num_list) - k + 1):
        window = num_list[i:i + k]
        result.append(max(window))
    # End Code Here
    return result


assert max_kernel([3, 4, 5, 1, -44], 3) == [5, 5, 5]
num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3
print(max_kernel(num_list, k))


# Question 2
def character_count(word):
    character_statistic = {}

    # Your Code Here
    for char in word:
        if char in character_statistic:
            character_statistic[char] += 1
        else:
            character_statistic[char] = 1

    # End Code Here
    return character_statistic


assert character_count("Baby") == {'B': 1, 'a': 1, 'b': 1, 'y': 1}
print(character_count('smiles'))


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


# file_path = '/content/P1_data.txt'
file_path = 'P1_data.txt'
result = count_word(file_path)
assert result['who'] == 3
print(result['man'])


#  Question 4

def levenshtein_distance(token1, token2):
    # Your Code Here
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
    # End Code Here

    return distance


assert levenshtein_distance("hi", "hello") == 4.0
print(levenshtein_distance("hola", "hello"))


# Question 5
def check_the_number(N):
    list_of_numbers = []
    result = ""
    for i in range(1, 5):
        # Your code here
        # Su dung append them i vao trong list_of_number
        list_of_numbers.append(i)
        # End code here
    if N in list_of_numbers:
        results = " True "
    if N not in list_of_numbers:
        results = " False "
    return results


N = 7
assert check_the_number(N) == " False "
N = 2
results = check_the_number(N)
print(results)


# Question 6
def my_function(data, max, min):
    result = []
    for i in data:
        # Your code here
        # Neu i < min thi them min vao result
        if i < min:
            result.append(min)
        elif i > max:
            result.append(max)
        else:
            result.append(i)
    return result


my_list = [5, 2, 5, 0, 1]
max = 1
min = 0
assert my_function(max=max, min=min, data=my_list) == [1, 1, 1, 0, 1]
my_list = [10, 2, 5, 0, 1]
max = 2
min = 1
print(my_function(max=max, min=min, data=my_list))


# Question 7

def my_function(x, y):
    # Your code here
    # Su dung extend de noi y vao x
    x.extend(y)
    # End code here
    return x


list_num1 = ['a', 2, 5]
list_num2 = [1, 1]
list_num3 = [0, 0]

assert my_function(list_num1, my_function(list_num2, list_num3)) == ['a', 2, 5, 1, 1, 0, 0]

list_num1 = [1, 2]
list_num2 = [3, 4]
list_num3 = [0, 0]

print(my_function(list_num1, my_function(list_num2, list_num3)))


# Question 8
def my_function(n):
    # Your code here
    min_value = n[0]
    for num in n:
        if num < min_value:
            min_value = num
    return min_value
    # End code here


my_list = [1, 22, 93, -100]
assert my_function(my_list) == -100

my_list = [1, 2, 3, -1]
print(my_function(my_list))


# Question 9
def my_function(n):
    # Your code here
    max_value = n[0]
    for num in n:
        if num > max_value:
            max_value = num
    return max_value
    # End code here


my_list = [1001, 9, 100, 0]
assert my_function(my_list) == 1001

my_list = [1, 9, 9, 0]
print(my_function(my_list))


# Question 10
def My_function(integers, number=1):
    return any(
        # Your code here : Thuc hien duyet tung phan tu trong integers , so sanh
        # tung phan tu voi number , neu bang nhau tra ve True , khac nhau tra ve false
        # vi du: integers = [1 , 2 , 3] , number = 2 , ban se tao ra list [False , True , False ]
        [num == number for num in integers]
    )


my_list = [1, 3, 9, 4]
assert My_function(my_list, -1) == False

my_list = [1, 2, 3, 4]
print(My_function(my_list, 2))


# Question 11
def my_function(list_nums=[0, 1, 2]):
    var = 0
    for i in list_nums:
        var += i
    return var / len(
        list_nums)  # Your code here : Tra ve gia tri trung binh cua list bang cach chia var cho so luong phan tu trong list_mums


assert my_function([4, 6, 8]) == 6
print(my_function())


# Question 12
def my_function(data):
    var = []
    for i in data:
        # Your code here
        # Neu i chia het cho 3 thi them i vao list var
        if i % 3 == 0:
            var.append(i)
    # End code here
    return var


assert my_function([3, 9, 4, 5]) == [3, 9]
print(my_function([1, 2, 3, 5, 6]))


# Question 13
def my_function(y):
    var = 1
    while (y > 1):
        # Your code here
        var = var * y
        y -= 1
    # End code here
    return var


assert my_function(8) == 40320
print(my_function(4))


# Question 14
def my_function(x):
    # your code here
    return x[::-1]
    # End code here


x = 'I can do it'
assert my_function(x) == "ti od nac I"

x = 'apricot'
print(my_function(x))


# Question 15
def function_helper(x):
    # Your code here
    # Neu x >0 tra ve 'T', nguoc lai tra ve 'N'
    if x > 0:
        return 'T'
    else:
        return 'N'
    # End code here


def my_function(data):
    res = [function_helper(x) for x in data]
    return res


data = [10, 0, -10, -1]
assert my_function(data) == ['T', 'N', 'N', 'N']

data = [2, 3, 5, -1]
print(my_function(data))


# Question 16
def function_helper(x, data):
    for i in data:
        # Your code here
        # Neu x == i thi return 0
        if x == i:
            return 0
    # End code here
    return 1


def my_function(data):
    res = []
    for i in data:
        if function_helper(i, res):
            res.append(i)
    return res


lst = [10, 10, 9, 7, 7]
assert my_function(lst) == [10, 9, 7]

lst = [9, 9, 8, 1, 1]
print(my_function(lst))
