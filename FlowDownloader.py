from asyncio import wait_for
from pytube import YouTube

from random import randint
from pytube.cli import on_progress
# Ascii art \/
print("""\
  ______ _                 _____                      _                 _           
 |  ____| |               |  __ \                    | |               | |          
 | |__  | | _____      __ | |  | | _____      ___ __ | | ___   __ _  __| | ___ _ __ 
 |  __| | |/ _ \ \ /\ / / | |  | |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |/ _ \ '__|
 | |    | | (_) \ V  V /  | |__| | (_) \ V  V /| | | | | (_) | (_| | (_| |  __/ |   
 |_|    |_|\___/ \_/\_/   |_____/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|\___|_|                                                                                                                                                                       
                          The Fastest Youtube Downloader      Made by Erik Hellak
                    """)
# Asking for Link input
link = input("Flow Downloader: Enter Youtube link:")
yt = YouTube(link)

print("Flow Downloader: Downloading from YouTube...")

# Searching for Video on Youtube
yt=YouTube(link,on_progress_callback=on_progress)
videos=yt.streams.first()
videos.download()
print("(:")
  
# downloading Video in Highest Res
ys = yt.streams.get_highest_resolution()
ys.download()
print(" ")
print("Flow Downloader: Download Completed!")


# Auto Closing the Programm
n = 100
while n > 0:
    n -= 1
print("Bye...")

exit()
