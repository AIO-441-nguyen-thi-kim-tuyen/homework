import torch
import torch.nn as nn


class Softmax_Stable(nn.Module):
    def __init__(self):
        super(Softmax_Stable, self).__init__()

    def forward(self, x):
        max_val = torch.max(x)
        return torch.exp(x - max_val) / torch.sum(torch.exp(x - max_val), dim=0, keepdim=True)
