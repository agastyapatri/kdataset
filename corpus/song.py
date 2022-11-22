import requests
import bs4 
from bs4 import BeautifulSoup
import os

class Song:
    """
        Defining a class that creates a song which is indexible.
    """
    def __init__(self, title) -> None:
        self.title = title
        self.lyrics = None
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
        pass


    
        













if __name__ == "__main__":

    #   1. Step One: getting all the song urls from the artist page.

    path = "OklamAI/corpus/lyrics/"

    with open(os.path.join(path, "kendricklamar.html")) as artist_page:
        soup = BeautifulSoup(artist_page, "lxml")
    
    songs = soup.find_all("div", class_="listalbum-item")
    song_titles = [] 
    for  song  in songs:
        song_titles.append(song.text)   

    def save_song_titles(save = None):
        if save == True:
            discography = open(os.path.join(path, "song_titles.txt"), "w+")
            for song  in song_titles:
                discography.write(song + "\n")
            discography.close()

    
    


    
            


    
    
    


