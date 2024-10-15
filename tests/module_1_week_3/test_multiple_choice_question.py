from homework.module_1_week_3.multiple_choice_question import MySoftmax, SoftmaxStable, Student, Teacher, Doctor, Ward, \
    MyStack, MyQueue

import torch
import torch.nn as nn


# Question 1
def test_nn_softmax():
    data = torch.Tensor([1, 2, 3])
    softmax_function = nn.Softmax(dim=0)
    output = softmax_function(data)
    assert round(output[0].item(), 2) == 0.09


# Question 2
def test_my_softmax_2():
    data = torch.Tensor([5, 2, 4])
    my_softmax = MySoftmax()
    output = my_softmax(data)
    assert round(output[-1].item(), 2) == 0.26


# Question  3
def test_my_softmax_3():
    data = torch.Tensor([1, 2, 300000000])
    my_softmax = MySoftmax()
    output = my_softmax(data)
    assert round(output[0].item(), 2) == 0.0


# Question 4
def test_stable_softmax():
    data = torch.Tensor([1, 2, 3])
    softmax_stable = SoftmaxStable()
    output = softmax_stable(data)
    assert round(output[-1].item(), 2) == 0.67


# Question 5
def test_student(capfd):
    student1 = Student(name=" studentZ2023 ", yob=2011, grade="6")
    assert student1._yob == 2011
    student1.describe()
    out, err = capfd.readouterr()
    assert out.strip() == "Student:  studentZ2023 , yob: 2011, grade: 6"


# Question 6
def test_teacher(capfd):
    teacher1 = Teacher(name=" teacherZ2023 ", yob=1991, subject=" History ")
    assert teacher1._yob == 1991
    teacher1.describe()
    out, err = capfd.readouterr()
    assert out.strip() == "Teacher:  teacherZ2023 , yob: 1991, subject:  History"


# Question 7
def test_doctor(capfd):
    doctor1 = Doctor(name=" doctorZ2023 ", yob=1981, specialist=" Endocrinologists ")
    assert doctor1._yob == 1981
    doctor1.describe()
    out, err = capfd.readouterr()
    assert out.strip() == "Doctor:  doctorZ2023 , yob: 1981, specialist:  Endocrinologists"


# Question 8
def test_ward(capfd):
    student1 = Student(name=" studentA ", yob=2010, grade="7")
    teacher1 = Teacher(name=" teacherA ", yob=1969, subject=" Math ")
    teacher2 = Teacher(name=" teacherB ", yob=1995, subject=" History ")
    doctor1 = Doctor(name=" doctorA ", yob=1945, specialist=" Endocrinologists ")
    ward1 = Ward(name=" Ward1 ")
    ward1.add_person(student1)
    ward1.add_person(teacher1)
    ward1.add_person(teacher2)
    ward1.add_person(doctor1)
    assert ward1.count_doctor() == 1

    doctor2 = Doctor(name=" doctorB ", yob=1975, specialist=" Cardiologists ")
    ward1.add_person(doctor2)
    assert ward1.count_doctor() == 2


# Question 9
def test_stack_9():
    stack1 = MyStack(capacity=5)
    stack1.push(1)
    assert stack1.is_full() == False
    stack1.push(2)
    assert stack1.is_full().__eq__(False)


# Question 10
def test_stack_10():
    stack1 = MyStack(capacity=5)
    stack1.push(1)
    assert stack1.is_full().__eq__(False)
    stack1.push(2)
    assert stack1.top() == 2


# Question 11
def test_queue_11():
    queue1 = MyQueue(capacity=5)
    queue1.enqueue(1)
    assert queue1.is_full().__eq__(False)
    queue1.enqueue(2)
    assert queue1.is_full().__eq__(False)


# Question 12
def test_queue_12():
    queue1 = MyQueue(capacity=5)
    queue1.enqueue(1)
    assert queue1.is_full().__eq__(False)
    queue1.enqueue(2)
    assert queue1.front() == 1
