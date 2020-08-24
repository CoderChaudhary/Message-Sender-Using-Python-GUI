import requests
import json
from tkinter import *
from tkinter.messagebox import showinfo, showerror


# I am Using FAST2SMS (fast2sms.com)
# Replace this[Your-API-Key] with your API-KEY.
api_key = 'Your-API-Key'

def send_sms(number,message):
    url = 'https://www.fast2sms.com/dev/bulk'
    Paramters = {
        'authorization' : api_key,
        'sender_id' : 'FSTSMS',
        'language' : 'english',
        'route' : 'p',
        'message' : message,
        'numbers' : number,
    }
    response = requests.get(url, params = Paramters)
    res = response.json()
    print(res)
    return res.get('return')

# Creating GUI for Message Sender.

def click_send_sms():
    number = phoneNo.get()
    msgs = msg.get("1.0", END)
    r = send_sms(number, msgs)
    if r:
        showinfo("Send Success", "Successfully sent")
    else:
        showerror("Error", "Something went wrong..")


root = Tk()
root.title("Message Sender - By Gaurav Chaudhary")
root.geometry("400x650")
root.minsize(280,635)
Label(root, text="Message Sender", font="comicsansms 25 bold", relief = RAISED).pack()

phoneNumber = Label(root, text="To: ", font="Helvetica 15 bold")
phoneNumber.pack(anchor = "nw")

phoneNo = Entry(root, font="Helvetica 15")
phoneNo.pack(fill=X, pady=7)

msg_label = Label(root, text="Type Message: ", font="Helvetica 15 bold")
msg_label.pack(anchor = "nw")

msg = Text(root, font="Helvetica 12")
msg.pack(fill=X, pady=7)

btn = Button(root, text="Send SMS", command=click_send_sms, bg="blue", fg="white", font="Helvetica 15 bold")
btn.pack()
root.mainloop()
