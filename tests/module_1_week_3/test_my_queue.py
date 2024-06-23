from homework.module_1_week_3.my_queue import MyQueue


def test_my_queue():
    queue1 = MyQueue(capacity=5)
    queue1.enqueue(1)
    queue1.enqueue(2)
    assert queue1.is_full().__eq__(False)
    assert queue1.front() == 1
    assert queue1.dequeue() == 1
    assert queue1.front() == 2
    assert queue1.dequeue() == 2
    assert queue1.is_empty().__eq__(True)
