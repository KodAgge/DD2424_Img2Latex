import torch
import torch.nn as nn
from torch.utils.data import DataLoader
import torch.optim as optim
from matplotlib import pyplot as plt

from CNN import Net as CNN
from paper_LSTM import paper_LSTM_Module
from AttentionMechanism import AttentionMechanism

import sys
sys.path.insert(0, '..\data')
from CROHME_Datasets import CROHME_Training_Set



class EncoderDecoder(nn.Module):

    def __init__(self, input_size, hidden_size, batch_size):
        super().__init__()


        # Network Architecture
        self.CNN = CNN()
        self.LSTM_module = paper_LSTM_Module(input_size, hidden_size, batch_size)
        self.AttentionMechanism = None

        # ... rest of layers

    def init_parameters(self):
        """Function to initialize parameters that are NOT initialized in the modules (which should take care of themselves"""
        pass

    def forward(self, X_batch): 
        # CNN & "Cube Creation"

        # LSTM 

        # Attention

        # The Rest

        pass




def main():
    train_set = CROHME_Training_Set()

    #image = train_set[0]['image']
    #label = train_set[0]['label']
    #plt.imshow(image.permute(1, 2, 0), cmap='gray')
    #plt.show()
    
    embedding_size = 80; # number of rows in the E-matrix
    o_size = 100;  # size of o-vektorn
    input_size = embedding_size + o_size
    hidden_size = 512; 

    batch_size = 20; num_epochs = 1

    train_loader = DataLoader(train_set, batch_size=batch_size, shuffle=True)
    ED = EncoderDecoder(input_size=input_size, hidden_size=hidden_size, batch_size=batch_size)


    n_batches = len(train_loader)
    print(n_batches)
    print(len(train_set))
    for epoch in range(num_epochs):
        for (i, batch) in enumerate(train_loader):
            images = batch['image'] # [batch_size, height, width]
            labels = batch['label']
            #print(images)
            #print(labels)
            print(images.shape)
            print(len(labels))

            # Forward-pass


            # Backward-pass and gradient descent


            input('---BATCH IS OVER---')

if __name__=='__main__':
    main()
    
