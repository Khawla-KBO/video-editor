# 🎬 Simple Video Editor (Windows 11)
A small desktop video editor built with Python.
It allows you to remove selected time intervals from an MP4 video.

## ✅ Requirements
- Python 3.8 or newer
- FFmpeg
- moviepy (Python library)

## 🔧 Installation Steps

### 1️⃣ Install Python
1. Download Python from:
   https://www.python.org/downloads/
2. During installation, IMPORTANT:
   ✔ Check **"Add Python to PATH"**
3. Finish installation.

To verify:
Open Command Prompt and run:
python --version

### 2️⃣ Install MoviePy
Open Command Prompt:
pip install moviepy

### 3️⃣ Install FFmpeg
1. Download FFmpeg from:
   https://ffmpeg.org/download.html
   (Choose Windows build)

2. Extract the ZIP file (for example to `C:\ffmpeg`)

3. Add FFmpeg to PATH:
   - Press Windows key
   - Search: **Environment Variables**
   - Click **Edit the system environment variables**
   - Click **Environment Variables**
   - Select **Path** → Click **Edit**
   - Click **New**
   - Add:
     ```
     C:\ffmpeg\bin
     ```
   - Click OK to save

4. Restart Command Prompt and verify:
ffmpeg -version

## ▶️ Run the Application

Double click on `video_editor.py`
OR 
Open Command Prompt inside that folder and Run:
python video_editor.py

The interface will open.

## 🧭 How to Use
1. Click **Browse** → Select input video.
2. Click **Add Interval**.
3. Enter times in format: HH:MM:SS (Example: 00:01:30 → 00:02:10)
4. Click **Save As**.
5. Click **Process Video**.

The new edited video will be generated.


