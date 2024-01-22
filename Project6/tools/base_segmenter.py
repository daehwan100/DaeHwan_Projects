import time
import torch
import cv2
from PIL import Image, ImageDraw, ImageOps
import numpy as np
from typing import Union
from segment_anything import sam_model_registry, SamPredictor, SamAutomaticMaskGenerator
import matplotlib.pyplot as plt
import PIL
from .mask_painter import mask_painter


class BaseSegmenter:
    def __init__(self, SAM_checkpoint, model_type, device='cuda:0'):

        print(f"Initializing BaseSegmenter to {device}")
        assert model_type in ['vit_b', 'vit_l', 'vit_h'], 'model_type must be vit_b, vit_l, or vit_h'

        self.device = device
        self.torch_dtype = torch.float16 if 'cuda' in device else torch.float32
        self.model = sam_model_registry[model_type](checkpoint=SAM_checkpoint)
        self.model.to(device=self.device)
        self.predictor = SamPredictor(self.model)
        self.embedded = False

    @torch.no_grad()
    def set_image(self, image: np.ndarray):
        self.orignal_image = image
        if self.embedded:
            print('repeat embedding, please reset_image.')
            return
        self.predictor.set_image(image)
        self.embedded = True
        return
    
    @torch.no_grad()
    def reset_image(self):
        self.predictor.reset_image()
        self.embedded = False

    def predict(self, prompts, mode, multimask=True):

        assert self.embedded, 'prediction is called before set_image (feature embedding).'
        assert mode in ['point', 'mask', 'both'], 'mode must be point, mask, or both'
        
        if mode == 'point':
            masks, scores, logits = self.predictor.predict(point_coords=prompts['point_coords'], 
                                point_labels=prompts['point_labels'], 
                                multimask_output=multimask)
        elif mode == 'mask':
            masks, scores, logits = self.predictor.predict(mask_input=prompts['mask_input'], 
                                multimask_output=multimask)
        elif mode == 'both':   # both
            masks, scores, logits = self.predictor.predict(point_coords=prompts['point_coords'], 
                                point_labels=prompts['point_labels'], 
                                mask_input=prompts['mask_input'], 
                                multimask_output=multimask)
        else:
            raise("Not implement now!")
        return masks, scores, logits


