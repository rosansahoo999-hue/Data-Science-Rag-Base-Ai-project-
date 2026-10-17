# converts the video to mp3
import os
import subprocess

files = os.listdir('video')
for file in files:
    file_name = file.split('.mp4')[0]
    print(file_name)
    subprocess.run(['ffmpeg', '-i', f'video/{file}', f'audio/{file_name}.mp3'])
