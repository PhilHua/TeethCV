import numpy as np
from PyQt5.QtGui import QColor, QBrush, QFont, QPen
from PyQt5.QtWidgets import QGraphicsSimpleTextItem
import math


class Tooth:
    landmarks = None
    centroid = None

    landmark_size = 2
    outline_pen = QPen(QColor.fromRgb(255, 0, 0))
    point_pen = QPen(QColor.fromRgb(0, 255, 0))
    text_brush = QBrush(QColor.fromRgb(0, 0, 255))
    centroid_color = QColor.fromRgb(255, 255, 0)

    def __init__(self, landmarks):
        self.landmarks = landmarks
        self._calculate_centroid()

    def _calculate_centroid(self):
        self.centroid = np.mean(self.landmarks, axis=0)

    def sum_of_squared_distances(self, other):
        """
        Calculates sum of squared distances between this and other shape
        :param other: Other object
        :return: Sum of squared distances
        """
        assert isinstance(other, Tooth)

        return np.sum((self.landmarks - other.landmarks) ** 2)

    def align(self, other):
        """
        Uses procrustes analysis to align this shape to the other.
        :param other: Object to which this one should align. Must be at origin and unit sized.
        """
        self.move_to_origin()
        self.normalize_shape()

        x = self.landmarks[:, 0]
        y = self.landmarks[:, 1]
        w = other.landmarks[:, 0]
        z = other.landmarks[:, 1]
        top_sum = np.sum(w * y - z * x)
        bottom_sum = np.sum(w * x + z * y)
        angle = math.atan(top_sum / bottom_sum)

        rot_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                              [np.sin(angle), np.cos(angle)]])

        self.landmarks = self.landmarks.dot(rot_matrix)

    def move_to_origin(self):
        """
        Moves all landmarks so that centroid is at the origin (0,0)
        """
        self.landmarks = self.landmarks - self.centroid
        self._calculate_centroid()

    def normalize_shape(self):
        """
        Normalizes shape X so that |X| = 1.
        Uses Root Mean Squares
        """
        # Calculate vectors from origin to each landmark
        scaling_factor = self.landmarks - self.centroid
        # Square distances
        scaling_factor **= 2
        # Sum all distances
        scaling_factor = np.sum(scaling_factor)
        # Divide by number of elements and get square root
        scaling_factor = np.sqrt(scaling_factor / self.landmarks.size)

        self.landmarks *= 1 / scaling_factor

    def draw(self, scene, outline, landmarks, text):
        count = self.landmarks.shape[0]

        if outline:
            for i in range(0, count):
                scene.addLine(self.landmarks[i][0], self.landmarks[i][1], self.landmarks[(i + 1) % count][0],
                              self.landmarks[(i + 1) % count][1], pen=self.outline_pen)

        if landmarks:
            for i in range(0, count):
                scene.addEllipse(self.landmarks[i][0] - self.landmark_size, self.landmarks[i][1] - self.landmark_size,
                                 self.landmark_size * 2, self.landmark_size * 2, pen=self.point_pen)

            scene.addEllipse(self.centroid[0] - self.landmark_size, self.centroid[1] - self.landmark_size,
                             self.landmark_size * 2, self.landmark_size * 2,
                             pen=QPen(self.centroid_color), brush=QBrush(self.centroid_color))

        if text:
            for i in range(0, count):
                font = QFont("Times", 6)
                text = scene.addSimpleText(str(i), font=font)
                assert isinstance(text, QGraphicsSimpleTextItem)
                text.setPos(self.landmarks[i][0] + self.landmark_size,
                            self.landmarks[i][1] - text.boundingRect().height() / 2)
                text.setBrush(self.text_brush)