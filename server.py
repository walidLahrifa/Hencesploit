import tkinter as tk
import socket
import threading
from tkinter import *
from tkinter import *
from PIL import ImageTk, Image
from flask_bcrypt import Bcrypt
from flask_pymongo import PyMongo
from flask import Flask

app=Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://127.0.0.1:27017/Hencesploit20'
mongo=PyMongo(app)
projects = mongo.db.Projects
users = mongo.db.users
bcrypt = Bcrypt(app)
window = tk.Tk()
window.title("Hencesploit_Multi_Auditor_Recorder")

# Top frame consisting of two buttons widgets (i.e. btnStart, btnStop)
topFrame = tk.Frame(window)
x = "logoH.png"
img = Image.open(x)
img = img.resize((250, 250), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)
panel = Label(topFrame, image=img)
panel.image = img
panel.pack()
btnStart = tk.Button(topFrame, text="RECORD MY HACKING", command=lambda: start_server())
btnStart.pack(side=tk.LEFT)
btnStop = tk.Button(topFrame, text="STOP RECORD", command=lambda: stop_server(), state=tk.DISABLED)
btnStop.pack(side=tk.LEFT)
topFrame.pack(side=tk.TOP, pady=(5, 0))

# Middle frame consisting of two labels for displaying the host and port info

middleFrame = tk.Frame(window)
lblHost = tk.Label(middleFrame, text="Host: X.X.X.X")
lblHost.pack(side=tk.LEFT)
lblPort = tk.Label(middleFrame, text="Port:XXXX")
lblPort.pack(side=tk.LEFT)
middleFrame.pack(side=tk.TOP, pady=(5, 0))

# The client frame shows the client area
clientFrame = tk.Frame(window)
lblLine = tk.Label(clientFrame, text="*******************AUDITORS LIST*****************").pack()
scrollBar = tk.Scrollbar(clientFrame)
scrollBar.pack(side=tk.RIGHT, fill=tk.Y)
tkDisplay = tk.Text(clientFrame, height=50, width=50)
tkDisplay.pack(side=tk.LEFT, fill=tk.Y, padx=(5, 0))
scrollBar.config(command=tkDisplay.yview)
tkDisplay.config(yscrollcommand=scrollBar.set, background="#5b6e31", highlightbackground="grey", state="disabled")
clientFrame.pack(side=tk.BOTTOM, pady=(5, 16))

server = None
HOST_ADDR = "0.0.0.0"
HOST_PORT = 8080
client_name = " "
clients = []
clients_names = []


# Start server function
def start_server():
    global server, HOST_ADDR, HOST_PORT  # code is fine without this
    btnStart.config(state=tk.DISABLED)
    btnStop.config(state=tk.NORMAL)

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(socket.AF_INET)
    print(socket.SOCK_STREAM)

    server.bind((HOST_ADDR, HOST_PORT))
    server.listen(5)  # server is listening for client connection

    threading._start_new_thread(accept_clients, (server, " "))

    lblHost["text"] = "Host: " + HOST_ADDR
    lblPort["text"] = "Port: " + str(HOST_PORT)


# Stop server function
def stop_server():
    global server
    btnStart.config(state=tk.NORMAL)
    btnStop.config(state=tk.DISABLED)


def accept_clients(the_server, y):
    while True:
        client, addr = the_server.accept()
        clients.append(client)

        # use a thread so as not to clog the gui thread
        threading._start_new_thread(send_receive_client_message, (client, addr))


# Function to receive message from current client AND
# Send that message to other clients
def send_receive_client_message(client_connection, client_ip_addr):
    global server, client_name, clients, clients_addr
    client_msg = " "
    client_name = ""
    # send welcome message to client
    client_name = client_connection.recv(4096)
    modifiedMessage=client_name.decode('utf-8')
    testluck="Welcome " + modifiedMessage + ". Use 'exit' to quit"
    client_connection.send(testluck.encode('utf-8'))
    clients_names.append(modifiedMessage)
    update_client_names_display(clients_names)  # update client names display

    while True:
        data = client_connection.recv(4096)
        if not data: break
        if data == "exit": break

        client_msg = data.decode('utf-8')

        idx = get_client_index(clients, client_connection)
        sending_client_name = clients_names[idx]

        for c in clients:
            if c != client_connection:

                soluted=sending_client_name + "->" + client_msg
                print(sending_client_name)
                print(client_msg)
                c.send((soluted.encode('utf-8')))

    # find the client index then remove from both lists(client name list and connection list)
    idx = get_client_index(clients, client_connection)
    del clients_names[idx]
    del clients[idx]
    bye="BYE!"
    client_connection.send(bye.encode('utf-8'))
    client_connection.close()
    update_client_names_display(clients_names)  # update client names display


# Return the index of the current client in the list of clients
def get_client_index(client_list, curr_client):
    idx = 0
    for conn in client_list:
        if conn == curr_client:
            break
        idx = idx + 1

    return idx


# Update client name display when a new client connects OR
# When a connected client disconnects
def update_client_names_display(name_list):
    tkDisplay.config(state=tk.NORMAL)
    tkDisplay.delete('1.0', tk.END)

    for c in name_list:
        print(name_list)
        print(c)
        tkDisplay.insert(tk.END, c + "\n")
    tkDisplay.config(state=tk.DISABLED)


window.mainloop()
