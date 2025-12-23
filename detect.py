import torch
import cv2
# image = cv2.imread('input.jpg')
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# night_vision = cv2.applyColorMap(gray, cv2.COLORMAP_JET)

model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

def detect_animal(image_path):
    image = cv2.imread(image_path)
    results = model(image)

    detections = results.pandas().xyxy[0]

    for _, row in detections.iterrows():
        if row['name'] in ['dog', 'cat'] and row['confidence'] > 0.5:
            return True, round(row['confidence'], 2)

    return False, 0
