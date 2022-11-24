"""
    Python Program to create the required text corpus form scraping the web.
"""

import numpy as np 
from bs4 import BeautifulSoup
import requests
from song import Song
import os
import json
import random 



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
        try: 
            if save == True:
                discography = open(os.path.join(path, "song_titles.txt"), "w+")
                for song  in song_titles:
                    discography.write(song + "\n")
                discography.close()

            with open(os.path.join(path, "song_links.json"), "w+", encoding="utf-8") as links:
                json.dump(song_links, links, ensure_ascii=False, indent=4)
                links.close()      
        except: 
            print("Current IP Blocked")


    #   2. Getting the song lyrics from each link | Outputting to text files.
    def save_song_lyrics():

        for title in song_titles:
            try: 
                song = Song(title = title)
                lyrics = song.lyrics
                name = title + ".txt"
                if not os.path.exists(os.path.join(path, "lyric_pages/", name)):
                    with open(os.path.join(path, "lyric_pages/", name), "w+") as file:
                        file.write(lyrics)
                        file.close()

            except:
                pass 
    