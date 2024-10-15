class MyStack:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__stack = []

    def is_empty(self):
        return len(self.__stack) == 0

    def is_full(self):
        return len(self.__stack) == self.__capacity

    def pop(self):
        if self.is_empty():
            print('Do nothing!')
            return None
        else:
            return self.__stack.pop()

    def push(self, value):
        if self.is_full():
            print('Do nothing!')
        else:
            self.__stack.append(value)

    def top(self):
        if self.is_empty():
            print('Do nothing!')
            return None
        else:
            return self.__stack[-1]
