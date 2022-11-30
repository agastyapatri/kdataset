"""
    Laying out the framework for training and text generation. 
"""

from corpus.text import Corpus
from src.model import Model 
import os 
import string
import unidecode

"""
    1. Importing the data from a OklamAI/corpus/lyrics/KDOT.txt

    ~ corpus is a list of all sentences. DATASET.
"""
path = "OklamAI/corpus/lyrics/"

dataset = Corpus(PATH=path)













