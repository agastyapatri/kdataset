"""
    Defining the model that will be used for text generation 
"""
import torch 
import torch.nn as nn 
import numpy as np 
import unidecode 
import string

class Dataset(torch.utils.data.Dataset):
    def __init__(self) -> None:
        super().__init__()

class Network(nn.Module):
    #   Defining a word based LSTM to generate lyrics
    
    def __init__(self, input_size, hidden_size, sequence_length, output_size, num_layers) -> None:
        super().__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.sequence_length = sequence_length 
        
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first = True, dtype = torch.float32)
        self.fc = nn.Linear(hidden_size, output_size, dtype = torch.float32)


    def forward(self, x, hidden, cell):
        ouptut, (hidden, cell) = self.lstm(x, (hidden , cell))
        output = self.fc(output)
        return output, hidden, cell 


    def init_hidden_state(self, sequence_length):
        return (torch.zeros(self.num_layers, self.sequence_length, self.lstm_size),
                torch.zeros(self.num_layers, self.sequence_length, self.lstm_size))

    


    