from os import path
from pydub import AudioSegment
import os
import sys

count=1
for file in [doc for doc in os.listdir(os.curdir) if doc.endswith(".mp3")]:
	print(file)     
	dst="Group_Defense."+str(count)+".wav"                                                          
	sound = AudioSegment.from_mp3(file)
	sound.export(dst, format="wav")
	count+=1
