import cv2
import numpy as np
import matplotlib.pyplot as plt


class EdgeMask:

    def __init__(self, path):
        self.path = path

    # Read image
    def read_img(self, p):
        img = cv2.imread(p)
        assert img is not None, "Image not found in path, check path again"
        return img

    # Show image
    def show_img(self, img):
        plt.imshow(img)
        edges = self.edge(img)
        plt.subplot(121), plt.imshow(img, cmap='gray')
        plt.title('Original Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(edges, cmap='gray')
        plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
        plt.show()

    # Save image
    def save_img(self, img, path):
        cv2.imwrite(path, img)

    # Convert image to grayscale
    def grayscale(self, img):
        return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    def edge(self, img):
        return cv2.Canny(img, 100, 200)
