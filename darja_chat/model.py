import numpy as np
import tensorflow as tf
from decoder import decoder
from tensorflow.keras.layers import Dense,Embedding


    

class model:
    
    def __init__(self,n_encoder,input_size,num_heads,key_dim,n_token):
        self.input_size=input_size
        self.layers=[]
        self.dense=Dense(n_token,activation="softmax")
        self.emb=Embedding(input_dim=n_token,output_dim=64,input_length=32)
        self.optimizer = tf.keras.optimizers.Adam(0.01)
        for _ in n_encoder:
            self.layers.append(decoder(num_heads,key_dim))
        
        
    def fit(self,x,y,epoch):
        n_sample=len(x)
        for ep in epoch:
            for i in range(n_sample):
                a=x[i]
                with tf.GradientTape() as tape:
                    a=self.emb(a)
                    for l in self.layers:
                        a=l.forward(a)
                    out=self.dense(a)
                    loss=tf.reduce_mean((out-y[i])**2)
                
                variables=self.dense.trainable_variables
                
                for l in reversed(self.layers):
                    variables += l.fnn.trainable_variables
                    variables += l.msa.trainable_variables
                    variables += [l.ln1.gamma, l.ln1.beta, l.ln2.gamma, l.ln2.beta]
                variables += self.emb.trainable_variables
                
                grads = tape.gradient(loss, variables)
                self.optimizer.appy_gradients(zip(grads,variables))
                   
                        
                        
                        
                        
                
                
            