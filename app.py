from edge_mask import EdgeMask as em

path = "VIDEO/pic.jpg"

e = em(path)
img = e.edge(e.grayscale(e.read_img(path)))
e.show_img(img)
e.save_img(img, path + "_edge.jpg")
