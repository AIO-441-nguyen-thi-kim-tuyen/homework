from homework.module_1_week_3.softmax import Softmax

import torch


def test_softmax():
    data = torch.Tensor([1, 2, 3])
    softmax = Softmax()
    output = softmax(data)
    assert round(output[0].item(), 2) == 0.09
    assert round(output[1].item(), 4) == 0.2447
    assert round(output[2].item(), 4) == 0.6652

# >> tensor ([0.0900 , 0.2447 , 0.6652])
