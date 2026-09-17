![alt text](images/banner.png)
# YouTube Downloader

In this project, it is developed a Python application that allows users to download YouTube videos for offline viewing. The mission is to create a Python script that takes a YouTube video URL as input and downloads the video to the user's local system. This project will provide a hands-on experience with the `PyTubeFix` library, user input handling, and feedback mechanisms such as a download progress bar.

A simple Python-based YouTube downloader built with `PyTubeFix` and `FFmpeg`.

This project downloads the video and audio streams separately when necessary, then uses FFmpeg to merge them into a single MP4 file containing both video and audio.

## Features

- Download videos from YouTube URLs
- Download high-quality video streams
- Download audio separately when YouTube provides separate video/audio streams
- Automatically merge video and audio using FFmpeg
- Save the final result as an MP4 file
- Automatically remove temporary video and audio files after merging
- Select a specific video resolution

## How It Works

Modern YouTube videos often provide high-resolution video and audio as separate streams.

For example:

```
YouTube
   │
   ├── Video Stream ───► video.mp4
   │
   └── Audio Stream ───► audio.mp4
          │
          ▼
       FFmpeg (Combine "Video + Audio")
          │
          ▼
     final_video.mp4
     ```

The application:

1. Receives a YouTube URL.
2. Creates a `YouTube` object using `PyTubeFix`.
3. Finds the appropriate video stream.
4. Finds the best available audio stream.
5. Downloads both streams.
6. Uses `FFmpeg` to merge them.
7. Removes the temporary files.

##  requirements

Before running the project, make sure you have:

- Python 3.10+
- PyTubeFix
- FFmpeg

__Python__

Check your Python version:

python --version

or:

python3 --version

__PyTubeFix__

`python -m pip install -U pytubefix`

__FFmpeg__

Check whether FFmpeg is installed:

ffmpeg -version

If you are using Ubuntu or WSL, install it with:

```
sudo apt update
sudo apt install ffmpeg
ffmpeg -version
```

## Installation

__1. Clone the repository__

git clone <YOUR_REPOSITORY_URL>
cd 07-Youtube-Downloader

__2. Create a virtual environment__

Linux / macOS:
```
python3 -m venv venv
source venv/bin/activate
```

Windows:
```
python -m venv venv
venv\Scripts\activate
```

__3. Install dependencies__

`pip install pytubefix`

`pip install -r requirements.txt`


## Project Structure

The project structure is:

```
07-Youtube-Downloader/
│
├── images/
│   └── banner.png
├── src/
│   └── youtube_downloader.py
│
├── README.md
└── requirements.txt
```


## Usage

The downloader can be used by creating an instance of `YouTubeDownloader` and calling `download()`.

Example:
```
from downloader import YouTubeDownloader

YouTubeDownloader(
    "https://www.youtube.com/watch?v=jNQXAC9IVRw"
).download()
```
The application will download the required streams and create a final MP4 file.

## Selecting a Quality

The downloader can also receive a quality parameter.

For example:
```
YouTubeDownloader(
    "https://www.youtube.com/watch?v=jNQXAC9IVRw",
    quality="720p"
).download()
```
If no quality is specified:
```
YouTubeDownloader(
    "https://www.youtube.com/watch?v=jNQXAC9IVRw"
).download()
```
the downloader attempts to select 'the highest available video resolution'.

## Output Directory

You can specify where the downloaded video should be saved:
```
from pathlib import Path
from downloader import YouTubeDownloader

YouTubeDownloader(
    "https://www.youtube.com/watch?v=jNQXAC9IVRw",
    output_path=Path("./downloads")
).download()
```
The final MP4 file will be created in 'the specified directory'.

## FFmpeg Integration

When YouTube provides separate video and audio streams, the project uses FFmpeg to combine them.

The equivalent `FFmpeg` command is:
```
ffmpeg \
  -i "video.mp4" \
  -i "audio.m4a" \
  -c:v copy \
  -c:a aac \
  "final.mp4"
```

__What do these options mean?__

|Option| Description
|--| --|
|`-i video.mp4`| `Input video`|
|`-i audio.m4a`| `Input audio`|
|`-c:v copy`| `Copy the video without re-encoding`|
|`-c:a aac`| `Encode audio as AAC`|
|`final.mp4`| `Output file`|

Using `-c:v copy` means the video does not need to be re-encoded, which makes the merging process considerably faster.


## Troubleshooting

### No suitable stream found

If the application prints:

`Video or audio stream not found.`

the requested stream may not be available for that video.

Try another resolution or inspect the available streams.

### Video plays without sound in VS Code

If the downloaded MP4 has sound in VLC or another media player but not in VS Code, the problem may be related to the media player's codec support rather than the downloaded file.

You can verify the file with:

`ffmpeg -i "your_video.mp4"`

Look for both:

Video: ...
Audio: ...

## Important Notes

- Internet access is required to download YouTube content.
- YouTube may change its streaming system, which can occasionally require updates to PyTubeFix.
- Some videos may not be accessible because of restrictions, availability, or authentication requirements.
- The availability of particular resolutions depends on the source video.
- High-resolution YouTube streams are often separate video and audio streams.


## License

This project is intended for educational and personal development purposes.

Make sure you comply with YouTube's terms, copyright law, and the rights of the content owner when downloading videos.

## Author

Developed as a Python project for learning:

- Object-Oriented Programming
- Python file handling
- YouTube streaming
- FFmpeg integration
- Subprocess execution
- Video/audio processing



## In this project:

- The `PyTubeFix` library is used to interact with YouTube content.
    - The `PyTubeFix` library is a Python library for interfacing with YouTube content. It allows you to query for metadata about videos, streams, and playlists; as well as download video and audio streams.
- Filter and select video streams based on parameters like resolution and file extension.
- Create a command-line interface (CLI) for user interaction.
- Implement a progress bar to show download progress.
- Use exception handling for a robust application.
- Manage file input/output in Python.
