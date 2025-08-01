# -*- coding: utf-8 -*-
"""ImageCaptioning_CodSoft

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/14hN4Hc-OY1itUN8MOIhEsw7jLaNZromF

# 🖼️ Task 4: Image Captioning AI  
👩‍💻 Name: Priyanka Sinha  
📅 CodSoft AI Internship – June Batch  

---

## 📝 Text-Based Explanation (No Voice Demo)

👉 This is an AI-powered image captioning project using Python and a pre-trained model.  
👉 The model takes an image as input and generates a descriptive sentence.  
👉 I’ve used Hugging Face’s `BLIP` model to simplify the task.  
👉 The model automatically understands what's in the image and explains it in words.

Below is the code, image used, and caption generated.
"""

# Install required packages (takes a minute)
!pip install transformers torchvision pillow

# Import libraries
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import requests

# Load the pre-trained model
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Load an image (sample image from the internet)
image_url = "https://images.pexels.com/photos/1043474/pexels-photo-1043474.jpeg"
image = Image.open(requests.get(image_url, stream=True).raw)

# Show the image in Colab
image.show()

# Prepare input and generate caption
inputs = processor(image, return_tensors="pt")
out = model.generate(**inputs)

# Print the caption
caption = processor.decode(out[0], skip_special_tokens=True)
print("📷 AI-generated caption:", caption)

from IPython.display import display
display(image)