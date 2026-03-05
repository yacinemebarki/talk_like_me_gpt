import os,shutil

path="message/your_instagram_activity/messages/inbox"
target="data"

dirc=os.listdir(path)
print(dirc)

for dir in dirc:
    sub_path=os.path.join(path,dir)
    
    if os.path.isdir(sub_path):
        file=os.listdir(sub_path)
       
        for f in file:
            
            src_file=os.path.join(sub_path,f)
            new_name=dir+"_"+f
            des=os.path.join(target,new_name)
            print(des)
            if os.path.isfile(src_file) and not(os.path.exists(des)):
                shutil.move(src_file,des)
                