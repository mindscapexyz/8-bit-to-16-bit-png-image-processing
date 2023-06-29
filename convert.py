import cv2
import argparse


def convert_image(input_path, output_path):
    img = cv2.imread(
        input_path, cv2.CV_LOAD_IMAGE_COLOR
    )  # Need to be sure to have a 8-bit input
    convert = cv2.normalize(
        img, dst=None, alpha=0, beta=65535, norm_type=cv2.NORM_MINMAX
    )

    cv2.imwrite(convert, output_path)


if __name__ == "__main__":
    # Initialize parser
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="8-bit input image path to be converted")
    parser.add_argument("-o", "--output", help="16-bit output image path result")
    args = parser.parse_args()
