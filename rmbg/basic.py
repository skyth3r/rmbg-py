from rembg import remove
from PIL import Image

input = Image.open("input.jpg")
output = remove(input)
output.save("output.png", "PNG")