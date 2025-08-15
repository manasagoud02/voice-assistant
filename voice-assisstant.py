from PIL import Image
from IPython.display import display

import matplotlib.pyplot as plt

# Take image path from user
image_path = input("Enter image path: ")

# Open the image
img = Image.open("/content/download.jpg")

# Show inline in Colab
plt.imshow(img)
plt.axis('off')
plt.show()
