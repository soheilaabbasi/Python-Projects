![alt text](images/banner.png)
# YouTube Downloader

In this project, it is developed a Python application that allows users to download YouTube videos for offline viewing. The mission is to create a Python script that takes a YouTube video URL as input and downloads the video to the user's local system. This project will provide a hands-on experience with the `pytube` library, user input handling, and feedback mechanisms such as a download progress bar.

Users should be able to run YouTube Downloader from the command line or used as a module in other Python scripts. Here are the basic steps to use the tool:

`python youtube_downloader.py <youtube-url> <video-quality> <output-directory>`

You can also use argparse to parse the command line arguments. The following is an example of how to use argparse to parse the command line arguments:

`python youtube_downloader.py --url <youtube-url> --quality <video-quality> --output <output-directory>`

And the video(s) will be downloaded to the specified output directory.

In this project:
- The `pytube` library is used to interact with YouTube content.
    - The `pytube` library is a Python library for interfacing with YouTube content. It allows you to query for metadata about videos, streams, and playlists; as well as download video and audio streams.
- Filter and select video streams based on parameters like resolution and file extension.
- Create a command-line interface (CLI) for user interaction.
- Implement a progress bar to show download progress.
- Use exception handling for a robust application.
- Manage file input/output in Python.

## Features

- __Command Line Interface (CLI):__ A simple CLI for easy interaction with the downloader. This is the primary interface through which users will interact with your application.
- __Graphical User Interface (GUI):__ As an advanced feature, consider developing a GUI using a library like streamlit for a more user-friendly experience. This is optional but can greatly enhance usability.
- __Download Progress Bar:__ Incorporate real-time feedback on the download progress so users can see how much of the video has been downloaded.
- __Configurable Settings:__ Allow users to set default download folders, preferred video quality, and other settings to customize their experience.
- __Playlist Downloading:__ Another advanced feature is to enable users to download entire playlists in addition to individual videos.
- __Audio Extraction:__ Give users the option to download only the audio track of a video in MP3 format.
- __Error Handling:__ Gracefully handle common errors, such as invalid URLs or network issues.
