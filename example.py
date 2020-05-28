"""
Example script that uses treimage.
"""
from PIL import Image, ImageDraw
from treimage.trebuchet import D


CANVAS_SIZE = (640, 640)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

a = D(10, 10, 10, 0.3)
print("Size:", a.size)
print(a.points)

with Image.new('RGB', CANVAS_SIZE, WHITE) as im:
    draw = ImageDraw.Draw(im)
    draw.polygon(a.points, fill=RED)
    im.show()
