import cv2
import mediapipe as mp


class HandTracker:

    def __init__(self):

        self.mp_hands = mp.solutions.hands
        self.mp_draw = mp.solutions.drawing_utils

        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=2,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )

    def process(self, frame):

        rgb_frame = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB
        )

        results = self.hands.process(rgb_frame)

        hands_data = []

        if results.multi_hand_landmarks:

            height, width = frame.shape[:2]

            for hand_landmarks in results.multi_hand_landmarks:

                # Draw hand landmarks
                self.mp_draw.draw_landmarks(
                    frame,
                    hand_landmarks,
                    self.mp_hands.HAND_CONNECTIONS
                )

                # Index finger tip = 8
                index_tip = hand_landmarks.landmark[8]

                # Thumb tip = 4
                thumb_tip = hand_landmarks.landmark[4]

                index_x = int(index_tip.x * width)
                index_y = int(index_tip.y * height)

                thumb_x = int(thumb_tip.x * width)
                thumb_y = int(thumb_tip.y * height)

                hands_data.append({
                    "index": (index_x, index_y),
                    "thumb": (thumb_x, thumb_y)
                })

        return frame, hands_data