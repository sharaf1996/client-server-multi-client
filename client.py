from socket import *
from _thread import *
from tkinter import *


s = socket((AF_INET) , SOCK_STREAM)


host = "127.0.0.1"
port = 2039
s.connect((host , port))

root = Tk();
root.title("Server chat")
root.geometry("350x150")

L1 = Label(root , fg = 'red')
L1.grid(row =4 , column=2)


entry = Entry(root ,width = '30')
entry.grid(row =2 , column =2)



def Clicked():
	message = entry.get()
	s.send(message.encode('utf-8'))
	entry.delete(0 , END)

btn = Button(root , text = "Send" , bg ="green" , fg = "black" , width =4 , height =1 , command=Clicked)
btn.grid(row=2 , column=9)



def recvThread(s):
	while True:
		L1["text"] = s.recv(1204).decode('utf-8')
        

start_new_thread(recvThread , (s,))

root.mainloop();