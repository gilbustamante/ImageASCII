"""
Goal: Take an image as input and return an ASCII representation
1. Take image and resize it
2. Convert image to greyscale
3. Map each pixel (11 groups of 25 == 255) to an ascii character and "".join
4. Create list of "lines" based on predetermined width and "\n".join
5. Print
"""

import sys
import os
from PIL import Image


def handle_image(filepath):
    """Main function that loads image and begins conversion"""
    filepath = os.path.abspath(filepath)
    try:
        image = Image.open(filepath)
    except:
        print(f"ERROR: Could not load file at path: {filepath}")
        print("Are you sure it's an image?")
        return

    final = create_image(image)
    print(final)


def create_image(image, new_width=100):
    """Resize, map pixels, and create ASCII image"""
    # Resize image
    image = resize_image(image)

    # Convert to greyscale
    image = convert_greyscale(image)

    # Map pixels to ASCII characters
    pixel_chars = map_pixels_to_ascii(image)

    # Create ASCII 'image' by separating the characters into groups
    # of 'new_width' (100 by default) separated by a newline for printing
    ascii_image = [pixel_chars[i:i+new_width]
                   for i in range(0, len(pixel_chars), new_width)]

    return "\n".join(ascii_image)


def resize_image(image, new_width=100):
    """Resize image while preserving aspect ratio"""
    (orig_width, orig_height) = image.size
    aspect_ratio = orig_width / orig_height
    new_height = int(aspect_ratio * new_width)
    resized_image = image.resize((new_width, new_height))

    return resized_image


def convert_greyscale(image):
    """Quick helper that converts image to greyscale"""
    return image.convert('L')


def map_pixels_to_ascii(image, range=25):
    """Maps list of pixels to list of 11 ASCII characters"""
    ascii_chars = ['.', ',', ':', '?', '-', '+', '*', '%', '#', '&', '@']

    # Create list of image's pixels
    image_pixels = list(image.getdata())

    # Create one big string of ASCII chars from pixels
    pixel_chars = [ascii_chars[int(pixel/range)] for pixel in image_pixels]
    pixel_chars = "".join(pixel_chars)

    return pixel_chars


if __name__ == '__main__':
    try:
        img_path = sys.argv[1]
    except IndexError:
        print("You need to provide an image to convert.")
        print("Syntax: python main.py <image>")
        sys.exit()
    handle_image(img_path)
