import cv2
import numpy as np

# Read the image
image_path = './image2.png'
image = cv2.imread(image_path)

# Convert it to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Canny edge detection
low_threshold = 100
high_threshold = 200
edges = cv2.Canny(gray_image, low_threshold, high_threshold)

# Display the original and edge-detected images
cv2.imshow('Original Image', image)
cv2.imshow('Edges Detected', edges)

# Wait for a key press and then destroy all image windows
cv2.waitKey(0)
cv2.destroyAllWindows()
