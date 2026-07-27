import cv2

video_path = r"C:\Users\Ramya R S\Downloads\sample.mp4.mp4"

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open the video.")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Video finished.")
        break

    cv2.imshow("Video Player", frame)

    # Press 'q' to quit
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()