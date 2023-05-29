import arguments as a
import os
import sys
import time
import torch
import numpy as np
from PIL import Image
from diffusers import StableDiffusionControlNetPipeline, ControlNetModel
from edge_mask import EdgeMask as em
import cv2
import helper
import warnings
warnings.filterwarnings("ignore")

# args = arguments.get_args()
print(a.args)