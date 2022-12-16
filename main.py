"""
    Laying out the step by step framework for training and text generation. 
"""
#   general imports
import torch 
import torch.nn as nn 
import os 
import string
import unidecode

#   imports from local files
from corpus.text import Corpus
from src.model import LSTM 
from src.dataset import TensorData
from src.traintest import Trainer
from src.utils import Evaluate 

"""
    1. Loading the Data.
    ~ text data is a list of sentences.
    ~ tensor data is a matrix where each row is a one hot encoding of each sentence. 
    
"""
path = "/home/agastyapatri/Projects/NLP/OklamAI/corpus/lyrics"
text_data = Corpus(PATH=path)
tensor_data = TensorData(words=text_data.words, vocab=text_data.vocabulary)
dataloader = torch.utils.data.DataLoader(tensor_data)

model = LSTM(input_size = len(text_data.vocabulary), hidden_size=256, sequence_length = 128, output_size=len(text_data.vocabulary), num_layers=2)
trainer = Trainer(model = model, dataloader = dataloader, num_epochs = 100, learning_rate = 0.001, batch_size=128) 

print(trainer)











