import cv2
import numpy as np
import face_recognition
import os
from numpy import save
from numpy import load


def exportImages(path):
    images = []
    names = []
    myList = os.listdir(path)

    for cl in myList:
        curImg = cv2.imread(f"{path}/{cl}")
        images.append(curImg)
        names.append(os.path.splitext(cl)[0])


    return images, names

def importData(file):
    arrays = []
    data = load(file, allow_pickle= True)
    for i in data:
        values = np.array(i)
        arrays.append(values)
    return arrays


