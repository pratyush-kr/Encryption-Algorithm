import pandas as pd
import random
import getpass
import tkinter as tk
my_data = ""
#Getting Data from user
window = tk.Tk()
def get_data():
    global data
    data = e1.get()
    window.destroy()
def collect():
    return data
e1 = tk.Entry(window)
e1.grid(row = 0, column = 1)
window.title('Encryptor')

l1 = tk.Label(window,text='Encrypte: ')
l1.grid(row = 0, column = 0)
button = tk.Button(window,text = 'Encrypt', command = get_data)
button.grid(row = 1, column = 1)
window.mainloop()
my_data = collect()

encrypt = ""
file=pd.read_csv('.key-lock.csv')
for i in range(len(my_data)):
    num=ord(my_data[i])
    string="i am "+str(num)
    n=random.randint(1,20)
    encrypt+=str(file[string][n])+'%'
my_file = open(".password.csv",'a')
my_file.write(encrypt+'\n')
window2 = tk.Tk()
label_Encrypt = tk.Label(window2,text='Encrypt Data: ')
label_Encrypt.grid(row = 0, column = 0)
label_Encrypt = tk.Label(window2,text=encrypt)
label_Encrypt.grid(row = 0, column = 1)
window2.mainloop()
