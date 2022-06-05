import cv2

# cap = cv2.VideoCapture(0)
classNames = []
classFile = "coco.names"
with open(classFile, "rt") as f:
    classNames = f.read().rstrip("\n").split("\n")

configPath = "ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"
weightsPath = "frozen_inference_graph.pb"

net = cv2.dnn_DetectionModel(weightsPath, configPath)
net.setInputSize(320, 320)
net.setInputScale(1.0/127.5)
net.setInputMean((127.5,127.5,127.5))
net.setInputSwapRB(True)

def getObjects(img, thres, nms, draw = True, objects = []):
    classIds, confs, bbox = net.detect(img, confThreshold=thres, nmsThreshold= nms)
    ObjectInfo = []
    if len(objects) == 0: objects = classNames
    if len(classIds) != 0:
        for classId, confidence, box in zip(classIds.flatten(), confs.flatten(), bbox):
            className = classNames[classId-1]
            if className in objects:
                ObjectInfo.append([box, className])
                if (draw):
                    cv2.rectangle(img, box, color=(0,255,0), thickness=2)
                    cv2.putText(img, classNames[classId-1].upper(), (box[0]+10, box[1]+30),cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
    return img, ObjectInfo

if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)

    while True:
        success, img = cap.read()
        result, ObjectInfo = getObjects(img, 0.6,0.2,True, objects=[])
        for i in ObjectInfo:
            print(i[1])
        cv2.imshow("output", img)
        cv2.waitKey(1)

    cap.release()
    cv2.destroyAllWindows()
