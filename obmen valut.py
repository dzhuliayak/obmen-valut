import requests
import json
from tkinter import*
from tkinter import messagebox as mb

from bottle import response


def exchange():
    code =entry.get() # код валюты получаем из поля ввода информации
    if code: #делаем проверку, если код введен, то работаем и делаем обработку исключений
        try:
            response=requests.get("https://open.er-api.com/v6/latest/USD")# ответ получим из вопроса с сайта
            response.raise_for_status() #проверяем на ошибки, если ответ 200, то все хорошо, если нет отрабатываем исключения
            data=response.json() #ответ от json
            if code in data["rates"]: #если внутри rates есть код валют, то можно обрабатывать
                exchange_rate=data["rates"][code]# курс обмена из словаря (date rates) выбираем значение по ключу
                mb.showinfo("курс обмена", f"курс: {exchange_rate}{code} за 1 доллар")# выводим окно
            else:
                mb.showerror("ошибка", f"валюта {code} не найдена")
        except Exception as e: # обрабатываем исключения
            mb.showerror("ошибка", f"произошла ошибка: {e}")
    else: # если поле ввода пустое
        mb.showwarning("внимание",f"введите код валюты")


window=Tk()
window.title("курс обмена валют")
window.geometry("360x180")

Label(text="введите код валюты").pack(padx=10, pady=10)

entry=Entry()
entry.pack(padx=10, pady=10)

Button(text="получить курс обмена к доллару",command=exchange).pack(padx=10, pady=10)# кнопка с функцией обмена

window.mainloop()
