import os
import string
from string import punctuation

os.system('@echo off')
os.system('title ffmpeg-subtiltles-import-v3 - Made By Dev_Nergis')
os.system('cls')

print("made by Dev_Nergis")

vinput = input('video input : ')
voutput = input('video output : ')
subtiltles = input('subtiltles file : ')

vinput = '%s' % (vinput).strip(string.punctuation)
voutput = '%s' % (voutput).strip(string.punctuation)
subtiltles = '%s' % (subtiltles).strip(string.punctuation)

print(vinput)
print(voutput)
print(subtiltles)

os.system('ffmpeg -i "%s" -i "%s" -map 0:v:0 -c:v copy -map 0:a:0 -c:a copy -map 1 -c:s:0 mov_text -metadata:s:s:0 title=srt -metadata:s:s:0 language=kor "%s"' % (vinput, subtiltles, voutput))
