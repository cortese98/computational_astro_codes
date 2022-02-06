#Script used to produce the movie of the petar positions. The same script has been used for all the movies produced


from moviepy.editor import *
import numpy as np

files=[]
for i in range (118):
    name= "positions_PeTar_"+str(i)+".png"
    files.append(name)
print (files)
    
clip = ImageSequenceClip(files, fps = 6) 
clip.write_videofile("video.mp4", fps = 30)
