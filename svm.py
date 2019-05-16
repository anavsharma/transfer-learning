import torch
import torch.nn as nn

class SVM(nn.Module):
    def __init__(self):
        super(SVM, self).__init__()
        self.fc = nn.Linear(1024, 1)
    
    def forward(self, x):
        h = self.fc(x)
        return h