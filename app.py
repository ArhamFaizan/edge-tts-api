from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
import edge_tts
import uuid
import os

app = FastAPI()

class TTSRequest(BaseModel):
    text: str
    voice: str = "en-US-AriaNeural"

@app.get("/")
def home():
    return {"status": "Edge TTS API Running"}

@app.post("/tts")
async def tts(req: TTSRequest):
    filename = f"{uuid.uuid4()}.mp3"

    communicate = edge_tts.Communicate(
        req.text,
        req.voice
    )

    await communicate.save(filename)

    return FileResponse(
        filename,
        media_type="audio/mpeg",
        filename="voice.mp3"
    )
