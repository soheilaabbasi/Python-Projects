from pytubefix import YouTube
from pathlib import Path
import subprocess


class YouTubeDownloader:
    def __init__(self, url, output_path=None, quality=None):
        self.url = url
        self.output_path = output_path or Path().cwd()
        self.quality = quality or 'highest'
        self.yt = YouTube(self.url, on_progress_callback=self.on_progress
                          , on_complete_callback=self.on_complete)

    def on_progress(self, stream, chunk, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining

        print(
            f"\r('downloading...':<15)"
            f"{(100*(total_size-bytes_remaining)/total_size):>3.0f}% "
            f"| {bytes_downloaded/1024/1024:>5.1f}MB"
            f" of {total_size/1024/1024:>5.1f}MB "
            f"| {'finished':<10}",
            end=''
        )


    def on_complete(self, stream, file_path):
        print()
        print(f"Download complete. File saved to: {file_path}")


    def download(self):
        # Download video
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

        video_file = video_stream.download(
            output_path=self.output_path,
            filename="video.mp4"
        )

        audio_file = audio_stream.download(
            output_path=self.output_path,
            filename="audio.mp4"
        )


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

        subprocess.run(command, check=True)

        # Delete temporary files
        Path(video_file).unlink()
        Path(audio_file).unlink()

        print(f"Download completed: {final_file}")



if __name__ == '__main__':
    url = input("Enter a youtube url:")
    YouTubeDownloader(url).download()
    