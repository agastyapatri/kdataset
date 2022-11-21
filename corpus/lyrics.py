"""
    Getting the lyrics of all KDot songs from <somewhere> on the internet 
"""
import requests
import bs4 
from bs4 import BeautifulSoup
import os


if __name__ == "__main__":
    reqs = requests.get(url="https://www.azlyrics.com/k/kendricklamar.html")
    soup = BeautifulSoup(reqs.text, "lxml")

