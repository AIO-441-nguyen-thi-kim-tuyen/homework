import torch
import torch.nn as nn
from abc import ABC, abstractmethod


class MySoftmax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        return torch.exp(x) / torch.sum(torch.exp(x), dim=0, keepdim=True)


class SoftmaxStable(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        # max_val = torch.max(x)
        # return torch.exp(x - max_val) / torch.sum(torch.exp(x - max_val), dim=0, keepdim=True)

        x_max = torch.max(x, dim=0, keepdims=True)
        x_exp = torch.exp(x - x_max.values)
        partition = x_exp.sum(0, keepdims=True)
        return x_exp / partition


class Person(ABC):
    def __init__(self, name: str, yob: int):
        self._name = name
        self._yob = yob

    def get_yob(self):
        return self._yob

    @abstractmethod
    def describe(self):
        pass


class Student(Person):
    def __init__(self, name: str, yob: int, grade: str):
        super().__init__(name, yob)
        self._grade = grade

    def describe(self):
        print(f"Student: {self._name}, yob: {self._yob}, grade: {self._grade}")


class Teacher(Person):
    def __init__(self, name: str, yob: int, subject: str):
        super().__init__(name, yob)
        self._subject = subject

    def describe(self):
        print(f"Teacher: {self._name}, yob: {self._yob}, subject: {self._subject}")


class Doctor(Person):
    def __init__(self, name: str, yob: int, specialist: str):
        super().__init__(name, yob)
        self._specialist = specialist

    def describe(self):
        print(f"Doctor: {self._name}, yob: {self._yob}, specialist: {self._specialist}")


class Ward:
    def __init__(self, name: str):
        self.__name = name
        self.__listPeople = list()

    def add_person(self, person: Person):
        self.__listPeople.append(person)

    def describe(self):
        print(f" Ward Name : {self.__name}")
        for p in self.__listPeople:
            p.describe()

    def count_doctor(self):
        count = 0
        for p in self.__listPeople:
            if isinstance(p, Doctor):
                count += 1
        return count


class MyStack:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__stack = []

    def is_full(self):
        return len(self.__stack) == self.__capacity

    def push(self, value):
        if self.is_full():
            print('Do nothing!')
        else:
            self.__stack.append(value)

    def is_empty(self):
        return len(self.__stack) == 0

    def top(self):
        if self.is_empty():
            print('Do nothing!')
            return None
        else:
            return self.__stack[-1]


class MyQueue:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__queue = []

    def is_empty(self):
        return len(self.__queue) == 0

    def is_full(self):
        return len(self.__queue) == self.__capacity

    def dequeue(self):
        if self.is_empty():
            print('Do nothing!')
            return None
        else:
            return self.__queue.pop(0)

    def enqueue(self, value):
        if self.is_full():
            print('Do nothing!')
            return None
        else:
            self.__queue.append(value)

    def front(self):
        if self.is_empty():
            print('Do nothing!')
            return None
        else:
            return self.__queue[0]
