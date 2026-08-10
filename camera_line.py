import cv2

# Open camera
cap = cv2.VideoCapture(0)

# Store points
start_point = None
end_point = None


def draw_line(event, x, y, flags, param):
    global start_point, end_point

    # Left mouse button → select starting point
    if event == cv2.EVENT_LBUTTONDOWN:
        start_point = (x, y)
        end_point = None

    # Move mouse → update ending point
    elif event == cv2.EVENT_MOUSEMOVE and start_point is not None:
        end_point = (x, y)

    # Release mouse → finish line
    elif event == cv2.EVENT_LBUTTONUP:
        end_point = (x, y)


cv2.namedWindow("Live Camera")
cv2.setMouseCallback("Live Camera", draw_line)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Draw line while selecting
    if start_point is not None and end_point is not None:
        cv2.line(
            frame,
            start_point,
            end_point,
            (0, 0, 255),
            3
        )

    cv2.imshow("Live Camera", frame)

    # Press C to clear the line
    if cv2.waitKey(1) & 0xFF == ord('c'):
        start_point = None
        end_point = None

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()