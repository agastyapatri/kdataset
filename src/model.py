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
    
    def __init__(self, dataset) -> None:
        super().__init__()
        self.lstm_size = 128 
        self.embedding_dim = 128 
        self.num_layers = 3 
        self.n_vocab = 10
    
    def __getitem__(self, i):
        #   Returning the Nth layer of the network 
        return self.network()[i]

    def __str__(self):
        #   Describing the network 
        return f"\nOklamAI: Kendrick Lamar Lyric Generation.\n" 
    
    def network(self):
        net = nn.Sequential(

            nn.Embedding(
                num_embeddings = self.n_vocab,
                embedding_dim=self.embedding_dim,
                ),

            nn.LSTM(
            input_size = self.lstm_size,
            hidden_size = self.lstm_size,
            num_layers = self.num_layers,
            dropout = 0.2
                ),

            nn.Linear(self.lstm_size, self.n_vocab)
        )
        return net
    
    def init_state(self, sequence_length):
        return (torch.zeros(self.num_layers, sequence_length, self.lstm_size),
                torch.zeros(self.num_layers, sequence_length, self.lstm_size))

    


if __name__ == "__main__":  
    lstm = Network(dataset = None)
    print(lstm.network())