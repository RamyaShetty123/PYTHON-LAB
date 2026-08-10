import cv2 as cv

# Open the traffic video
video_path = r"C:\Users\Ramya R S\Downloads\trafficvideo.mp4"
cap = cv.VideoCapture(video_path)

# Check if video opened
if not cap.isOpened():
    print("Error: Cannot open traffic video.")
    exit()

# Create background subtractor
backSub = cv.createBackgroundSubtractorMOG2()

# Vehicle counter
vehicle_count = 0

# Counting line position
line_y = 300

# Distance tolerance
offset = 10

# Store counted vehicle centers
detected = []

while True:

    ret, frame = cap.read()

    if not ret:
        break

    # Resize frame
    frame = cv.resize(frame, (800, 600))

    # Background subtraction
    mask = backSub.apply(frame)

    # Remove shadows
    _, mask = cv.threshold(mask, 200, 255, cv.THRESH_BINARY)

    # Remove noise
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
    mask = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel)
    mask = cv.dilate(mask, kernel, iterations=2)

    # Find contours
    contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    # Draw counting line
    cv.line(frame, (0, line_y), (800, line_y), (255, 0, 0), 3)

    for cnt in contours:

        area = cv.contourArea(cnt)

        if area < 1200:
            continue

        x, y, w, h = cv.boundingRect(cnt)

        # Draw rectangle
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Center point
        cx = x + w // 2
        cy = y + h // 2

        cv.circle(frame, (cx, cy), 4, (0, 0, 255), -1)

        cv.putText(frame,
                   "Vehicle",
                   (x, y - 10),
                   cv.FONT_HERSHEY_SIMPLEX,
                   0.6,
                   (0, 255, 0),
                   2)

        # Count vehicle
        if line_y - offset < cy < line_y + offset:

            if (cx, cy) not in detected:
                detected.append((cx, cy))
                vehicle_count += 1

    # Display count
    cv.putText(frame,
               f"Vehicle Count : {vehicle_count}",
               (20, 40),
               cv.FONT_HERSHEY_SIMPLEX,
               1,
               (0, 0, 255),
               2)

    # Show windows
    cv.imshow("Traffic Video", frame)
    cv.imshow("Motion Mask", mask)

    # Press Q to quit
    if cv.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()