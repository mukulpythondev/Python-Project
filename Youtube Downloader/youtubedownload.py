from pytube import YouTube
from pytube import Playlist
import time
while True:
    choice=input(" Download video or Playlist:\n")
    if choice.lower()=='video':
        def youtube_downloader():
            print("****** Welcome To Youtube Video Downloader ******")
            time.sleep(1)
            print("   Menu    ")
            time.sleep(1)
            print("1.Download Tittle of Video  \n")
            time.sleep(1)
            print("2.Download Thumbnail of Video  \n ")
            time.sleep(1)
            print("3. Download The Video \n")
            time.sleep(1) 
            print("4.Exit\n")
            try:
                task=int(input("Enter the number for specific work \n"))
                if task==1:
                    link=input("Enter the video link \n")
                    youtube_1=YouTube(link)

                    print(youtube_1.title)# To download Title 
                elif task==2:
                    link=input("Enter the video link \n")
                    youtube_1=YouTube(link)
                    print(youtube_1.thumbnail_url)
                elif task==3:
                    link=input("Enter the video link \n")
                    youtube_1=YouTube(link)
                    video=youtube_1.streams.all()
                    audio=youtube_1.streams.filter(only_audio=True)
                    quality=list(enumerate(video))
                    for i in quality:
                        print(i)
                    strm=int(input("Enter the Quality :\n"))
                    video[strm].download()
                    print("Downloading ") 

                elif task==4:
                   print("Exit")

                   
            except Exception as e:
                print("Enter Correct Url of Video ")
#To download *****Playlist******
    elif choice.lower()=='playlist':
        try:

            url=input("Enter the url of Playlist\n")
            playlist=Playlist(url)
            print(f"Downloading {playlist.title}")
            for video in playlist.videos:
                video.streams.first().download()
    
        except Exception as e :
            print("Enter the correct URL")
    downloader=youtube_downloader()