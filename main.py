import cv2
import math

from modules.camera import Camera
from modules.hand_tracking import HandTracker
from effects.invisibility import InvisibilityEffect


camera = Camera()
tracker = HandTracker()
invisibility = InvisibilityEffect()

background_captured = False


while True:

    frame = camera.read()

    if frame is None:
        print("Camera open nahi ho raha!")
        break

    # Hand tracking
    frame, hands_data = tracker.process(frame)

    # Background message
    if not background_captured:

        cv2.putText(
            frame,
            "Press B to capture background",
            (30, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 255),
            2
        )

    # Portal + pinch control
    if background_captured and len(hands_data) > 0:

        hand = hands_data[0]

        index_point = hand["index"]
        thumb_point = hand["thumb"]

        # Portal position
        center = index_point

        # Distance between thumb and index finger
        distance = math.hypot(
            index_point[0] - thumb_point[0],
            index_point[1] - thumb_point[1]
        )

        # Convert finger distance to portal radius
        radius = int(distance * 1.5)

        # Minimum and maximum size
        radius = max(50, min(radius, 250))

        # Apply invisibility effect
        frame = invisibility.apply(
            frame,
            center,
            radius=radius
        )

        # Show pinch distance
        cv2.putText(
            frame,
            f"Portal Size: {radius}",
            (30, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 255),
            2
        )

    cv2.imshow(
        "Magic Mirror AI - Phase 4",
        frame
    )

    key = cv2.waitKey(1) & 0xFF

    # Capture background
    if key == ord("b"):

        invisibility.capture_background(frame)

        background_captured = True

        print("Background captured!")

    # Exit
    if key == ord("q"):
        break


camera.release()
cv2.destroyAllWindows()