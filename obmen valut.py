import requests
import json
from tkinter import*
from tkinter import messagebox as mb




window=Tk()
window.title("курс обмена валют")
window.geometry("360x180")


Label(text="введите код валюты").pack(padx=10, pady=10)

entry=Entry()
entry.pack(padx=10, pady=10)

Button(text="получить курс обмена к доллару",command=exchange).pack(padx=10, pady=10)# кнопка с функцией обмена


window.mainloop()




