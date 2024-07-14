from homework.module_2_week_1.multiple_choice_question import (create_array_0_9,
                                                               create_array_3x3_s1, create_array_3x3_s2,
                                                               create_array_3x3_s3,
                                                               question_3, question_4, question_5, question_6,
                                                               question_7,
                                                               question_8, question_9, question_10, question_11)

import numpy as np


# Question 1
def test_question_1():
    arr = create_array_0_9()
    assert all(arr == np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))


def test_question_2():
    arr1 = create_array_3x3_s1()
    assert (arr1 == np.array([[True, True, True], [True, True, True], [True, True, True]])).all()
    arr2 = create_array_3x3_s2()
    assert (arr2 == np.array([[True, True, True], [True, True, True], [True, True, True]])).all()
    arr3 = create_array_3x3_s3()
    assert (arr3 == np.array([[True, True, True], [True, True, True], [True, True, True]])).all()


def test_question_3():
    arr = question_3()
    assert all(arr == np.array([1, 3, 5, 7, 9]))


def test_question_4():
    arr = question_4()
    assert all(arr == np.array([0, -1, 2, -1, 4, -1, 6, -1, 8, -1]))


def test_question_5():
    arr_2d = question_5()
    assert (arr_2d == [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]).all()


def test_question_6():
    arr = question_6()
    assert (arr == np.array([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]])).all()


def test_question_7():
    arr = question_7()
    assert (arr == np.array([[0, 1, 2, 3, 4, 1, 1, 1, 1, 1], [5, 6, 7, 8, 9, 1, 1, 1, 1, 1]])).all()


def test_question_8(capfd):
    question_8()
    out, err = capfd.readouterr()
    print("out: %s", out.strip())
    ss = out.strip().split("\n")
    assert ss[0] == "[1 1 1 2 2 2 3 3 3]"
    assert ss[1] == "[1 2 3 1 2 3 1 2 3]"


def test_question_9():
    index = question_9()
    assert all(index == np.array([6, 9, 10]))


def test_question_10(capfd):
    question_10()
    out, err = capfd.readouterr()
    assert out.strip() == "[6. 7. 9. 8. 9. 7. 5.]"


def test_question_11():
    arr = question_11()
    assert all(arr == np.array([6, 7, 9, 8, 9, 7, 5]))
