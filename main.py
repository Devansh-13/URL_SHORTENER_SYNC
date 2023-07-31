import pyshorteners
from tkinter import *


def shortener():
    url_entry = url.get()
    result = pyshorteners.Shortener().tinyurl.short(url_entry)
    urlEntry.insert(END,result)


window = Tk()
window.title("URL-Shortener")
window.geometry("800x300")
window.configure(bg="powder blue")

Label(window,text="Generate Short URL", font=("Times new roman",25,"bold"),fg="red", bg="powder blue").pack(pady=10)

frame1 = Frame(window)
Label(frame1, text="Paste URL Here: ", font=("Arial",15,"bold"), bg="powder blue").pack(side="left")
url = Entry(frame1, width=40, font=("arial",15))
url.pack()
frame1.pack(pady=10)

Button(window, text="Generate Link", font=("arial", 15, "bold"),command=shortener).pack(pady=10)

frame2 = Frame(window)
Label(frame2, text="Copy URL: ", font=("arial",15,"bold"),bg="powder blue").pack(side="left")
urlEntry = Entry(frame2, width="25", fg="blue", font=("arial",15))
urlEntry.pack()
frame2.pack(pady=10)


window.mainloop()
