"""
testing some PIL magig coding on the iPad
"""

import PIL
from PIL import ImageOps
from PIL import Image
import argparse
import glob

images = glob.glob("test_images/*.jpeg")
print(images)

# OK - let's try some PIL functions
img = Image.open(images[0])
img.show()

print("done")
