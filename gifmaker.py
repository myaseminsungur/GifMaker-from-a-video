import subprocess

import imageio.v2



video_path = 'deneme_video.mp4'
vid = imageio.get_reader(video_path, 'ffmpeg')

frames = []
for image in vid:
    frames.append(image)

gif_path = 'output.gif'
imageio.v2.mimsave(gif_path, frames, format='GIF', duration=0.1)

print("GIF created successfully")
