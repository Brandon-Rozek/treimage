from argparse import ArgumentParser
from . import create, trebuchet

parser = ArgumentParser(description="Create an image out of trebuchet tiles similar to image specified")
parser.add_argument("image_path", type=str, help="The image to emulate.")
parser.add_argument("--shape", type=str, help="The trebuchet shape (A, B, C, D)")
parser.add_argument("--color", type=str, help="The RGB value specified as \"r,g,b\"")
parser.add_argument("--scale", type=int, help="The multiplicative scale for the trebuchet height and width.")
args = vars(parser.parse_args())

image_path = args['image_path']

shape = args['shape']
if shape is not None:
    shape = dict(
        a=trebuchet.A,
        b=trebuchet.B,
        c=trebuchet.C,
        d=trebuchet.D
    )[args['shape'].lower()]

color = args['color']
if color is not None:
    color = tuple(int(c) for c in args['color'].split(","))
    assert len(color) == 3

scale = args['scale']

im = create(image_path, shape, color, scale)
im.show()
