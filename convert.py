import numpy as np
import cv2
import argparse


def convert_image():
    i = cv2.imread(
        imgNameIn, cv2.CV_LOAD_IMAGE_COLOR
    )  # Need to be sure to have a 8-bit input
    img = np.array(i, dtype=np.uint16)  # This line only change the type, not values
    img *= 256  # Now we get the good values in 16 bit format


if __name__ == "__main__":
    # Initialize parser
    parser = argparse.ArgumentParser()
    parser.parse_args()