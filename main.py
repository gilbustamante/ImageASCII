import sys
import os
from PIL import Image


def handle_image(filepath):
    """Main function that loads image, begins conversion, and writes to file"""
    filepath = os.path.abspath(filepath)
    try:
        image = Image.open(filepath)
    except:
        print(f"ERROR: Could not load file at path: {filepath}")
        print("Are you sure it's an image?")
        return

    # Convert image to ASCII
    final = create_image(image)

    # Write to output.txt
    write_to_file(final)


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

    return ascii_image


def resize_image(image, new_width=100):
    """Resize image while preserving aspect ratio"""
    (orig_width, orig_height) = image.size
    aspect_ratio = orig_width / orig_height
    new_height = int(aspect_ratio * new_width)
    resized_image = image.resize((new_width, new_height))

    return resized_image


def convert_greyscale(image):
    """Converts image to greyscale"""
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


def write_to_file(ascii_list):
    """Write ASCII output to text file"""
    with open('output.txt', 'w') as f:
        for line in ascii_list:
            f.write(f"{line}\n")
    print('Done')


if __name__ == '__main__':
    try:
        img_path = sys.argv[1]
    except IndexError:
        print("You need to provide an image to convert.")
        print("Syntax: python main.py <image>")
        sys.exit()
    handle_image(img_path)
