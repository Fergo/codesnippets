# Inverts the green channel of image files
# Useful to convert between OpenGL and DirectX normal map formats

from PIL import Image
from PIL.ImageChops import invert
import sys
import os

if len(sys.argv) < 2:
    print("Usage: normal_map_inverter.py [image1] [image2] [image3] ...")
    exit(0)

for file in sys.argv[1:]:
    new_file = f'{os.path.splitext(file)[0] + "_inverted" + os.path.splitext(file)[1]}'

    print(f'Inverting green channel from file {file} to {new_file}')

    image = Image.open(file)
    red, green, blue = image.split()
    inverted = Image.merge('RGB', (red, invert(green), blue))
    inverted.save(new_file)
