import time
import cv2
import numpy as np
import face_recognition
import os
from numpy import save
from modules import exportImages

    #find encodings of the images
def meow():
    images, names = exportImages("trials")
    print(f"Calculating encodings for the following images {names}")
    print(f"{len(images)}, {len(names)}")

    #encoding process

    encodeList = []
    for index, img in enumerate(images):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
        print(f"encoding complete for {names[index]}.png")

    print(f"Encoding complete for all images in path")

    time.sleep(5)

    print("Saving encoded list data in data.npy")
    data = encodeList
    save("data.npy", data, allow_pickle=True)

    print("data.npy overwritten")

    def saved():
        return img