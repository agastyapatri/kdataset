import requests
import bs4 
from bs4 import BeautifulSoup
import os
import json 
from requests_ip_rotator import ApiGateway

class Song:
    """
        Defining a class that creates a song which is indexible.
    """
    def __init__(self, title) -> None:
        self.title = title
        self.lyrics = self.getlyrics()
        self.artist = "Kendrick Lamar"
        self.album = None 


    #   Getting a single line of the song
    def __getitem__(self, i):
        # return self.getlyrics()[i]
        pass 

    #   Printing out metadata 
    def __str__(self):
        return f"TITLE: {self.title}\nALBUM:{None}\nARTIST:{self.artist}"


    #   getting the lyrics of one song
    def getlyrics(self):
        with open("OklamAI/corpus/lyrics/song_links.json") as file:
            song_links = json.load(file)
            file.close()
        link = song_links[self.title]
        reqs = requests.get(url=link)
        soup = BeautifulSoup(reqs.text, "lxml")

        body = soup.find("div", class_ = "col-xs-12 col-lg-8 text-center")
        lyrics  = body.find_all("div", class_ = None)[0].text


        return lyrics
            


        

    
        



if __name__ == "__main__":
    song = Song("Hood Politics")
    print(song.lyrics)
    


    


    
            


    
    
    


