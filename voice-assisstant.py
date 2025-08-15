from PIL import Image

# Take image path from user
image_path = input("/content/download.jpg")

# Open the image
img = Image.open(image_path)

# Show the image
img.show()

