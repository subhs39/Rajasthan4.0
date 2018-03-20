#computer vision Wrapper for Python
import cv2
import numpy as np
from urllib.request import urlopen
#for controlling mouse movements
import pyautogui



def stage_order(ordinates):
	global flag
	global stage_num
	print("102")
	x, y = ordinates
	print(x, y)
	if x in range(225,411) and y in range(28,200):
		print("messi")
		if flag == False:
			print("ronaldo")
			flag = True
			# print("102.5")
			pyautogui.click(600,200)
			# print("103")
			stage_num = stage_num + 1
	elif x in range(241,369) and y in range(271,402):
		if flag == False:
			flag = True
			pyautogui.click(600,500)
			stage_num = 1
	elif x in range(509,612) and y in range(7,114):
		if flag == False:
			flag = True
			pyautogui.click(905,219)
			stage_num = 1	
	else:
		if flag == True:
			flag = False
def stage_language(ordinates):
	global flag
	global stage_num
	x, y = ordinates
	if x in range(38,117) and y in range(89,228):
		if flag == False:
			flag = True
			pyautogui.click(400,300)
			stage_num = stage_num + 1
	elif x in range(445,581) and y in range(86,225):
		if flag == False:
			flag = True
			pyautogui.click(900,300)
			stage_num = stage_num + 2
	else:
		if flag == True:
			flag = False	
def stage_eng(ordinates):
	global flag
	global stage_num
	x, y = ordinates
	if x in range(18,175) and y in range(219,372):
		if flag == False:
			flag = True
			pyautogui.click(400,400)
			stage_num = stage_num + 0.3
	elif x in range(460,611) and y in range(230,375):
		if flag == False:
			flag = True
			pyautogui.click(900,450)
			stage_num = stage_num + 0.7
	else:
		if flag == True:
			flag = False
def stage_eng_veg(ordinates):
	global flag
	global stage_num
	x, y = ordinates
	if x in range(10,112) and y in range(216,321):
		if flag == False:
			flag = True
			pyautogui.click(400,400)
			stage_num = 1
	elif x in range(263,366) and y in range(322,484):
		if flag == False:
			flag = True
			pyautogui.click(650,500)
			stage_num = 1
	elif x in range(507,607) and y in range(216,316):
		if flag == False:
			flag = True
			pyautogui.click(900,400)
			stage_num = 1
	else:
		if flag == True:
			flag = False
def stage_eng_nveg(ordinates):
	global flag
	global stage_num
	x, y = ordinates
	if x in range(13,137) and y in range(190,313):
		if flag == False:
			flag = True
			pyautogui.click(400,400)
			stage_num = 1
	elif x in range(214,344) and y in range(311,437):
		if flag == False:
			flag = True
			pyautogui.click(650,500)
			stage_num = 1
	elif x in range(472,595) and y in range(209,534):
		if flag == False:
			flag = True
			pyautogui.click(900,400)
			stage_num = 1
	else:
		if flag == True:
			flag = False
def stage_hind(ordinates):
	global flag
	global stage_num
	x, y = ordinates
	if x in range(25,179) and y in range(256,407):
		if flag == False:
			flag = True
			pyautogui.click(400,500)
			stage_num = stage_num + 0.3
	elif x in range(461,620) and y in range(253,542):
		if flag == False:
			flag = True
			pyautogui.click(900,450)
			stage_num = stage_num + 0.7
	else:
		if flag == True:
			flag = False
def stage_hind_veg(ordinates):
	global flag
	global stage_num
	x, y = ordinates
	if x in range(24,174) and y in range(206,358):
		if flag == False:
			flag = True
			pyautogui.click(400,400)
			stage_num = 1
	elif x in range(260,410) and y in range(321,468):
		if flag == False:
			flag = True
			pyautogui.click(650,500)
			stage_num = 1
	elif x in range(490,434) and y in range(207,347):
		if flag == False:
			flag = True
			pyautogui.click(900,400)
			stage_num = 1
	else:
		if flag == True:
			flag = False
def stage_hind_nveg(ordinates):
	global flag
	global stage_num
	x, y = ordinates
	if x in range(23,167) and y in range(195,337):
		if flag == False:
			flag = True
			pyautogui.click(400,400)
			stage_num = 1
	elif x in range(262,394) and y in range(338,471):
		if flag == False:
			flag = True
			pyautogui.click(650,550)
			stage_num = 1
	elif x in range(502,643) and y in range(200,340):
		if flag == False:
			flag = True
			pyautogui.click(900,400)
			stage_num = 1
	else:
		if flag == True:
			flag = False


# cap = cv2.VideoCapture(0)
url='http://192.168.43.1:8080/shot.jpg'
flag = False
stage_num = 1

stage = {'1':stage_order,'2':stage_language,'3':stage_eng,
'3.3':stage_eng_veg,'3.7':stage_eng_nveg,'4':stage_hind,'4.3':stage_hind_veg,'4.7':stage_hind_nveg}

def define_stages(ordinates):
	global stage_num
	# print("101")
	stage[str(stage_num)](ordinates)


while True:
	# Recording Frames from my MotoG4
	imgResp = urlopen(url)
	imgNp = np.array(bytearray(imgResp.read()),dtype=np.uint8)
	frame = cv2.imdecode(imgNp,-1)
	# print(frame.shape)
	# cv2.imwrite("messi.jpg", frame)

	point_1 = np.array([[189,59],[314,59],[187,181],[316,181]],dtype=np.float32)
	point_2 = np.array([[0,0],[640,0],[0,480],[640,480]],dtype=np.float32)
	
	#Affine Transform !

	mask = cv2.getPerspectiveTransform(point_1, point_2)

	frame = cv2.warpPerspective(frame,mask,(640,480))

	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	lower_val = np.array([100,150,100])
	higher_val = np.array([140,255,255])

	mask = cv2.inRange(hsv, lower_val, higher_val)

	blur = cv2.medianBlur(mask,5)
	blur = cv2.blur(blur,(5,5))

	_, contours, hierarchy = cv2.findContours(blur, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	# cv2.rectangle(frame, (630-363,520-169), (730-363,620-169), (0,0,255), 2)
	cv2.rectangle(frame, (578-356,193-160), (763-356,360-160), (0,0,255), 2)

	try:
		cnt = contours[0]
		M = cv2.moments(cnt)
		cx = int(M['m10']/M['m00'])
		cy = int(M['m01']/M['m00'])
		#print(cx, cy)
		(x,y),radius = cv2.minEnclosingCircle(cnt)
		center = (int(x),int(y))
		radius = int(radius)
		#print("center co-ordinates are",int(x),int(y))
		img = cv2.circle(frame,center,radius,(0,255,0),2)
		cv2.drawContours(frame, contours, 0, (0,255), 3)
		# print("100")
		define_stages(center)
		# print(center)
		# print(M)
	except Exception as e:
		pass
		#print(e)
		#print("no contours !")

	result = cv2.bitwise_and(frame, frame, mask = blur)
	print(stage_num)

	# cv2.namedWindow('frame',cv2.WINDOW_NORMAL)
	# cv2.resizeWindow('frame', 800,600)
	cv2.imshow("frame", frame)
	# cv2.imshow("mask", mask)
	# cv2.imshow("result", result)
	# cv2.imshow("blurred", blur)

	k = cv2.waitKey(15) & 0xFF
	if k==ord('q'):
		break
cv2.destroyAllWindows()
# cap.release()