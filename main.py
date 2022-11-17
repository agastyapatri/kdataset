import torch 
import numpy as np 
from bs4 import BeautifulSoup
import requests
from corpus.lyrics import Corpus



#   1. GETTING THE URLS

url = "https://www.azlyrics.com/k/kendricklamar.html"
reqs = requests.get(url=url)
soup = BeautifulSoup(reqs.text, "html.parser")

urls = []
for link in soup.find_all("a"):
    #   only getting all the kendrick lamar songs (singles + album releases) from the website        
    if "lyrics/kendricklamar" in str(link.get("href")):
        urls.append("https://www.azlyrics.com/" + link.get("href"))


dataset = Corpus()
print(dataset)

