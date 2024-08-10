from fastapi import FastAPI, Request, Form, UploadFile, File
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
import yt_dlp
import os

app = FastAPI()
templates = Jinja2Templates(directory="youtubeVideoDownloader")

# Route for the home page
@app.get("/", response_class=HTMLResponse)
@app.head("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Route to handle the form submission for downloading the video
@app.post("/download")
async def download_video(request: Request, url: str = Form(...)):
    ydl_opts = {
        'outtmpl': 'downloads/%(title)s.%(ext)s',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        video_title = ydl.prepare_filename(info_dict)
        return FileResponse(video_title, filename=os.path.basename(video_title))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
