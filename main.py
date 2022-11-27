"""
    Laying out the framework for training and text generation. 
"""

from corpus.song import Song
from src.model import Model 
import os 
import string
import unidecode

"""
    1. Importing the data from a OklamAI/corpus/lyrics/KDOT.txt

    ~ corpus is a list of all sentences. 
"""
path = "OklamAI/corpus/lyrics/"
 
with open(os.path.join(path, "KDOT.txt")) as file:
    corpus =  unidecode.unidecode(file.read())
    corpus = corpus.split("\n")


print(corpus[3])














