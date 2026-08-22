import math


class GestureDetector:

    def distance(self, point1, point2):

        return math.hypot(
            point1[0] - point2[0],
            point1[1] - point2[1]
        )

    def detect_pinch(self, hand):

        index_point = hand["index"]
        thumb_point = hand["thumb"]

        distance = self.distance(
            index_point,
            thumb_point
        )

        return distance < 50

    def detect_open_palm(self, hand):

        return hand.get("open_palm", False)