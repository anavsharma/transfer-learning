import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision.models as models
import torchvision.datasets as datasets
import torchvision.transforms as transforms

class GoogLeNetPartial(nn.Module):
    def __init__(self,
                 layer='fc6',
                 model_file=None,
                 data_parallel=False,
                 **kwargs):         
        super(GoogLeNetPartial, self).__init__()
        self.model = models.googlenet(pretrained=True)
        self.output_layer = layer
        for param in self.model.parameters():
            param.requires_grad = False
        
        num_ftrs = self.model.fc.in_features
        self.model.fc = nn.Linear(num_ftrs, 1024)
        self.input_size = 224

        features = list(self.model.children())[:17]
        # print(features)

        self.model.featExtract = nn.Sequential(*features)

    def forward(self, x):
        in_size = x.size(0)
        x = self.model.featExtract(x)
        x = x.view(in_size, -1)
        return x