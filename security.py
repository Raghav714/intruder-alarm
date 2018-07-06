import numpy as np
import cv2
import pygame
cap = cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorMOG2()
pygame.mixer.init()
pygame.mixer.music.load("1.mp3")
while(1):
	ret, frame = cap.read()
	fgmask = fgbg.apply(frame) 
	flag = np.std(fgmask)
	if flag>50:
		print("some one came")
		pygame.mixer.music.play()
	cv2.imshow('fgmask',frame)
	cv2.imshow('frame',fgmask)
	k = cv2.waitKey(30) & 0xff
	if k == 27:
		pygame.mixer.music.stop()
		break

cap.release()
cv2.destroyAllWindows()
