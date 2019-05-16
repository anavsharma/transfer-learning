# CMPE 275 Project: Transfer Learning for images
Using pretrained models for feature generation and using it to classify images of ants and bees from: https://download.pytorch.org/tutorial/hymenoptera_data.zip

Extract the data from the zip file in the root folder or modify line 23 in main.py to point to the data directory.

Added functions for googlenet to the tutorial from: https://github.com/pytorch/tutorials/blob/master/beginner_source/finetuning_torchvision_models_tutorial.py

Models Used:

### AlexNet, GoogLeNet (Inception-v1), Inception (Inception-v3)

----
## Install dependencies:
This code runs on python 3. 

Please change the commands to python3 instead of python and pip3 instead of pip if needed.

1. The vision module, torchvision needs to be built from source:
```bash
    git clone https://github.com/pytorch/vision.git
    cd vision
    python setup.py install
```
2. Use pip to install PyTorch
```bash
    pip install torch
```

3. use pip to install Matplotlib
```bash
    pip install matplotlib
```

----
## Running the code:
There are 2 command line arguments used:

    model_name

    feature_extract

1. Required:

    -m

    --model-name

    Type: string
    
    Description: One of the following: alexnet, googlenet, inception.

2. Optional:

    -f

    --feature-extract

    Type: boolean

    Description: Use a pretrained model for feature extraction only. Defaults to False.

```bash
    python main.py -m alexnet
```
----
## Sources & Citations:
Finetuning Torchvision models: https://pytorch.org/tutorials/beginner/finetuning_torchvision_models_tutorial.html

Transfer Learning Tutorial: https://github.com/pytorch/tutorials/blob/master/beginner_source/finetuning_torchvision_models_tutorial.py

Feature Extraction for VideoSummarization: https://github.com/anavsharma/video-analysis/blob/master/generate_features.py