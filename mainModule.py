from Objectidentification import *
import time
from TTS import TTS

def mainModule():
    cap = cv2.VideoCapture(0)
    cap.set(3, 1920)
    cap.set(4, 1080)
    list_of_objects_detected = []
    t_end = time.time() + 60/2

    TTS("Object identification system active")
    while time.time() < t_end:
        success, img = cap.read()
        result, ObjectInfo = getObjects(img, 0.6, 0.2, True, objects = [])
        cv2.imshow("output", img)
        cv2.waitKey(1)
        for i in ObjectInfo:
            print(i[1])
            list_of_objects_detected.append(i[1])
    TTS("Processing complete")

    list_of_objects = list(set(list_of_objects_detected))

    if len(list_of_objects) == 0:
        TTS("None of the objects present are recognised")
    else:
        TTS(f" {len(list_of_objects)} objects recognised")
        TTS(f"Recognised objects are as follows")
        for index, objects in enumerate(list_of_objects):
            TTS(f"{objects}")

    cap.release()
    cv2.destroyAllWindows()



