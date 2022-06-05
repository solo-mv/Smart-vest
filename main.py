import numpy as np
from modules import exportImages
from modules import importData
import cv2
import face_recognition
from TTS import TTS
import time

def main():
    t_end = time.time() + 60/2


    images, names = exportImages("./trials")
    encodeListKnown = importData("./data.npy")
    cap = cv2.VideoCapture(0)
    list_of_people_present = []
    while time.time() < t_end:
        success, img = cap.read()
        imgS = cv2.resize(img, (0,0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS,facesCurFrame )

        for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
            print(faceDis)
            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                name =  names[matchIndex].upper()
                print(name)
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
                cv2.rectangle(img, (x1, y1,), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(img, (x1, y2-35), (x2, y2), (0,255,0), cv2.FILLED)
                cv2.putText(img, name, (x1+6, y2-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                list_of_people_present.append(name)
        cv2.imshow('Webcam', img)
        cv2.waitKey(1)

    TTS("loop ended, awaiting results")
    list_of_people = list(set(list_of_people_present))
    if len(list_of_people) == 0:
        TTS("0 people recognized")
    else:
        if len(list_of_people) == 1:
            TTS(f"{len(list_of_people)} person recognized")
        else:
            TTS(f"{len(list_of_people)} people recognized")
        TTS("recognized people are as follows")
        for index, lists in enumerate(list_of_people):
            TTS(f"{index+1} {lists}")

    cap.release()
    cv2.destroyAllWindows()


