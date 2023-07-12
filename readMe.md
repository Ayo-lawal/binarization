# Binarize and Denoise Image

This project focuses on binarizing and denoising an input image using Python and OpenCV. It applies adaptive thresholding for binarization and a series of morphological operations for noise removal.

## Usage

1. Place your input image file in the project directory.
2. Update the file name in the script to match your input image.
3. Run the script using the following command:
   ```shell
   python binarize_denoise.py

The binarized image will be saved as binarized_image.png, and the denoised image will be saved as denoised_image.png in the project directory.
The original, binarized, and denoised images can be displayed by uncommenting the corresponding cv2.imshow() lines in the script.
Press any key to close the image windows.

## Requirements

Python 3.x
OpenCV (cv2)

## Customization

If needed, you can modify the parameters in the cv2.adaptiveThreshold() function to adjust the binarization process.
Adjust the kernel size and the number of iterations in the morphological operations (cv2.morphologyEx()) to control the denoising effect.