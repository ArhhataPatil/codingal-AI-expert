import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
img = cv2.imread('palmT.jpg')

# Convert to RGB for displaying with matplotlib
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Show the original image
plt.imshow(img_rgb)
plt.title("Original Image")
plt.show()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.imshow(gray, cmap='gray')
plt.title("Grayscale Image")
plt.show()

# Crop the image
crop = img[100:300, 200:400]
crop_rgb = cv2.cvtColor(crop, cv2.COLOR_BGR2RGB)

plt.imshow(crop_rgb)
plt.title("Cropped Region")
plt.show()

# Rotate the image by 45 degrees
(height, width) = img.shape[:2]
middle = (width // 2, height // 2)

rotation = cv2.getRotationMatrix2D(middle, 45, 1.0)
rotated_img = cv2.warpAffine(img, rotation, (width, height))

rotated_rgb = cv2.cvtColor(rotated_img, cv2.COLOR_BGR2RGB)

plt.imshow(rotated_rgb)
plt.title("Rotated Image")
plt.show()

# Increase brightness by adding 50 to all pixel values
bright_matrix = np.ones(img.shape, dtype="uint8") * 50
bright_img = cv2.add(img, bright_matrix)

bright_rgb = cv2.cvtColor(bright_img, cv2.COLOR_BGR2RGB)

plt.imshow(bright_rgb)
plt.title("Brighter Image")
plt.show()

# Save the output images
cv2.imwrite('output_images/grayscale_image.jpg', gray)
cv2.imwrite('output_images/cropped_image.jpg', crop)
cv2.imwrite('output_images/rotated_image.jpg', rotated_img)
cv2.imwrite('output_images/brighter_image.jpg', bright_img)

# In this code, I added rotating the image, making it brighter, and saving the images,
# while in the classwork I only cropped and changed the image to grayscale.
