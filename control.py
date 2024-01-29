import serial 
import cv2 
import numpy as np 
cap=cv2.VideoCapture(0) 
lower_range=np.array([23,90,64]) 
upper_range=np.array([37,255,255]) 
Known_distance = 15.0 
Known_width = 4.0 
if __name__ == '__main__': 
ser = serial.Serial('/dev/ttyACM0',9600,timeout=1) 
ser.flush() 
def Focal_Length_Finder(Known_distance, real_width, width_in_rf_image): focal_length = (width_in_rf_image * Known_distance) / real_width 
return focal_length 
def obj_data(img): 
obj_width = 0 
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV) 
mask=cv2.inRange(hsv,lower_range,upper_range) 
_,mask1=cv2.threshold(mask,254,255,cv2.THRESH_BINARY) 
cnts,_=cv2.findContours(mask1,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NO NE) 
for c in cnts: 
x=600 
if cv2.contourArea(c)>x: 
x,y,w,h=cv2.boundingRect(c) 
cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2) 
obj_width = w 
return obj_width 
def Distance_finder(Focal_Length, Known_width, obj_width_in_frame): distance = (Known_width * Focal_Length)/obj_width_in_frame 
return distance 
def Speed_value(distance): 
if 10 <= distance <= 100: 
# linear mapping from [10, 65] to [70, 255]

speed = ((distance - 10) * (255 - 70) / (65 - 10)) + 70 
else: 
speed = 0 
return speed 
ref_image = cv2.imread("rf.png") 
ref_image_obj_width = obj_data(ref_image) 
Focal_length_found = Focal_Length_Finder(Known_distance, Known_width,  ref_image_obj_width) 
while True: 
ret,frame=cap.read() 
frame=cv2.resize(frame,(640,480)) 
obj_width_in_frame=obj_data(frame) 
Distance = 0 
if obj_width_in_frame != 0: 
Distance = Distance_finder(Focal_length_found, Known_width,  obj_width_in_frame) 
Speed = Speed_value(Distance) 
if 0 <= Speed <= 70: 
ser.write(b"21\n") 
if 70 <= Speed <= 85: 
ser.write(b"0\n") 
if 85 <= Speed <= 95: 
ser.write(b"1\n") 
if 95 <= Speed <= 105: 
ser.write(b"2\n") 
if 105 <= Speed <= 115: 
ser.write(b"3\n") 
if 115 <= Speed <= 125: 
ser.write(b"4\n") 
if 125 <= Speed <= 135: 
ser.write(b"5\n") 
if 135 <= Speed <= 145: 
ser.write(b"5\n") 
if 145 <= Speed <= 155: 
ser.write(b"7\n") 
if 155 <= Speed <= 165: 
ser.write(b"8\n") 
if 165 <= Speed <= 175:
ser.write(b"9\n") 
if 175 <= Speed <= 185: 
ser.write(b"10\n") 
if 185 <= Speed <= 195: 
ser.write(b"11\n") 
if 195 <= Speed <= 205: 
ser.write(b"12\n") 
if 205 <= Speed <= 215: 
ser.write(b"13\n") 
if 215 <= Speed <= 225: 
ser.write(b"14\n") 
if 225 <= Speed <= 235: 
ser.write(b"15\n") 
if 235 <= Speed <= 245: 
ser.write(b"16\n") 
if 245 <= Speed <= 255: 
ser.write(b"17\n") 
else: 
Speed = 0 
ser.write(b"20\n") 
cv2.putText(frame, f"Speed: {round(Speed,2)}", (30,  
70),cv2.FONT_HERSHEY_COMPLEX, 0.6, (255,0,0), 2) 
cv2.putText(frame, f"Distance: {round(Distance,2)} CM", (30,  
35),cv2.FONT_HERSHEY_COMPLEX, 0.6, (255,0,0), 2) 
cv2.imshow("FRAME",frame) 
if cv2.waitKey(1)&0xFF==27: 
break 
cap.release() 
cv2.destroyAllWindows() 
ser.close()
