import yt_dlp
from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or specify allowed origins like ["https://example.com"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/download")
def download_youtube_video(video_url: str = Form(...)):
    ydl_opts = {
        'format': 'best',
        'outtmpl': './%(title)s.%(ext)s',
    } 

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

    return {"message": "Download started!"}
