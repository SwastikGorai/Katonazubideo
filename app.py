import helper
import torch
import numpy as np
from PIL import Image
from diffusers import StableDiffusionControlNetPipeline, ControlNetModel
from edge_mask import EdgeMask as em
import cv2
path = "VIDEO/TEST/pic.jpg"

e = em(path)
img = e.edge(e.grayscale(e.read_img(path)))
# e.show_img(e.read_img(path))
e.save_img(img, path + "_edge.jpg")
image = img[:, :, None]
image = np.concatenate([image, image, image], axis=2)
canny_image = Image.fromarray(image)
canny_image

controlnet = ControlNetModel.from_pretrained(
    "lllyasviel/sd-controlnet-canny", torch_dtype=torch.float32)
pipe = StableDiffusionControlNetPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5", controlnet=controlnet, torch_dtype=torch.float32
)


pipe = StableDiffusionControlNetPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5", controlnet=controlnet,  torch_dtype=torch.float32
)

# pipe.enable_model_cpu_offload()

# pipe.enable_xformers_memory_efficient_attention()

pipe.enable_attention_slicing()


prompt = ", best quality, extremely detailed"
prompt = [t + prompt for t in ["Sandra Oh",
                               "Kim Kardashian", "rihanna", "taylor swift"]]
generator = [torch.Generator(device="cpu").manual_seed(2)
             for i in range(len(prompt))]


output = pipe(
    prompt,
    canny_image,
    negative_prompt=[
        "monochrome, lowres, bad anatomy, worst quality, low quality, bad"] * 4,
    num_inference_steps=20,
    generator=generator,
).to("cpu")

helper.image_grid(output.images, 2, 2)
