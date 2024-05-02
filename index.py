from PIL import Image
from PIL import ImageFilter

image = Image.open("images/ada1.jpeg")

gray_image = image.convert("L")

edges = gray_image.filter(ImageFilter.FIND_EDGES)

smooth_image = edges.filter(ImageFilter.SMOOTH_MORE)

sharpen = smooth_image.filter(ImageFilter.SHARPEN)

cartoon_image = sharpen.convert("RGBA")

cartoon_image.show("images/adaBW1.png")