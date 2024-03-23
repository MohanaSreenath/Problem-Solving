from pytube import YouTube
from  tkinter import *
ytlink=input("enter the youtube url :")
yt = YouTube(ytlink)
print("Title :",yt.title)
print("view: ", yt.views)
yd=yt.streams.get_highest_resolution()
pth1=input("Enter the path where you need to download :")
pth1=pth1.replace('\\','/')
pth1=pth1.replace('"','')
yd.download(pth1)
print("Download Completed")
