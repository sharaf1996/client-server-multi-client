from socket import * 
from _thread import *
from tkinter import *


s = socket((AF_INET) , SOCK_STREAM) 

host = "127.0.0.1"
port = 2039

s.bind((host , port))

s.listen(5) 

root = Tk();
root.title("Server chat")
root.geometry("350x150")

L1 = Label(root , fg = 'red')
L1.grid(row =4 , column=2)


entry = Entry(root ,width = '30')
entry.grid(row =2 , column =2)


sessions = []

def Clicked():
	message = "Server : " + entry.get()
	for c in sessions:
		c.send(message.encode('utf-8'))
	entry.delete(0 , END)

btn = Button(root , text = "Send" , bg ="green" , fg = "black" , width =4 , height =1 , command=Clicked)
btn.grid(row=2 , column=9)


def recvThread(c,ad):
	while True:
		L1["text"]= str(ad[1]) +" : " + c.recv(1024).decode('utf-8')
		
def mainTread(s):
	while True:
		c , ad = s.accept()
		sessions.append(c)

		L1["text"] = "Session # "+ str(ad[1])
		start_new_thread(recvThread , (c,ad))
start_new_thread(mainTread , (s,))

root.mainloop()
