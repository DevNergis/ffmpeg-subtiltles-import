import os

print("made by Dev_Nergis")

vinput = input('video input : ')
voutput = input('video output : ')
subtiltles = input('subtiltles file : ')

os.system('ffmpeg -i %s -i %s -map 0:v:0 -c:v copy -map 0:a:0 -c:a copy -map 1 -c:s:0 mov_text -metadata:s:s:0 title=srt -metadata:s:s:0 language=kor %s' % (vinput, subtiltles, voutput))
