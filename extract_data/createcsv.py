import pandas as pd 
import json
import os
import csv


def extract(message_file,data_file):
    
    with open(message_file,"r") as f:
        data=json.load(f)
    
    participent=data["participants"]
    if len(participent)>2:
        return
    
    message=data["messages"]

    with open(data_file,"a",newline="") as f:
        writer=csv.writer(f)
        
        if os.path.getsize(data_file)==0:
            writer.writerow(["content"])
            
        
        
        a=[]
        for m in message:
            
            if "content" not in m:
                continue
            a.append(m["content"])
            writer.writerow([m["content"]])
            
            
path="data"
target_file="data/message.csv"
file=os.listdir("data")
out=[]
for f in file:
    if f!="message.csv":
        
        fpath=os.path.join(path,f)
        print(fpath)
        extract(fpath,target_file)
        
                       
                
                
            
            
            
             
                
                     
                
        
        
        
        
              