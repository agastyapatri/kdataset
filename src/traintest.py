"""
    Training the model. 
"""
import torch
import torch.nn as nn 
from torch.utils.data import DataLoader
import numpy as np 
from model import LSTM
from dataset import TensorData


class Trainer(nn.Module):
    """
        Training KDOTBOT
    """
    def __init__(self, model, dataset, num_epochs, learning_rate, batch_size) -> None:
        super().__init__()
        self.dataloader = DataLoader(dataset, batch_size=batch_size)
        self.num_epochs = num_epochs
        self.network = model
        # self.batch_size = batch_size
        
        self.optimizer = torch.optim.Adam(model.parameters(), lr =  learning_rate)
        self.loss_fun = nn.CrossEntropyLoss()


    def __str__(self):
        sentence1 = f"\nTraining the network. Hyperparameters of the training process:\n" 
        sentence2 = f"Number of Epochs = {self.num_epochs}\n"
        sentence3 = f"Number of sequences in a batch = {self.batch_size}\n"
        sentence4 = f"Optimizer = {self.optimizer.__str__()}\n"
        sentence5 = f"Loss Function = {self.loss_fun.__str__()}\n"
        return sentence1 + sentence2 + sentence3 + sentence4 + sentence5


    def train_one_epoch(self, hidden, cell):
        """
        training the network for a single epoch
        """
        self.network.train(True)
        running_loss = 0.0
        length = len(self.dataloader)
        # hidden, cell = self.network.init_hidden_state()

        for i, data in enumerate(self.dataloader):
            sample_batch, target_batch = data 
            
            # self.optimizer.zero_grad()
            # output, hidden, cell = self.network(sample_batch)
            # print(output.size())
            print(sample_batch.size())
            print(target_batch.size())

            break


    def train_all_epochs(self):
        """
        training the network all the epochs
        """
        for e in range(self.num_epochs):
            h, c= self.network.init_hidden_state()
            self.train_one_epoch(hidden=h, cell=c)
            break            
        pass 
    
