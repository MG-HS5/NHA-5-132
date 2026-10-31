from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Worker Tracking API")


class EventData(BaseModel):
  worker_id: int
  action: str
  timestamp: str


events_db = []


@app.get("/")
def read_root():
  return {
      "status": "Active",
      "message": "Worker Tracking & Behavioral Analytics API is running",
  }


@app.get("/events")
def get_events():
  return {"events": events_db}


@app.post("/events")
def create_event(event: EventData):
  events_db.append(event.model_dump())
  print(f"تم استقبال وتسجيل الحدث بنجاح: {event.model_dump()}")
  return {"message": "Event recorded successfully", "event": event}