#!/usr/bin/env python
# coding: utf-8

# In[4]:


import AudioWorks as aw
import AES_Encrypt


print("Enter the name of the file: ")
file_name = input()
audioData = aw.getAudioData(file_name)

while(1):
    print("Choose:")
    print("1) Encrypt\n2) Decrypt\n3) Exit\n")
    n= int(input())

    if n==1:
        AES_Encrypt.enc.encrypt_file(audioData[6])
        print("The file has been Encrypted!!\n")
        
    elif n==2:
        AES_Encrypt.enc.decrypt_file(audioData[6]+'.enc')
        print("File is decrypted!!\n")
    elif n==3:
        break
    else:
        print("Invalid Input!\nEnter again\n")


# In[ ]:




