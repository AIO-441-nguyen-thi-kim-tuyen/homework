from homework.module_1_week_3.my_stack import MyStack


def test_my_stack():
    stack1 = MyStack(capacity=5)
    stack1.push(1)
    stack1.push(2)
    assert stack1.is_full().__eq__(False)
    assert stack1.top() == 2
    assert stack1.pop() == 2
    assert stack1.top() == 1
    assert stack1.pop() == 1
    assert stack1.is_empty().__eq__(True)
