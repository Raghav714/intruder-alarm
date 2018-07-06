# intruder-alarm
making a intruder alaram using the web-cam or CCTV camera

system play a music saying that some one had enter the cctv area. 

# library required
OpenCV 3.2.0 ,pygame 1.9.3

# Steps used to Implement the system :-
1. create background subtractor using
cv2.createBackgroundSubtractorMOG2().
2. find the change in background using standard devaition.
3. set the thresold value to play the audio.
we can change the thresold according to the need. if we need a slight
change in background to be identify then reduce the thresold or else
increase it.
