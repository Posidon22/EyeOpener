import numpy as np
import matplotlib.pyplot as plt
import cv2
from PIL import Image
#from transformers import pipeline
#from accelerate import Accelerator
#import torch
#device = Accelerator().device
#checkpoint = "depth-anything/Depth-Anything-V2-base-hf"
#pipe = pipeline("depth-estimation", model=checkpoint, device=device)

test = Image.open("C:/Users/Talmid/PycharmProjects/EyeOpener/training/Images/test.jpg")
test.show()