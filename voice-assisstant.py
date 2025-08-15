from PIL import Image
import matplotlib.pyplot as plt

image_path = "/content/download.jpg"  # your file
img = Image.open(image_path)

plt.imshow(img)
plt.axis('off')
plt.savefig("output_image.png")  # save instead of show
print("Image saved as output_image.png")
