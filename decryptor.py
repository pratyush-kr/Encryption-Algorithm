import pandas as pd
import numpy as np
def decryptor(n):
    for num in range(33,126):
        string="i am "+str(num)
        arr=np.array(file[string])
        mid=int(arr.shape[0]/2)
        end=arr.shape[0]-1
        if (arr[0]==n or arr[end]==n):
            return num
        elif(arr[mid]==n):
            return num
        elif(arr[mid]>n):
            for i in range(1,mid):
                if(arr[i]==n):
                    return num
        elif(arr[mid]<n):
            for i in range(mid,end):
                if(arr[i]==n):
                    return num
file = pd.read_csv('.key-lock.csv')
st=input('Enter encrypt: ')
inum=""
decrypt=""
for i in range(len(st)):
    if(st[i]!='%'):
        inum+=st[i]
    if((i+1)%7==0):
        num=int(inum)
        inum=""
        decrypt+=chr(decryptor(num))
print("Decrypted: "+decrypt)
