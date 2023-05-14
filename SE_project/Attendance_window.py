import face_recognition
from datetime import datetime
import csv
import os
import numpy as np
from dependencies import cv2

video_capture = cv2.VideoCapture(0)

filename = 'database.csv'
known_faces_names = []
known_ids = []
known_face_encoding = []

with open(filename, 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        known_faces_names.append(row[0])
        #print(row[0])
        known_ids.append(row[1])
        known_face_encoding.append(row[3])


encodings = []
for known_encodings in known_face_encoding:
    #print(type(known_encodings))
    encodings.append(np.array(known_encodings[2:-2].split(), dtype=np.float64))


students = known_faces_names.copy()
s = True
face_encodings = []
face_locations = []

# Creating a csv file with the current date as it's name to store attendance records.
now = datetime.now()
current_date = now.strftime("%Y-%m-%d")
f = open(current_date+'.csv','w+',newline = '')
lnwriter = csv.writer(f)

 
while True:
    _,frame = video_capture.read()
    small_frame = cv2.resize(frame,(0,0),fx=0.25,fy=0.25)

    rgb_small_frame = small_frame[:,:,::-1]
    """small_frame is assumed to be a 3-dimensional NumPy array, representing an image with RGB color channels. The dimensions of the array are typically (height, width, channels). The channels dimension corresponds to the RGB color channels, in the order of red, green, and blue.
    [:,:,::-1] is the indexing and slicing notation used to select and reverse the order of the color channels. The first colon : selects all the elements along the height and width dimensions, which means the entire image is selected. The second colon : selects all the elements along the width dimension. The third ::-1 selects all the elements along the channels dimension in reverse order, which means the color channels are reversed from RGB to BGR.
    So, rgb_small_frame is a new NumPy array that has the same height and width as small_frame, but with the RGB color channels reversed to BGR. This is a common preprocessing step for images before they are used as input to some computer vision algorithms that require BGR images as input."""
    if s:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        face_names = []
        
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(encodings, face_encoding)
            print(matches)
            print("matching face encodings!!!")
            """compare_faces takes these two inputs and uses an algorithm to compare the face encoding to each of the known face encodings in the list. It returns a list of boolean values, where each value indicates whether the corresponding known face encoding in the list matches the input face encoding or not.
            So, matches is a list of boolean values, where each value corresponds to a known face encoding in known_face_encoding, and indicates whether that known face encoding matches the input face encoding in face_encoding. If the boolean value is True, it means there is a match between the two face encodings, and if it is False, there is no match."""
            name=""
            face_distance = face_recognition.face_distance(encodings, face_encoding)
            print(face_distance)
            print("Face distances!!!")
            """face_distance takes these two inputs and uses an algorithm to compute the Euclidean distance between the input face encoding and each of the known face encodings in the list. It returns a list of distances, where each distance represents the difference between the input face encoding and the corresponding known face encoding.
            face_distance can be used to identify the closest matching known face encoding to the input face encoding, and for further processing such as labeling the input face with the identity of the closest matching known face."""
            best_match_index = np.argmin(face_distance)
            
            if matches[best_match_index]:
                name = known_faces_names[best_match_index]
            print(name,"\n")
            face_names.append(name)
            if name in known_faces_names:
                font = cv2.FONT_HERSHEY_SIMPLEX
                bottomLeftCornerOfText = (10,100)
                fontScale              = 1.5
                fontColor              = (255,255,0)
                thickness              = 3
                lineType               = 2
                cv2.putText(frame, name+' Present', 
                            bottomLeftCornerOfText, 
                            font, 
                            fontScale,
                            fontColor,
                            thickness,
                            lineType)
 
                if name in students:
                    students.remove(name)
                    #print(name)
                    current_time = now.strftime("%H-%M-%S")
                    lnwriter.writerow([name,current_time])
    cv2.imshow("attendence system",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
 
video_capture.release()
cv2.destroyAllWindows()
f.close()