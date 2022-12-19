"""
    Laying out the step by step framework for training and text generation. 
"""
#   general imports
import torch 
import torch.nn as nn 
import os 
import string
import unidecode

#   local imports
from corpus.text import Corpus
from src.model import LSTM 
from src.dataset import TensorData
from src.traintest import Trainer
from torch.utils.data import DataLoader


#   DEFINING HYPERPARAMETERS
path = "/home/agastyapatri/Projects/NLP/OklamAI/corpus/lyrics"
seq_len = 32
batch_size = 4
hidden_size = 256
lstm_layers = 2


text_data = Corpus(PATH=path)
tensor_data = TensorData(words=text_data.words, vocab=text_data.vocabulary, sequence_length=seq_len)

model = LSTM(input_size = len(text_data.vocabulary), hidden_size=hidden_size, sequence_length = seq_len, output_size=len(text_data.vocabulary), num_layers=lstm_layers)

trainer = Trainer(model = model, dataset = tensor_data, num_epochs = 10, learning_rate = 0.001, batch_size=batch_size) 

trainer.train_all_epochs()




