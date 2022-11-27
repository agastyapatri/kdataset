from corpus.song import Song
from src.model import Model 
import os 

"""
    1. Importing the data from a OklamAI/corpus/lyrics/KDOT.txt

    ~ corpus is a list of all sentences. 
"""
path = "OklamAI/corpus/lyrics/"
 
with open(os.path.join(path, "KDOT.txt")) as file:
    corpus =  file.read().split("\n")







