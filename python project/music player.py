import pygame
import tkiner as tkr
from tkiner.filedialog import askdirectory
import os
musicplayer=tkr.TK()
musicplayer.title("music player")
musicplayer.geometry("500x500")
directory=askdirectory
os.chdir(directory)
songlist=os.listdir()

playlist=tkr.listbox(musicplayer,font="Verdana 12 bold", fg="white" ,bg="gold",selectmode=tke.SINGLE)

x=0
for i in songlist:
    playlist.insert(x,i)
    x=x+1

pygame.init()
pygame.mixer.init()

def play():
     pygame.mixer.load(playlist.get(tke.active))
     var.set(playlist.get(tke.active))
     playlist.mixer.music.play()
def stop():
     pygame.mixer.music.stop()
def pause():
    pygame.mixer.music.paus()
def unpause():
     pygame.mixer.music.unpause()

button1= tkr.button(musicplayer,width= 6 , height= 4,font="Verdana 12 bold",command="play",bg="navy",fg="gold")
button2= tkr.button(musicplayer,width= 6 , height= 4,font="Verdana 12 bold",command="stop",bg="navy",fg="gold")
button3= tkr.button(musicplayer,width= 6 , height= 4,font="Verdana 12 bold",command="pause",bg="navy",fg="gold")
button4= tkr.button(musicplayer,width= 6 , height= 4,font="Verdana 12 bold",command="unpause",bg="navy",fg="gold")
var=tkr.stringvar()
songtitle=tkr.lable(musicplayer,font="Verdana 12 bold",textvariable = var)
songtitle.pack()
button1.pack(fill="x")
button2.pack(fill="x")
button3.pack(fill="x")
button4.pack(fill="x")
playlist.pack(fill="both",expand="yes")
musicplayer.mainloop()








