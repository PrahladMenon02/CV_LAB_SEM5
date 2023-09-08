import cv2
def detect_lesions(image):
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    thresholded_image = cv2.threshold(grayscale_image, 127, 255, cv2.THRESH_BINARY)[1]

    contours, hierarchy = cv2.findContours(thresholded_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    lesions = []
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 100:
            lesions.append(contour)

    for lesion in lesions:
        cv2.fillPoly(image, [lesion], (0, 0, 255))

    return image



image = cv2.imread("img202.jpg")
detected_image = detect_lesions(image)
cv2.imshow("Detected Lesions", detected_image)
cv2.waitKey(0)
cv2.destroyAllWindows()