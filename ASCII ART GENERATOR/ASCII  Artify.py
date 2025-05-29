import cv2
import numpy as np
import sys

# ASCII symbols from darkest to lightest
SYMBOLS = ["@", "#", "*", "+", ":", "-", ".", " "]

def get_symbol_index(pixel_value):
    """Map pixel intensity to ASCII symbol index."""
    return int(pixel_value / (256 / len(SYMBOLS)))

def convert_to_ascii(image, scale_x=0.1, scale_y=0.05):
    """Resize image and convert to ASCII symbols."""
    height, width = image.shape
    new_width = int(width * scale_x)
    new_height = int(height * scale_y)
    resized_image = cv2.resize(image, (new_width, new_height))

    ascii_art = []
    for row in resized_image:
        ascii_row = ''.join(SYMBOLS[get_symbol_index(pixel)] for pixel in row)
        ascii_art.append(ascii_row)
    return ascii_art

def display_ascii_art(ascii_art):
    """Print ASCII art line by line."""
    for line in ascii_art:
        print(line)

def load_image(image_path):
    """Load image in grayscale mode."""
    return cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        image_path = sys.argv[1]
    else:
        print("Image path not specified. Using 'sample_image.png' by default.\n")
        image_path = "sample_image.png"

    image = load_image(image_path)

    if image is None:
        print("Error: Could not read the image. Please check the file path.")
        sys.exit(1)

    ascii_art = convert_to_ascii(image)
    display_ascii_art(ascii_art)
