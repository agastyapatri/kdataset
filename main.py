import torch 
import numpy as np 
from bs4 import BeautifulSoup
import requests
from corpus.song import Song
import os
import json



if __name__ == "__main__":
    #   1. Step One: getting all the song urls from the artist page.

    path = "OklamAI/corpus/lyrics/"

    with open(os.path.join(path, "kendricklamar.html")) as artist_page:
        soup = BeautifulSoup(artist_page, "lxml")
    

    #       1.1 Getting the names of the songs
    songs = soup.find_all("div", class_="listalbum-item")
    albums = soup.find_all("div", class_ = "album")
    song_titles = [] 
    song_links = {} 
    for  song in songs:
        song_titles.append(song.text)   
        song_links[song.text] =  "https://www.azlyrics.com/" + song.a.get("href")


    def save_song_titles(save = None):
        if save == True:
            discography = open(os.path.join(path, "song_titles.txt"), "w+")
            for song  in song_titles:
                discography.write(song + "\n")
            discography.close()

        with open(os.path.join(path, "song_links.json"), "w+", encoding="utf-8") as links:
            json.dump(song_links, links, ensure_ascii=False, indent=4)
            links.close()      


    #   2. Getting the song lyrics from each link 
    song = Song(title = "Hood Politics")
    print(song.lyrics)

