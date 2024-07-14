import numpy as np


# Question 1
def create_array_0_9():
    arr = np.arange(0, 10, 1)
    print(arr)
    return arr


# Question 2
def create_array_3x3_s1():
    arr = np.ones((3, 3)) > 0
    print(arr)
    return arr


def create_array_3x3_s2():
    arr = np.ones((3, 3), dtype=bool)
    print(arr)
    return arr


def create_array_3x3_s3():
    arr = np.full((3, 3), fill_value=True, dtype=bool)
    print(arr)
    return arr


# Question 3
def question_3():
    arr = np.arange(0, 10)
    print(arr[arr % 2 == 1])
    return arr[arr % 2 == 1]


#  Question 4
def question_4():
    arr = np.arange(0, 10)
    arr[arr % 2 == 1] = -1
    print(arr)
    return arr


# Question 5
def question_5():
    arr = np.arange(10)
    arr_2d = arr.reshape(2, -1)
    print(arr_2d)
    return arr_2d


# Question 6
def question_6():
    arr1 = np.arange(10).reshape(2, -1)
    arr2 = np.repeat(1, 10).reshape(2, -1)
    c = np.concatenate([arr1, arr2], axis=0)
    print(" Result : \n", c)
    return c


# Question 7

def question_7():
    arr1 = np.arange(10).reshape(2, -1)
    arr2 = np.repeat(1, 10).reshape(2, -1)
    c = np.concatenate([arr1, arr2], axis=1)
    print("C = ", c)
    return c


# Question 8
def question_8():
    arr = np.array([1, 2, 3])
    print(np.repeat(arr, 3))
    print(np.tile(arr, 3))


# Question 9
def question_9():
    a = np.array([2, 6, 1, 9, 10, 3, 27])
    index = np.where((a >= 5) & (a <= 10))
    print(" result ", a[index])
    return a[index]


# Question 10
def question_10():
    def maxx(x, y):
        if x >= y:
            return x
        else:
            return y

    a = np.array([5, 7, 9, 8, 6, 4, 5])
    b = np.array([6, 3, 4, 8, 9, 7, 1])

    pair_max = np.vectorize(maxx, otypes=[float])
    print(pair_max(a, b))
    # return pair_max(a, b)


# Question 11
def question_11():
    a = np.array([5, 7, 9, 8, 6, 4, 5])
    b = np.array([6, 3, 4, 8, 9, 7, 1])

    print(" Result ", np.where(a < b, b, a))
    return np.where(a < b, b, a)