import cv2
import matplotlib.pyplot as plt

im = cv2.imread('cat.jpg');
# dst = cv2.medianBlur(im, 15)
# dsv = cv2.GaussianBlur(im, (5, 5), cv2.BORDER_DEFAULT)
# dsk = cv2.Canny(im, 700, 900)
dsl = cv2.bilateralFilter(im,15, 80, 80, cv2.BORDER_DEFAULT)
plt.imshow(dsl)
plt.show()