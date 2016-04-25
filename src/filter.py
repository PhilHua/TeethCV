import cv2
import numpy as np

from src.utils import Rectangle


class Filter:
    @staticmethod
    def _scharr(image):
        grad_x = cv2.Scharr(image, cv2.CV_64F, 1, 0) / 16
        grad_y = cv2.Scharr(image, cv2.CV_64F, 0, 1) / 16
        grad = np.sqrt(grad_x ** 2 + grad_y ** 2)
        return grad

    @staticmethod
    def get_cropping_region(image):
        h, w = image.shape
        h2, w2 = h/2, w/2
        return Rectangle(w2 - 400, 500, w2 + 400, 1400)

    @staticmethod
    def crop_image(image):
        region = Filter.get_cropping_region(image)
        return image[region.top:region.bottom, region.left:region.right].copy()

    @staticmethod
    def process_image(image):
        image = cv2.medianBlur(image, 5)
        image = cv2.bilateralFilter(image, 17, 9, 200)
        image = Filter._scharr(image)
        return image