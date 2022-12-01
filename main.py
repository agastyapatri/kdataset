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

    ~   DATASET: kdot is a list of all the sentences that occur in the discography.
    ~   vocab is a list of all unique words that occur in the dataset.   
"""
path = "OklamAI/corpus/lyrics/"
kdot = Corpus(PATH=path, words = False, vectorize=True)
vocab = kdot.vocabulary()



#   Describing the data with plots.
def describe_data():

    pass 





















