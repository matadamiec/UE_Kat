from datetime import datetime

import numpy as np
import cv2

classFile = 'Config_files\classes.names'
with open(classFile, 'rt') as f:
    classNames = f.read().rstrip('\n').split(';')

labelsColor = (0, 255, 0)

configPrototxt = 'Config_files\MobileNetSSD_deploy.prototxt'
configCaffemodel = 'Config_files\MobileNetSSD_deploy.caffemodel'
imagesToProcess = ['Samples\sample1.jpeg', 'Samples\sample2.jpeg', 'Samples\sample3.jpeg', 'Samples\sample4.jpeg']

requiredConfidence = 0.4

# DNN - Deep Neural Network
net = cv2.dnn.readNetFromCaffe(configPrototxt, configCaffemodel)
for imgToProcess in imagesToProcess:
    processingStart = datetime.now()
    print("[INFO] Rozpoczynam przetwarzanie: " + str(processingStart))
    image = cv2.imread(imgToProcess)
    (h, w) = image.shape[:2]

    blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 0.007843, (300, 300), 127.5)

    net.setInput(blob)
    detections = net.forward()

    for i in np.arange(0, detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > requiredConfidence:
            detection_index = int(detections[0, 0, i, 1])
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")

            if classNames[detection_index] == 'person':
                label = classNames[detection_index] + " " + str(round(confidence * 100, 2)) + "%"
                print("Wykryto obiekt " + label)
                cv2.rectangle(image, (startX, startY), (endX, endY), labelsColor, 2)
                y = startY - 15 if startY - 15 > 15 else startY + 15
                cv2.putText(image, label, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, labelsColor, 2)

    processingEnd = datetime.now()
    print("[INFO] Koniec przetwarzania: " + str(processingEnd))
    processingSeconds = (processingEnd - processingStart)

    print("Czas przetwarzania: " + str(round(processingSeconds.total_seconds(), 3)) + "s")
    cv2.imshow(imgToProcess, image)
    cv2.waitKey(0)
