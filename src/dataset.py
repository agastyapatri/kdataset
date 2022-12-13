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

    def __str__(self) -> str:
        heading = f"\nRepresenting Text data as Tensors\n"
        dims = f"\nNumber of Dimensions: "
        batching = f"\nElements per Batch: \n"
        return heading + dims + batching

    def __len__(self) -> int:
        return len(self.text_data)

    def __getitem__(self, idx):
        # One hot encoding the sentences in the corpus.
        lines = self.text_data
        words = [] 

        for line in lines:
            temp = line.split(" ")
            for word in temp:
                words.append(word)

        vocabulary = list(set(words))

        vector = np.zeros((len(lines), len(vocabulary)), dtype=np.float32)



        """
        Steps needed: 
            1. find vocabulary from the sentences 
            2. do onehot encoding based on the vocabulary for each sentence. 
        """
         

        
        return vector[idx, :]

    
if __name__ == "__main__":
    dataset = TensorData(text_data=["1", "2", "3", "4"])
    print(dataset[1:10])