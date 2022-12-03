import requests
import bs4 
from bs4 import BeautifulSoup
import os
import json 
import unidecode
import string
import collections 


class Song:
    """
        Defining a class that creates a song which is indexible by name.
    """
    def __init__(self, title) -> None:
        self.title = title
        self.lyrics = self.getlyrics()
        self.artist = "Kendrick Lamar"
        self.album = None 

    #   Getting a single line of the song
    def __getitem__(self, i):
        lyrics = self.getlyrics().split("\n")
        return lyrics[i]

    #   Printing out metadata 
    def __str__(self):
        return f"TITLE: {self.title}\nALBUM:{None}\nARTIST:{self.artist}"

    #   getting the lyrics of one song
    def getlyrics(self):

        PATH = "OklamAI/corpus/lyrics/proxy_servers.txt"
    
        with open(PATH) as file:
            proxy_list = file.read()
            file.close()
    
        #   proxy_list is a list of proxy IP addresses with dtype string.
        proxy_list = proxy_list.split(" ")[0].split("\n")

        with open("OklamAI/corpus/lyrics/song_links.json") as file:
            song_links = json.load(file)
            file.close()
            link = song_links[self.title]
        for proxy in proxy_list:
            try: 
                reqs = requests.get(url=link, proxies={"http": proxy, "https" : proxy}, timeout=15)
                soup = BeautifulSoup(reqs.text, "lxml")

                body = soup.find("div", class_ = "col-xs-12 col-lg-8 text-center")
                lyrics  = body.find_all("div", class_ = None)[0].text
                return lyrics
            except:
                pass


class Corpus:
    """
        Defining the entire text corpus from locally sourced data, to avoid making HTTP requests all the time. 

        ~   vectorize: opting into vectorizing the corpus for feeding the network
        ~   words: representing the dataset as a list of words or list of sentences. 
    """       
    def __init__(self, PATH) -> None:
        self.path = PATH 


        self.words = self.get_words()[0]
        self.vocabulary = self.get_words()[1]


    def __getitem__(self, i):
        #   returning the nth line of the corpus
        return self.getlyrics()[i]        

    def __str__(self) -> str:
        #   returning the entirety of the lyrics
        return f"\nTHE KENDRICK LAMAR DATASET\nNumber of lines = {len(self.getlyrics())}\nNumber of Words = 75687 \nSize of Vocabulary = {len(self.get_words()[1])}\n"

    def __len__(self) -> int:
        return len(self.getlyrics())

    def get_words(self):
        #   Finding the unique words in the entire corpus. 
        lyrics = self.getlyrics()
        words = []
        for sentence in lyrics:
            temp = sentence.split(" ")
            for word in temp: 
                words.append(word)
        vocab = set(words)
        
        return words, vocab 

    def getlyrics(self):
        #   getting the lyrics from a local source
        with open(os.path.join(self.path, "KDOT.txt"), "r") as file: 
            corpus = unidecode.unidecode(file.read())
            corpus = corpus.split("\n")
        lines = [line.strip(r"\"") for line in corpus]
        lines = [line.translate(str.maketrans("", "", string.punctuation)) for line in corpus]
        
        return lines


if __name__ == "__main__":

    corpus = Corpus(PATH="/home/agastyapatri/Projects/NLP/OklamAI/corpus/lyrics/")
    print(corpus)
            


    
    
    


