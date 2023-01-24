import cv2
import src.GettingImage as gi

path = r'assets\images\face-1.jpg'

# img = cv2.imread(path)
#
# cv2.imshow('Image', img)
gi.image.OpenImage(path, 'Window')
cv2.waitKey(0)
cv2.destroyAllWindows()