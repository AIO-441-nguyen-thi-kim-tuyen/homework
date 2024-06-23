from homework.module_1_week_3.softmax_stable import Softmax_Stable
import torch


def test_softmax_stable():
    data = torch.Tensor([1, 2, 3])
    softmax_stable = Softmax_Stable()
    output = softmax_stable(data)
    assert round(output[0].item(), 2) == 0.09
    assert round(output[1].item(), 4) == 0.2447
    assert round(output[2].item(), 4) == 0.6652
# >> tensor ([0.0900 , 0.2447 , 0.6652])
