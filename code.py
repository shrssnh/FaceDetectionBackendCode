import cv2
import dlib
import face_recognition
import numpy as np
import json


with open('data.js', 'r') as outfile:
    js = json.load(outfile)

face = cv2.imread("image.png")
enc = face_recognition.face_encodings(face)

if(len(enc)==0):
	print("Face cannot be detected!")
	exit()
distances = []
# print(js)
for faces in range(len(js["encodes"])):
	# print(faces)
	enc2 = js["encodes"][faces]["Encoding"]
	# print(enc2)

	out = face_recognition.face_distance(np.array(enc), np.array(enc2))
		# print(enc)
	distances.extend(out)		
if(np.array(distances).min()>0.4):
	print("User Not Found")
else:
	idx = np.argmin(np.array(distances))
	# print(js[])
	print("User found is "+js["encodes"][int(idx)]["name"])
# print("--"*10+"Reading Faces"+"--"*10)
# while (len(enc)==0):
# 	ret, frame = vid.read() 
# 	enc = face_recognition.face_encodings(frame)
# 	cv2.waitKey(1)
# cv2.imwrite("detectedYash.jpg",frame)
# print("--"*10+"Face Detected"+"--"*10)
# print(len(enc))
# while True:

# 	ret, frame = vid.read() 
# 	cv2.imshow('frame',frame)
	
# 	cv2.waitKey(1)
	
# 	enc2 = face_recognition.face_encodings(frame)
# 	if((len(enc2))==0):
# 		continue

# 	out = face_recognition.face_distance(np.array(enc), np.array(enc2))
# 	print(out)