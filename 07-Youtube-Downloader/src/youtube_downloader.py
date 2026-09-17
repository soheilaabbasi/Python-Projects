from pytubefix import YouTube
from pathlib import Path
import subprocess
import time
# from time import sleep
from tqdm import tqdm

class YouTubeDownloader:
    def __init__(self, url, output_path=None, quality=None):
        self.url = url
        self.output_path = output_path or Path().cwd()
        self.quality = quality or 'highest'
        self.yt = YouTube(self.url, on_progress_callback=self.on_progress
                          , on_complete_callback=self.on_complete)


    def download(self):

        # Find video stream

        if self.quality == 'highest':
            video_stream = (self.yt.streams.filter(
                progressive=False, 
                file_extension='mp4',
                only_video=True
                ).order_by("resolution").desc().first()
            )
        else:
            video_stream = (self.yt.streams.filter(
                progressive=False, 
                file_extension='mp4',
                only_video=True,
                res=self.quality
            ).first()
            )

        # Download audio
        # Find audio stream

        audio_stream = (
            self.yt.streams
            .filter(
                only_audio=True,
                file_extension="mp4"
            )
            .order_by("abr")
            .desc()
            .first()
        )



        if video_stream is None or audio_stream is None:
            print("Video or audio stream not found.")
            return

        # -------------------------
        # Download video
        # -------------------------

        self.pbar = tqdm(
                    desc='Downloading video...',
                    total=video_stream.filesize,
                    unit='B',
                    unit_scale=True,
                    unit_divisor=1024
                    )

        video_file = video_stream.download(
            output_path=self.output_path,
            filename="video.mp4"
        )

        self.pbar.close()

        # -------------------------
        # Download audio
        # -------------------------

        self.pbar = tqdm(
                    desc='Downloading audio...',
                    total=audio_stream.filesize,
                    unit='B',
                    unit_scale=True,
                    unit_divisor=1024
                    )

        audio_file = audio_stream.download(
            output_path=self.output_path,
            filename="audio.mp4"
        )

        self.pbar.close()

        # -------------------------
        # Merge video + audio
        # -------------------------

        # after getting the video and audio seperately, 
        # now we combine two files and make final video that has sound.

        # Final file
        final_file = self.output_path / f"{self.yt.title}.mp4"

        command = [
            "ffmpeg",
            "-i", video_file,
            "-i", audio_file,
            "-c:v", "copy",
            "-c:a", "aac",
            "-y",
            str(final_file)
        ]

        subprocess.run(
            command, 
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
            )

        # -------------------------
        # Delete temporary files
        # -------------------------

        Path(video_file).unlink()
        Path(audio_file).unlink()

        print(f"Download completed: {final_file}")


    def on_progress(self, stream, chunk, bytes_remaining):
        current = stream.filesize - bytes_remaining
        self.pbar.update(current - self.pbar.n)     # (the current place that I should be) - (the place that I have gone in progress bar till now)
        
    
    def on_complete(self, stream, file_path):
        pass



if __name__ == '__main__':
    url = input("Enter a youtube url:")
    YouTubeDownloader(url).download()
    