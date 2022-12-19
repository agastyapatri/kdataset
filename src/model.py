"""
    Defining the model that will be used for text generation 
"""
import torch 
import torch.nn as nn 
import numpy as np 
import unidecode 
import string

class LSTM(nn.Module):
    #   Defining a word based LSTM to generate lyrics
    
    def __init__(self, input_size, hidden_size, sequence_length, output_size, num_layers) -> None:
        super().__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.sequence_length = sequence_length 
        
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first = True, dtype = torch.float32)
        self.fc = nn.Linear(hidden_size, output_size, dtype = torch.float32)

    def forward(self, x):
        batch_size = x.size()[0]

        h = torch.zeros(self.num_layers, batch_size, self.hidden_size)
        c = torch.zeros(self.num_layers, batch_size, self.hidden_size)

        output, (hidden, cell)= self.lstm(x, (h, c))
        output = self.fc(output)
        output = output[:, -1, :]
        return output, hidden, cell

    def init_hidden_state(self):
        return (torch.zeros(self.num_layers, self.sequence_length, self.hidden_size),
                torch.zeros(self.num_layers, self.sequence_length, self.hidden_size))


class RNN(nn.Module):

    pass 

class GRU(nn.Module):
    pass 



    


    