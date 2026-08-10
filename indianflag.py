import cv2
import numpy as np

# Create a blank white image
img = np.ones((360, 540, 3), dtype=np.uint8) * 255

# Draw the saffron stripe (top)
cv2.rectangle(img, (0, 0), (540, 120), (0, 140, 255), -1)

# Draw the white stripe (middle)
cv2.rectangle(img, (0, 120), (540, 240), (255, 255, 255), -1)

# Draw the green stripe (bottom)
cv2.rectangle(img, (0, 240), (540, 360), (0, 128, 0), -1)

# Draw the Ashoka Chakra (blue circle)
center = (270, 180)
cv2.circle(img, center, 40, (255, 0, 0), 2)

# Draw 24 spokes
for angle in range(0, 360, 15):
    x = int(center[0] + 40 * np.cos(np.radians(angle)))
    y = int(center[1] + 40 * np.sin(np.radians(angle)))
    cv2.line(img, center, (x, y), (255, 0, 0), 1)

# Display the flag
cv2.imshow("Indian Flag", img)

cv2.waitKey(0)
cv2.destroyAllWindows()