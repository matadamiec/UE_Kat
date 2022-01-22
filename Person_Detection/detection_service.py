from datetime import datetime

import numpy as np
import cv2


def run_detection(images_to_process: []):
    if images_to_process and len(images_to_process) > 0:
        class_file = 'Config_files\classes.names'
        with open(class_file, 'rt') as f:
            class_names = f.read().rstrip('\n').split(';')

        labels_color = (0, 255, 0)

        config_prototxt = 'Config_files\MobileNetSSD_deploy.prototxt'
        config_caffemodel = 'Config_files\MobileNetSSD_deploy.caffemodel'
        required_confidence = 0.4

        # DNN - Deep Neural Network
        net = cv2.dnn.readNetFromCaffe(config_prototxt, config_caffemodel)
        for imgToProcess in images_to_process:
            processing_start = datetime.now()
            print("[INFO] Rozpoczynam przetwarzanie: " + str(processing_start))
            image = cv2.imread(imgToProcess)
            (h, w) = image.shape[:2]

            blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 0.007843, (300, 300), 127.5)

            net.setInput(blob)
            detections = net.forward()
            person_count = 0
            for i in np.arange(0, detections.shape[2]):
                confidence = detections[0, 0, i, 2]
                if confidence > required_confidence:
                    detection_index = int(detections[0, 0, i, 1])
                    box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                    (startX, startY, endX, endY) = box.astype("int")

                    if class_names[detection_index] == 'person':
                        person_count += 1
                        label = class_names[detection_index] + " " + str(round(confidence * 100, 2)) + "%"
                        print("Wykryto obiekt " + label)
                        cv2.rectangle(image, (startX, startY), (endX, endY), labels_color, 2)
                        y = startY - 15 if startY - 15 > 15 else startY + 15
                        cv2.putText(image, label, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, labels_color, 2)

            processing_end = datetime.now()
            print("[INFO] Koniec przetwarzania: " + str(processing_end))
            processing_seconds = (processing_end - processing_start)

            print("Czas przetwarzania: " + str(round(processing_seconds.total_seconds(), 3)) + "s")
            print("Liczba znalezionych obiektów: "+str(person_count))
            cv2.imshow(imgToProcess, image)
            cv2.waitKey(0)
    else:
        print("Brak zdjęć do przetworzenia")
