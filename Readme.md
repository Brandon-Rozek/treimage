# Treimage

A library to emulate an image out of trebuchets.

## Terminal Usage

```bash
python -m treimage ~/Pictures/profile.png
```

| Flag          | Description                                                  |
| ------------- | ------------------------------------------------------------ |
| -h, --help    | Show this help message and exit.                             |
| --shape SHAPE | The trebuchet shape (A, B, C, D)                             |
| --color COLOR | The RGB value specified as "r,g,b"                           |
| --scale SCALE | The multiplicative scale for the trebuchet height and width. |


## Code Usage

```python
import treimage

image_path = '/home/brandon/Pictures/profile.png'
im = treimage.create(image_path)
im.show()
```

Parameters
```
image_path: str
    The path of the image that we wish to emulate.
```
```
shape: treimagetrebuchet.FlexibleTrebuchet
    Default: treimage.trebuchet.D
    The trebuchet shape to use. Options: A, B, C, D.
```
```
color: Optional[Tuple[int, int, int]]
    Default: (26, 95, 138)
    A RGB tuple containing 
    the color of the Trebuchet tile.
    If None, then we average 
    the color of the surrounding area.
```
```
scale: int
    Default: 2
    The multiplicative scale of 
    the width and height ofa Trebuchet tile.
```
