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
    Explanation: pending
"""
path = "/home/agastyapatri/Projects/NLP/OklamAI/corpus/lyrics"

kdot = Corpus(PATH=path)

dataset = TensorData(text_data=kdot.words)
print(dataset[10:100])



















