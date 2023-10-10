# WisconsinAutonomous

# I convert the image to HSV color space, 
# Defined the lower and upper bounds for the red color
# Create a mask for the red color and found the countours
# Got the centers of the detected cones for each region and found the centroid. Then I divided the image vertically into two parts and connected the cones seperately. Finally, I saved the output image in answer.png.

# Some issues that faced was that it conencts the cones, but then it connects to eitehr red objects or shadows after the cones. I couldn't fix this issue. One issue that I fixed though was that it was drawing zig zags on the cones, connecting them from both sides. After splitting the picture vertically, that helped fix that issue.

# Libraries used: OpenCV and numpy