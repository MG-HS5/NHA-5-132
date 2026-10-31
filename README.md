# Worker Tracking & Behavioral Analytics System

## المتطلبات الأساسية
- Python 3.8+
- تثبيت المكتبات:
  ```bash
  pip install -r requirements.txt

  تشغيل السيرفر (FastAPI):

Bash
uvicorn api:app --reload --port 8001

تشغيل تتبع الكاميرا (YOLOv8):

Bash
python main.py
عرض الأحداث المسجلة:
افتح المتصفح على: http://127.0.0.1:8001/events