from pytube import YouTube
import streamlit as st
import os

# YouTube video URL
# video_url = 'https://youtu.be/7zJvNZVZMew'

# Set the output directory


# # Choose the highest resolution stream (usually the first one)
# video_stream = yt.streams.get_highest_resolution()

# # Download the video
# video_stream.download(output_path=output_dir)

# print("Video downloaded successfully!")

class Download:
    def __init__(self):
        pass

    def youtube_d(self,url):
        self.url = url
        os.makedirs('test_videos',exist_ok=True)
        output_dir = "test_videos" 
        print(url)
        yt = YouTube(url)
        video_stream = yt.streams.get_highest_resolution()
        video_stream.download(output_path=output_dir)

        return yt.title, output_dir
    


        