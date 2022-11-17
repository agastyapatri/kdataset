"""
    Getting the lyrics of all KDot songs from <somewhere> on the internet 
"""
import requests
import bs4 
from bs4 import BeautifulSoup
import os
import urllib.request as request


class Corpus:
    """
        Python Class to generate a text corpus of kendrick lamar's lyrics.
        This class does the following things:
            1. Collecting a list of URL's that will be queried
            2. Entering each URL to scrape the lyrics 
            3. Generating a txt file similar to the shakespeare dataset
    """

    #   Should return the number of lines in the final corpus
    def __getitem__(self):
        pass 
    
    def __str__(self) -> str:
        return f"Kendrick Lamar Dataset. Number of Lines = {0}"

    #   Function to get the lyrics from a particular url
    def gettext(self, url, save=None):
        pass 

    #   Function to generate the complete text file; Final Dataset.
    def getcorpus(self, url_set):
        pass 


if __name__ == "__main__":
    url = "https://www.azlyrics.com/k/kendricklamar.html"
    reqs = requests.get(url=url)
    soup = BeautifulSoup(reqs.text, "html.parser")

    urls = []
    for link in soup.find_all("a"):

        #   only getting all the kendrick lamar songs (singles + album releases) from the website
        if "lyrics/kendricklamar" in str(link.get("href")):
            urls.append("https://www.azlyrics.com/" + link.get("href"))


