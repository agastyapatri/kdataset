"""
    Laying out the step by step framework for training and text generation. 
"""

import os 
import string
import unidecode
from corpus.text import Corpus
from src.model import Network 
from src.dataset import TensorData

"""
    1. Loading the Data.
    ~ text data is a list of sentences.
    ~ tensor data is a matrix where each row is a one hot encoding of each sentence. 
    
"""
path = "/home/agastyapatri/Projects/NLP/OklamAI/corpus/lyrics"

text_data = Corpus(PATH=path)
tensor_data = TensorData(text_data=text_data.vocabulary)

print(text_data)









