import numpy as np
import tensorflow as tf
from tensorflow.keras import models,layers
from tensorflow.keras.layers import MultiHeadAttention,LayerNormalization


class decoder:
    
    def __init__(self,num_heads,key_dim):
        model=models.Sequential()
        model.add(layers.Dense(64,activation="relu"))
        model.add(layers.Dense(32))
        self.fnn=model
        self.msa=MultiHeadAttention(num_heads,key_dim)
        self.ln1 = LayerNormalization()
        self.ln2 = LayerNormalization()
    
    def forward(self,x):
        out1=self.msa(query=x,value=x,key=x,use_causal_mask=True)
        x1=self.ln1(x+out1)
        out2=self.fnn(x1)
        x2=self.ln2(x1+out2)
        return x2
    
    
            
        
        
    