import yt_dlp
from fastapi import FastAPI, Form,Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates


app = FastAPI() 
 
 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or specify allowed origins like ["https://example.com"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
templates = Jinja2Templates(directory="youtubeVideoDownloader")

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/download")
def download_youtube_video(video_url: str = Form(...)):
    ydl_opts = {
        'format': 'best',
        'outtmpl': './%(title)s.%(ext)s',
    } 

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

    return {"message": "Download started!"}
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
