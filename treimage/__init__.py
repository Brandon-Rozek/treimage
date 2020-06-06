"""
treimage provides functionality to take an
image and replicate it with flexible trebuchets.

Concept was inspired by OptArt by Robert Bosch.
"""
from typing import Optional, Tuple
from PIL import Image, ImageDraw
import numpy as np
from . import trebuchet

__all__ = ['trebuchet', 'create']

WHITE = (255, 255, 255)

def create(image_path: str, shape: trebuchet.FlexibleTrebuchet = trebuchet.D,
           color: Optional[Tuple[int, int, int]] = (26, 95, 138), scale: int = 2):
    """
    Creates an image out of trebuchet tiles as close to the original image as possible.
    Inspired by the OptArt book by Robert Bosch.

    Parameters
    ==========
    image_path: str
        The path of the image that we wish to emulate.
    shape: trebuchet.FlexibleTrebuchet
        The trebuchet shape to use. Options: A, B, C, D.
    color: Optional[Tuple[int, int, int]]
        A RGB tuple containing the color of the Trebuchet tile.
        If None, then we average the color of the surrounding area.
    scale: int
        The multiplicative scale of the width and height of a Trebuchet tile.
    """
    if shape is None:
        shape = trebuchet.D
    if scale is None:
        scale = 2

    with Image.open(image_path) as im:
        with Image.new('RGB', im.size, WHITE) as new_im:
            grayscale_im = im.convert(mode='L')
            draw = ImageDraw.Draw(new_im)
            width, height = im.size
            length = 4 * scale
            for x in range(0, width, length):
                for y in range(0, height, length):
                    gray_tile = grayscale_im.crop((x, y, x + length, y + length))
                    brightness = np.asarray(gray_tile).mean() / 255
                    p = shape(x, y, scale, brightness)

                    tile_color = color
                    if color is None:
                        tile = im.crop((x, y, x + length, y + length))
                        avg_color = tuple(np.asarray(tile).mean((0, 1)))
                        tile_color = tuple(int(c) for c in tuple(avg_color))

                    draw.polygon(p.points, fill=tile_color)
            return new_im
