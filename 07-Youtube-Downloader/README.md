![alt text](images/banner.png)
# YouTube Downloader

In this project, it is developed a Python application that allows users to download YouTube videos for offline viewing. The mission is to create a Python script that takes a YouTube video URL as input and downloads the video to the user's local system. This project will provide a hands-on experience with the `PyTubeFix` library, user input handling, and feedback mechanisms such as a download progress bar.

A simple Python-based YouTube downloader built with `PyTubeFix`, `FFmpeg` and `tqdm`.

This project downloads the video and audio streams separately when necessary, then uses `FFmpeg` to merge them into a single MP4 file containing both video and audio.

The project also provides a command-line interface (CLI) using Python's built-in `argparse` module.

## Features

- Download videos from YouTube URLs
- Download high-quality video streams
- Select a specific video resolution
- Download video and audio streams separately
- Automatically merge video and audio using FFmpeg
- Save the final result as an MP4 file
- Automatically remove temporary video and audio files after merging
- Display download progress using `tqdm`
- Specify a custom output directory
- Handle unavailable videos and unexpected errors
- Provide a command-line interface using `argparse`


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
                           FFmpeg (Merge) 
                           │ 
                           ▼ 
                           final_video.mp4

```



The application:

1. Receives a YouTube URL from the command line..
2. Creates a `YouTube` object using `PyTubeFix`.
3. Finds the appropriate video stream.
4. Finds the best available audio stream.
5. Downloads both streams.
6. Uses `FFmpeg` to merge them.
7. Removes the temporary files.
8. Saves the final MP4 file in the selected output directory.

##  requirements

Before running the project, make sure you have:

- Python 3.10+
- PyTubeFix
- tqdm
- FFmpeg

__Python__

Check your Python version:

python --version

or:

python3 --version

__PyTubeFix and tqdm__

`python -m pip install -U pytubefix`
`python -m pip install -U pytubefix tqdm`

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
The application is designed to be used from the command line.

Run the downloader with:

`python src/youtube_downloader.py <YOUTUBE_URL>`

Example:

`python src/youtube_downloader.py "https://www.youtube.com/watch?v=jNQXAC9IVRw"`

If no quality or output directory is specified, the application:

- Attempts to select the highest available video resolution.
- Saves the downloaded file in the current working directory.

```
from downloader import YouTubeDownloader

YouTubeDownloader(
    "https://www.youtube.com/watch?v=jNQXAC9IVRw"
).download()
```


## Selecting a Quality

Use the `-q` or `--quality` option to specify the desired video resolution.

For example:

`python src/youtube_downloader.py "https://www.youtube.com/watch?v=jNQXAC9IVRw" -q 720p`

You can also write:

`python src/youtube_downloader.py "https://www.youtube.com/watch?v=jNQXAC9IVRw" --quality 720p`

If `--quality` is not specified:

`highest` is used by default, and the downloader attempts to select the highest available video resolution.

The requested resolution must be available for the selected video.

## Selecting an Output Directory

Use the `-o` or `--output_path` option to specify where the downloaded files should be saved.

Example:

`python src/youtube_downloader.py "https://www.youtube.com/watch?v=jNQXAC9IVRw" -o ./downloads`

You can also combine the output directory with a specific quality:

`python src/youtube_downloader.py "https://www.youtube.com/watch?v=jNQXAC9IVRw" -q 720p -o ./downloads`

If no output directory is specified, the current working directory is used.

## Command-Line Options

The application provides the following command-line arguments:

|Argument|	Description|	Default|
|--|--|--|
|`url`|	YouTube video URL|	Required|
|--|--|--|
|`-q`, `--quality`|	Video resolution, such as `720p`|	`highest`|
|--|--|--|
|`-o`, `--output_path`|	Directory where the files will be saved|	Current directory|


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
|`-y`|`Overwrite the output file if it already exists`|
|`final.mp4`| `Output file`|

Using `-c:v copy` means the video does not need to be re-encoded, which makes the merging process considerably faster.


## Progress Bar

The downloader uses the `tqdm` library to display download progress.

Separate progress bars are displayed for:

Video download
Audio download

The progress callback provided by `PyTubeFix` is used to update the progress bar while the file is being downloaded.


## Error Handling

The application uses exception handling to deal with common problems during the download process.

### Video Unavailable

If the requested video is unavailable, the application displays an error message:

`Video is unavailable.`

Possible causes include:

- Invalid or unavailable video
- Video restrictions
- Removed video
- Authentication requirements

### Video or Audio Stream Not Found

If a suitable video or audio stream cannot be found, the application displays:

`Video or audio stream not found.`

This can happen when the requested resolution is not available.

Try another resolution.

### Unexpected Errors

Other errors are caught and displayed as:

An unexpected error occurred: ...

This prevents the application from failing without providing information about what went wrong.

## Troubleshooting

### FFmpeg is not found

If the application cannot find `FFmpeg`, make sure it is installed and available in your system's `PATH`.

Check with:

`ffmpeg -version`

### No suitable stream found

If the application prints:

`Video or audio stream not found.`

the requested stream may not be available for that video.

Try another resolution:

`python src/youtube_downloader.py "<YOUTUBE_URL>" -q 720p`

### Video plays without sound

If the downloaded MP4 has sound in VLC or another media player but not in VS Code, the problem may be related to the media player's codec support.

You can inspect the output file with:

`ffmpeg -i "your_video.mp4"`

Look for both:

```
Video: ...
Audio: ...
```


## Important Notes

- Internet access is required to download YouTube content.
- YouTube may change its streaming system, which can occasionally require updates to PyTubeFix.
- Some videos may not be accessible because of restrictions, availability, or authentication requirements.
- The availability of particular resolutions depends on the source video.
- High-resolution YouTube streams are often separate video and audio streams.
- Downloading content should comply with YouTube's terms, applicable copyright law, and the rights of the content owner.

## License

This project is intended for educational and personal development purposes.

Make sure you comply with YouTube's terms, copyright law, and the rights of the content owner when downloading videos.

## Author

Developed as a Python project for learning:

- Object-Oriented Programming
- Python file handling
- Command-line interfaces
- `argparse`
- YouTube streaming
- `FFmpeg` integration
- `Subprocess` execution
- Video/audio processing
- Exception handling
- Progress bars with `tqdm`

## Technologies Used

### PyTubeFix

`PyTubeFix` is used to interact with YouTube content. It allows the application to retrieve video metadata and available streams and download video/audio streams.

### argparse

Python's built-in `argparse` module is used to create the command-line interface.

The user can provide:

- YouTube URL
- Video quality
- Output directory

### tqdm

`tqdm` is used to display download progress.

### FFmpeg

FFmpeg is used to merge the separately downloaded video and audio streams into the final MP4 file.

### pathlib

Python's `pathlib` module is used for filesystem path handling.

### subprocess

Python's `subprocess` module is used to execute FFmpeg from the Python application.

### Exception Handling

Python exception handling is used to handle unavailable videos and unexpected runtime errors.



## In this project:

- The `PyTubeFix` library is used to interact with YouTube content.
    - The `PyTubeFix` library is a Python library for interfacing with YouTube content. It allows you to query for metadata about videos, streams, and playlists; as well as download video and audio streams.
- Filter and select video streams based on parameters like resolution and file extension.
- Create a command-line interface (CLI) for user interaction.
- Implement a progress bar to show download progress.
- Use exception handling for a robust application.
- Manage file input/output in Python.
