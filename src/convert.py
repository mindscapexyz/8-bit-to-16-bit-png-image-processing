import cv2
import argparse
import os
import numpy as np


def convert_image(input_path, output_path):
    if os.path.exists(input_path):
        try:
            img = cv2.imread(input_path, 1)  # Need to be sure to have a 8-bit input
            img = np.array(
                img, dtype=np.uint16
            )  # This line only change the type, not values
            img *= 256  # Now we get the good values in 16 bit format

            status = cv2.imwrite(output_path, img)
            print("Conversion succeded!")
        except Exception as e:
            print("Something going wrong:", e)
    else:
        print("File path does not exist")


if __name__ == "__main__":
    # Initialize parser
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="8-bit input image path to be converted")
    parser.add_argument("-o", "--output", help="16-bit output image path result")
    args = parser.parse_args()
    convert_image(args.input, args.output)
