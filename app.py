from edge_mask import EdgeMask as em
import cv2
path = "VIDEO/pic.jpg"

e = em(path)
img = e.edge(e.grayscale(e.read_img(path)))
e.show_img(e.read_img(path))
e.save_img(img, path + "_edge.jpg")
