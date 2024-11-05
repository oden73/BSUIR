import cv2
import numpy as np

config_path = 'yolov3.cfg'
weights_path = 'yolov3.weights'
classes_path = 'coco.names'

with open(classes_path, 'r') as f:
    classes = [line.strip() for line in f.readlines()]

net = cv2.dnn.readNet(weights_path, config_path)

image_path = 'image6.jpg'
image = cv2.imread(image_path)
height, width = image.shape[:2]

blob = cv2.dnn.blobFromImage(image, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
net.setInput(blob)

layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

outputs = net.forward(output_layers)

boxes = []
confidences = []
class_ids = []

for output in outputs:
    for detection in output:
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]

        if confidence > 0.2:
            center_x = int(detection[0] * width)
            center_y = int(detection[1] * height)
            w = int(detection[2] * width)
            h = int(detection[3] * height)

            x = int(center_x - w / 2)
            y = int(center_y - h / 2)

            boxes.append([x, y, w, h])
            confidences.append(float(confidence))
            class_ids.append(class_id)

indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

for i in range(len(boxes)):
    if i in indexes:
        x, y, w, h = boxes[i]
        color = (0, 255, 0)

        cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
        cv2.putText(image, 'ball', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)


cv2.imshow("Detected Spheres", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
