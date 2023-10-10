import cv2
import numpy as np

# Load the image
image = cv2.imread("red.png")

# Convert the image to HSV color space
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define the lower and upper bounds for the red color
lower_red = np.array([0, 120, 70])
upper_red = np.array([10, 255, 255])

# Create a mask for the red color
mask = cv2.inRange(hsv_image, lower_red, upper_red)

# Find contours in the mask
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Set a threshold for contour area to filter out small contours
minimum_contour_area = 100# Get the centers of the detected cones for each region

# Get the centers of the detected cones for each region
cone_centers_left = []
cone_centers_right = []
for contour in contours:
    if cv2.contourArea(contour) > minimum_contour_area:
        # Find the centroid of the contour
        M = cv2.moments(contour)
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            # Divide the image vertically into two parts and connect cones within each part
            if cX < image.shape[1] // 2:
                cone_centers_left.append((cX, cY))
            else:
                cone_centers_right.append((cX, cY))

# Connect cones on the left side
for i in range(len(cone_centers_left) - 1):
    cv2.line(image, cone_centers_left[i], cone_centers_left[i + 1], (0, 0, 255), 2)

# Connect cones on the right side
for i in range(len(cone_centers_right) - 1):
    cv2.line(image, cone_centers_right[i], cone_centers_right[i + 1], (0, 0, 255), 2)

# Save the output image
cv2.imwrite("answer.png", image)