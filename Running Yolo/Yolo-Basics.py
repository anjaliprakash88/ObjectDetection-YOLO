from ultralytics import YOLO
import cv2

model = YOLO('Yolo-Weights/yolov8l.pt')
results = model("Images/bike.png", show=True)
cv2.waitKey(0)