from homework.module_1_week_2.multiple_choice_question import max_kernel, character_count, count_word, \
    levenshtein_distance, check_the_number, my_function_6, my_function_7, my_function_8, my_function_9, My_function_10, \
    my_function_11, my_function_12, my_function_13, my_function_14, my_function_15, my_function_16


def test_question_1_max_kernel():
    assert max_kernel([3, 4, 5, 1, -44], 3) == [5, 5, 5]
    print(max_kernel([3, 4, 5, 1, -44], 3))
    num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
    k = 3
    print(max_kernel(num_list, k))


# Question 2
def test_question_2_character_count():
    assert character_count("Baby") == {'B': 1, 'a': 1, 'b': 1, 'y': 1}


# Question 3
def test_question_3_count_word():
    import os
    import requests
    file_path = os.path.join('.', 'P1_data.txt')
    response = requests.get("https://drive.google.com/uc?id=1IBScGdW2xlNsc9v5zSAya548kNgiOrko", stream=True)
    with open(file_path, 'wb') as output:
        output.write(response.content)
    file_path = 'P1_data.txt'
    result = count_word(file_path)
    assert result['who'] == 3
    print(result['man'])


# Question 4
def test_question_4_levenshtein_distance():
    assert levenshtein_distance("hi", "hello") == 4.0
    print(levenshtein_distance("hola", "hello"))


# Question 5
def test_question_5_check_the_number():
    N = 7
    assert check_the_number(N) == " False "
    N = 2
    results = check_the_number(N)
    print(results)


# Question 6
def test_question_6_my_function():
    my_list = [5, 2, 5, 0, 1]
    max = 1
    min = 0
    assert my_function_6(max=max, min=min, data=my_list) == [1, 1, 1, 0, 1]
    my_list = [10, 2, 5, 0, 1]
    max = 2
    min = 1
    print(my_function_6(max=max, min=min, data=my_list))


# Question 7
def test_question_7_my_function():
    list_num1 = ['a', 2, 5]
    list_num2 = [1, 1]
    list_num3 = [0, 0]

    assert my_function_7(list_num1, my_function_7(list_num2, list_num3)) == ['a', 2, 5, 1, 1, 0, 0]

    list_num1 = [1, 2]
    list_num2 = [3, 4]
    list_num3 = [0, 0]

    print(my_function_7(list_num1, my_function_7(list_num2, list_num3)))


# Question 8
def test_question_8_my_function():
    my_list = [1, 22, 93, -100]
    assert my_function_8(my_list) == -100

    my_list = [1, 2, 3, -1]
    print(my_function_8(my_list))


# Question 9
def test_question_9_my_function():
    my_list = [1001, 9, 100, 0]
    assert my_function_9(my_list) == 1001

    my_list = [1, 9, 9, 0]
    print(my_function_9(my_list))


# Question 10
def test_question_10_my_function():
    my_list = [1, 3, 9, 4]
    assert My_function_10(my_list, -1) == False

    my_list = [1, 2, 3, 4]
    print(My_function_10(my_list, 2))


# Question 11
def test_question_11_my_function():
    assert my_function_11([4, 6, 8]) == 6
    print(my_function_11())


# Question 12
def test_question_12_my_function():
    assert my_function_12([3, 9, 4, 5]) == [3, 9]
    print(my_function_12([1, 2, 3, 5, 6]))


# Question 13
def test_question_13_my_function():
    assert my_function_13(8) == 40320
    print(my_function_13(4))


# Question 14
def test_question_14_my_function():
    x = 'I can do it'
    assert my_function_14(x) == "ti od nac I"

    x = 'apricot'
    print(my_function_14(x))


# Question 15
def test_question_15_my_function():
    data = [10, 0, -10, -1]
    assert my_function_15(data) == ['T', 'N', 'N', 'N']

    data = [2, 3, 5, -1]
    print(my_function_15(data))


# Question 16
def test_question_16_my_function():
    lst = [10, 10, 9, 7, 7]
    assert my_function_16(lst) == [10, 9, 7]

    lst = [9, 9, 8, 1, 1]
    print(my_function_16(lst))
