import moviepy.tools

cvt_video = moviepy.VideoFileClip('Shaboozey.webm')

ext_audio = cvt_video.audio

ext_audio.write_audiofile('Shaboozey.mp3')