# 8-bit to 16-bit image format converter

## What is a 8 bit format image?

An 8-bit format is an image format with 2^8 = 256 depth of different shades color in it. It is the most popular image format.

## What is a 16 bit formate image?

16-bit format, on other hand has an image format with 2^16 = 65535 depth of different shades of color in it. This means a 16-bit format image is supposed to have more information than an 8-bit format image.

## Why image bit format matter?

In image processing, there is a trade off between preserving detail of the bits vs the space the image takes. Training a machine learning on 16-bit image will be more computationally expensive as compared to 8-bit image, but in area where small details can’t be compromised (ie. medical x-ray images, machine defects), 16-bit image may need to be used.

Converting from 8-bit to 16-bit image won’t give the image the detail it doesn’t have in the first place, but sometimes the conversion must be done to ensure consistency with the rest of the data used for machine learning model training.

## Dependencies:

- Python - best programming language for the job
- OpenCV - library needed to load image
- NumPy - tensor operations

## Instructions

- 1. Clone the repo
- 2. Ensure all [dependencies](#dependencies) are available
- 3. In root directory, run the following command:

  ```python
  python src/convert.py -i <input_image_path> -o <output_image_path>
  ```

  Example:

  ```python
  python src/convert.py -i "example_img/dog.png" -o "example_img/dog_16_bit.png"
  ```

- 4. You will find the converted file in the output image path you specified.
