import cv2

image1 =cv2.imread('goku.jpg')
image2 =cv2.imread('background1.jpeg')
image3 =cv2.imread('background2.jpeg')
image4 =cv2.imread('background3.jpeg')
image5 =cv2.imread('background4.jpeg')
image6 =cv2.imread('background5.jpeg')
image7 =cv2.imread('background6.jpeg')
image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))
image3 = cv2.resize(image3, (image1.shape[1], image1.shape[0]))
image4 = cv2.resize(image4, (image1.shape[1], image1.shape[0]))
image5 = cv2.resize(image5, (image1.shape[1], image1.shape[0]))
image6 = cv2.resize(image6, (image1.shape[1], image1.shape[0]))
image7 = cv2.resize(image7, (image1.shape[1], image1.shape[0]))
added_image = image1 + image2 + image3 + image4 + image5 + image6 + image7
blended_image1 = cv2.addWeighted(image1, 0.3, image2, 0.6,  gamma=0.5)

cv2.imshow("Added Image", added_image)
cv2.imshow("Blendedage1", blended_image1)
cv2.waitKey(0)


