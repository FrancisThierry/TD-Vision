import cv2 
import numpy as np 
  
# Read image. 
  # Read image.
img = cv2.imread('monimage.jpg', cv2.IMREAD_COLOR)
# Convert to grayscale. 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
  
# Blur using 3 * 3 kernel. 
gray_blurred = cv2.blur(gray, (3, 3)) 
  
# Apply Hough transform on the blurred image. 
detected_circles = cv2.HoughCircles(gray_blurred,  
                   cv2.HOUGH_GRADIENT, 1, 20, param1 = 50, 
               param2 = 30, minRadius = 1, maxRadius = 800) 
  
# Draw circles that are detected. 
if detected_circles is not None: 
  
    # Convert the circle parameters a, b and r to integers. 
    detected_circles = np.uint16(np.around(detected_circles)) 

# Extract the first circle (if any) and draw it
if detected_circles is not None:
  circles = np.round(detected_circles[0, :]).astype("int")  # Extract first circle
  x, y, radius = circles[0]
  cv2.circle(img, (x, y), radius, (0, 255, 0), 2)  # Draw only the first circle

# Display the image with the drawn circle
cv2.imshow("Detected Circle", img)
cv2.waitKey(0)
cv2.destroyAllWindows()