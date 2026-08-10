import cv2

# Read the image
img = cv2.imread(r"C:\Users\Ramya R S\Downloads\image.png")

if img is None:
    print("Error: Image could not be loaded.")
else:
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Original Image", img)
    cv2.imshow("Grayscale Image", gray)

    cv2.waitKey(0)
    cv2.destroyAllWindows()