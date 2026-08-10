import cv2

# Read the image
img = cv2.imread(r"C:\Users\Ramya R S\Downloads\sample.jpg.png")

# Check if the image is loaded
if img is None:
    print("Error: Image could not be loaded.")
else:
    print("Image loaded successfully")
    print("Image Shape:", img.shape)

    # Display the image
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()