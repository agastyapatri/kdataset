"""
    Vectorizing the text corpus and defining a torch dataset
"""
import torch 
import numpy as np 
import torch.nn as nn 

class TensorData(torch.utils.data.Dataset):
    """
        Taking in a list of text data and returning a torch dataset 
        ~   text_data = a list of text (words or sentences)
        ~   
    """
    def __init__(self, text_data) -> None:
        super().__init__()
        self.text_data = text_data 
        self.text_tensor = None
        

    def __len__(self) -> int:
        return len(self.text_data)
    
    def __str__(self) -> str:
        heading = f"\nRepresenting Text data as Tensors\n"
        dims = f"\nNumber of Dimensions: "
        batching = f"\nElements per Batch: \n"
        return heading + dims + batching

    def __getitem__(self, i):
        #   temporary         
        return self.text_data[i]

    def text_to_tensor(self, text_data):
        #   cleaning and converting the text corpus into usable data
        pass 

if __name__ == "__main__":
    dataset = TensorData(text_data = None)
    print(dataset)