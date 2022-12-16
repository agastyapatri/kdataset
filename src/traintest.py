"""
    Training the model. 
"""
import torch
import torch.nn as nn 
import numpy as np 
from model import LSTM
from dataset import TensorData

class Trainer(nn.Module):
    """
        Training KDOTBOT
    """
    def __init__(self, model ,dataloader, num_epochs, learning_rate, batch_size) -> None:
        super().__init__()
        self.dataloader = dataloader
        self.num_epochs = num_epochs
        self.network = model
        self.batch_size = batch_size
        
        self.optimizer = torch.optim.Adam(model.parameters(), lr =  learning_rate)
        self.loss_fun = nn.CrossEntropyLoss()


    def __str__(self):
        sentence1 = f"\nTraining the network. Hyperparameters of the training process:\n" 
        sentence2 = f"Number of Epochs = {self.num_epochs}\n"
        sentence3 = f"Number of sequences in a batch = {self.batch_size}\n"
        sentence4 = f"Optimizer = {self.optimizer.__str__()}\n"
        sentence5 = f"Loss Function = {self.loss_fun.__str__()}\n"
        return sentence1 + sentence2 + sentence3 + sentence4 + sentence5


    def train_one_epoch(self, e):
        """
        training the network for a single epoch
        """
        self.network.train(True)
        running_loss = 0.0
        length = len(self.dataloader)

        for i, sample in enumerate(self.dataloader):
            sample = sample.unsqueeze(0)
            output = self.network(sample)
            pass 
        pass 
    

    def train_all_epochs(self):
        """
        training the network all the epochs
        """
        hidden, cell = self.network.init_hidden_state()
        pass 
    



