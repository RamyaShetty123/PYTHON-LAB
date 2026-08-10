import cv2
import numpy as np

# Create a blank white image
img = np.ones((500, 500, 3), dtype=np.uint8) * 255

# Draw horizontal lines
for i in range(0, 501, 50):
    cv2.line(img, (0, i), (500, i), (0, 0, 0), 1)

# Draw vertical lines
for j in range(0, 501, 50):
    cv2.line(img, (j, 0), (j, 500), (0, 0, 0), 1)

# Display the grid
cv2.imshow("Grid", img)

cv2.waitKey(0)
cv2.destroyAllWindows()