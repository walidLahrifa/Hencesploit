import tkinter as tk
from tkinter import messagebox
import socket
import threading
from tkinter import *
from tkinter import *
from PIL import ImageTk, Image
import os
window = tk.Tk()
window.title("Hencesploit_Multi_Auditor_Recorder")
username = " "
topFrame = tk.Frame(window)
initial = []
p = '/'
flux = os.getcwd().split('/')
for i in range(0, len(flux)):
    if flux[i] == 'Hencesploit2.0.2020':
        m = i
        for x in range(1, m + 1):
            initial = initial + [flux[x]]
        dope = p.join(initial)
        iq = '/' + dope + "/core/adit/logoH.png"
x = iq
img = Image.open(x)
img = img.resize((150,150), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)
panel = Label(topFrame, image=img)
panel.image = img
panel.pack()
lblName = tk.Label(topFrame, text = "Name:").pack(side=tk.LEFT)
entName = tk.Entry(topFrame)
entName.pack(side=tk.LEFT)
btnConnect = tk.Button(topFrame, text="connect", command=lambda: connect())
btnConnect.pack(side=tk.LEFT)
topFrame.pack(side=tk.TOP)

displayFrame = tk.Frame(window)
lblLine = tk.Label(displayFrame, text="Dear Auditor welcome to the multi_auditor mode : In this window you'll be able to see your collaborators output and they can see yours "
                                      "in order to connect enter a nickname or your real name ! ").pack()
scrollBar = tk.Scrollbar(displayFrame)
scrollBar.pack(side=tk.RIGHT, fill=tk.Y)
tkDisplay = tk.Text(displayFrame, height=25, width=150)
tkDisplay.pack(side=tk.LEFT, fill=tk.Y, padx=(5, 0))
tkDisplay.tag_config("tag_your_message", foreground="white")
scrollBar.config(command=tkDisplay.yview)
tkDisplay.config(yscrollcommand=scrollBar.set, background="#5b6e31", highlightbackground="grey", state="disabled")
displayFrame.pack(side=tk.TOP)


bottomFrame = tk.Frame(window)
tkMessage = tk.Text(bottomFrame, height=30, width=55)
tkMessage.pack(side=tk.LEFT, padx=(5, 13), pady=(5, 10))
tkMessage.config(background="#c0b7ff",highlightbackground="grey", state="disabled")
tkMessage.bind("<Return>", (lambda event: getChatMessage(tkMessage.get("1.0", tk.END))))
bottomFrame.pack(side=tk.BOTTOM)


def connect():
    global username, client
    print(entName.get())
    if len(entName.get()) < 1:
        tk.messagebox.showerror(title="ERROR!!!", message="You MUST enter your first name <e.g. John>")
    else:
        username = entName.get()
        print(type(username))
        connect_to_server(username)


# network client
client = None
HOST_ADDR = "0.0.0.0"
HOST_PORT = 8080

def connect_to_server(name):
        global client, HOST_PORT, HOST_ADDR
    #try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((HOST_ADDR, HOST_PORT))
        client.sendto(name.encode('utf-8'), (HOST_ADDR, HOST_PORT)) # Send name to server after connecting

        entName.config(state=tk.DISABLED)
        btnConnect.config(state=tk.DISABLED)
        tkMessage.config(state=tk.NORMAL)

        # start a thread to keep receiving message from server
        # do not block the main thread :)
        threading._start_new_thread(receive_message_from_server, (client, "m"))
    #except Exception as e:
        #tk.messagebox.showerror(title="ERROR!!!", message="Cannot connect to host: " + HOST_ADDR + " on port: " + str(HOST_PORT) + " Server may be Unavailable. Try again later")


def receive_message_from_server(sck, m):
    while True:
        from_server = sck.recv(4096)
        message_decoded=from_server.decode('utf-8')
        if not from_server: break

        # display message from server on the chat window

        # enable the display area and insert the text and then disable.
        # why? Apparently, tkinter does not allow us insert into a disabled Text widget :(
        texts = tkDisplay.get("1.0", tk.END).strip()
        tkDisplay.config(state=tk.NORMAL)
        if len(texts) < 1:
            tkDisplay.insert(tk.END, message_decoded)
        else:
            tkDisplay.insert(tk.END, "\n\n"+ message_decoded)

        tkDisplay.config(state=tk.DISABLED)
        tkDisplay.see(tk.END)

        # print("Server says: " +from_server)

    sck.close()
    window.destroy()

def getChatMessage(msg):
        msg = msg.replace('\n', '')
        texts = tkDisplay.get("1.0", tk.END).strip()

        # enable the display area and insert the text and then disable.
        # why? Apparently, tkinter does not allow use insert into a disabled Text widget :(
        tkDisplay.config(state=tk.NORMAL)
        if len(texts) < 1:
            tkDisplay.insert(tk.END, "You->" + msg, "tag_your_message")  # no line
        else:
            tkDisplay.insert(tk.END, "\n\n" + "You->" + msg, "tag_your_message")

        tkDisplay.config(state=tk.DISABLED)

        send_mssage_to_server(msg)

        tkDisplay.see(tk.END)
        tkMessage.delete('1.0', tk.END)


def send_mssage_to_server(msg):
    client.send(msg.encode('utf-8'))
    if msg == "exit":
        client.close()
        window.destroy()
    print("Sending message")


window.mainloop()