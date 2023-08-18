import cv2
image = cv2.imread('C:/Users/OSLAB/PycharmProjects/pythonProject/Coolpic.jpg')
b, g, r = (image[129, 175])
print(b)
print(g)
print(r)