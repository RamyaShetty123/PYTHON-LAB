import cv2
import os

# ---- Load the image ----
image_path = 'car.jpeg'
image = cv2.imread(image_path)

if image is None:
    raise FileNotFoundError(
        f"Could not load '{image_path}'. "
        f"Check that the file exists in this folder: {os.getcwd()}"
    )

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# ---- Load the Haar cascade for number plates ----
# First try OpenCV's built-in cascades folder
cascade_path = os.path.join(cv2.data.haarcascades, 'haarcascade_russian_plate_number.xml')

if not os.path.isfile(cascade_path):
    raise FileNotFoundError(
        f"Cascade file not found at '{cascade_path}'. "
        f"Download 'haarcascade_russian_plate_number.xml' from the OpenCV GitHub repo "
        f"(opencv/data/haarcascades) and place it in this folder or update the path below."
    )

plate_cascade = cv2.CascadeClassifier(cascade_path)

if plate_cascade.empty():
    raise IOError(f"Failed to load cascade classifier from '{cascade_path}'")

# ---- Detect plates ----
plates = plate_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=4,
    minSize=(25, 25)
)

print(f"Detected {len(plates)} plate(s)")

# ---- Draw rectangles around detected plates ----
for (x, y, w, h) in plates:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.putText(image, "Plate", (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

# ---- Show and save result ----
cv2.imshow("Detected Plates", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("output.jpeg", image)
print("Result saved as output.jpeg")