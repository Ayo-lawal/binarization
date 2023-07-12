import cv2

def binarize_image(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply adaptive thresholding for binarization
    binary_image = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

    return binary_image

# Read the input image
image = cv2.imread('input_image.png')

# Binarize the image
binary_image = binarize_image(image)

# Apply a series of morphological operations for noise removal
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel, iterations=2)
denoised_image = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel, iterations=2)

# Display the original, binarized, and denoised images
# cv2.imshow('Original Image', image)
# cv2.imshow('Binary Image', binary_image)
# cv2.imshow('Denoised Image', denoised_image)

cv2.imwrite('binarized_image.png', binary_image)
cv2.imwrite('denoised_image.png', denoised_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()