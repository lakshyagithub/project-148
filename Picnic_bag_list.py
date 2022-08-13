from tkinter import *
import random

root = Tk()
root.geometry("400x400")
root.title("List")
root.configure(background="sky blue")

label1 = Label(root)
label2 = Label(root)

List1 = ["Pen", "ID card", "Chips"]
label1["text"] = "Listed items: " + str(List1)

def randomnumber():
    gift = random.sample(range(0,3),1)
    label2["text"] = "Put item no " + str(gift) + " in bag"

btn = Button(root, text="Which item to put in bag?", command=randomnumber, bg="light green", relief='flat', highlightthickness=0, bd=0)

label1.place(relx=0.5, rely=0.4, anchor=CENTER)
btn.place(bordermode=OUTSIDE, relx=0.5, rely=0.5, anchor=CENTER)
label2.place(relx=0.5, rely=0.6, anchor=CENTER)

root.mainloop()