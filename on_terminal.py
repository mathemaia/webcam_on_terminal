from utils.image_conversor import convert_image

import cv2


cap = cv2.VideoCapture(0)
while True:
	ret, frame = cap.read()

	print_frame(convert_image(frame, 9))
