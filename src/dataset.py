"""
    Vectorizing the text corpus and defining a torch dataset
"""
import torch 
import numpy as np 
import torch.nn as nn 

class TensorData(torch.utils.data.Dataset):
    """
        Taking in a list of text data and returning a torch dataset 
        
    """
    def __init__(self, words, vocab) -> None:
        super().__init__()
        self.words = words 
        self.vocabulary = vocab

    def __str__(self) -> str:
        heading = f"\nRepresenting Text data as Tensors\n"
        dims = f"\nNumber of Dimensions: "
        batching = f"\nElements per Batch: \n"
        return heading + dims + batching

    def __len__(self) -> int:
        return len(self.words)

    def __getitem__(self, idx):
        # One hot encoding the sentences in the corpus.
        word_to_idx = {word: idx for idx, word in enumerate(set(self.words))}
        
        one_hot = np.zeros((len(self.words), len(self.vocabulary)))

        for i, word in enumerate(self.words):
            one_hot[i, word_to_idx[word]] = 1
        one_hot = torch.tensor(one_hot, dtype=torch.float32)
        return one_hot[idx, :]
    
if __name__ == "__main__":
    print("native file")

    