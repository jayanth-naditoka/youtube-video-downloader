# YouTube Video Downloader

This project is a simple YouTube Video Downloader built using FastAPI for the backend and a basic HTML frontend with Bootstrap for styling. The application allows users to input a YouTube video URL and download the video in the best available format.

## Features

- **FastAPI Backend**: Handles the video download process using `yt_dlp`.
- **HTML & Bootstrap Frontend**: Provides a user-friendly interface for inputting the video URL.
- **CORS Support**: Configured to allow cross-origin requests.
- **Responsive Design**: The frontend is responsive and works well on various devices.

## Installation

### Prerequisites

- Python 3.7+
- `yt-dlp` library
- `FastAPI` and `uvicorn` for the server
- `Bootstrap` for frontend styling


## Usage

1. Enter the URL of the YouTube video you want to download into the input field.
2. Click the "Download" button.
3. The backend will start downloading the video, and a message will be displayed indicating the download status.

## Project Structure

```bash
.
├── main.py                  # Main FastAPI application file
├── index.html               # HTML file for the frontend
├── style.css                # CSS file for custom styling (optional)
├── README.md                # Project documentation
├── requirements.txt         # Python dependencies
