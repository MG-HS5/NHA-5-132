import cv2
from datetime import datetime
import requests
from ultralytics import YOLO

model = YOLO("yolov8n.pt")
API_URL = "http://127.0.0.1:8001/events"
cap = cv2.VideoCapture(0)

sent_workers = set()

while cap.isOpened():
  success, frame = cap.read()
  if not success:
    break

  results = model.track(frame, persist=True, classes=[0], verbose=False)
  boxes = results[0].boxes

  if boxes is not None and boxes.id is not None:
    track_ids = boxes.id.int().cpu().tolist()
    for tid in track_ids:
      if tid not in sent_workers:
        sent_workers.add(tid)
        payload = {
            "worker_id": int(tid),
            "action": "Detected",
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
        try:
          res = requests.post(API_URL, json=payload, timeout=2)
          print(f"event sent successfully{tid}،code: {res.status_code}")
        except Exception as ex:
          print(f"error: {ex}")

  annotated_frame = results[0].plot()
  cv2.imshow("Worker Tracking", annotated_frame)

  if cv2.waitKey(1) & 0xFF == ord("q"):
    break

cap.release()
cv2.destroyAllWindows()