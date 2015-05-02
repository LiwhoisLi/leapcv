import cv2
import Leap,sys
from Leap import SwipeGesture

img = cv2.imread('lena.jpg')

class SampleListener(Leap.Listener):

    def on_connect(self,controller):

	print "Connected"
	controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);

    def on_frame(self,controller):

	frame = controller.frame()
    
    	for gesture in frame.gestures():

            if gesture.type is Leap.Gesture.TYPE_SWIPE:
	        swipe = Leap.SwipeGesture(gesture)
	        velocity = int(swipe.speed/50)
		global img
		img2 = cv2.blur(img,(velocity,velocity))
		cv2.imshow("Image",img2)
		img = img2
		cv2.waitKey(5)
		print velocity



listener = SampleListener()
controller = Leap.Controller()
controller.add_listener(listener)

print "Press Enter to quit"
try:
    sys.stdin.readline()
except KeyboardInterrupt:
    pass
finally:
    controller.remove_listener(listener)
