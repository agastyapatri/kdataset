"""
    Training the model. 
"""
import torch
import torch.nn as nn 
import numpy as np 
from model import Network
from dataset import TensorData

class Trainer(nn.Module):
    """
        Training KDOTBOT
    """
    def __init__(self, model ,dataloader, num_epochs, learning_rate) -> None:
        super().__init__()
        self.dataloader = dataloader
        self.num_epochs = num_epochs
        self.network = model    
        self.optimizer = torch.optim.Adam(model.parameters(), lr = learning_rate)

    def train_one_epoch(self, e):
        """
        training the network for a single epoch
        """
        self.network.train(True)
        running_loss = 0.0
        length = len(self.dataloader)


        pass 
    

    def train_all_epochs(self):
        """
        training the network for a single epoch
        """
        pass 
    



if __name__ == "__main__":
    pass 