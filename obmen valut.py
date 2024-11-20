import requests
import json
from tkinter import*
from tkinter import messagebox as mb
from tkinter import ttk

from packaging.utils import canonicalize_name


def update_c_label(event): #функция для обновления метки (которая отображает полную информацию по названию валюты)
    code = combobox.get()#код получим из комбобокса
    name= cur[code] #имя валюты получим из списка cur
    c_label.config(text=name)


def exchange():
    code =combobox.get() # код валюты получаем из поля ввода информации
    if code: #делаем проверку, если код введен, то работаем и делаем обработку исключений
        try:
            response=requests.get("https://open.er-api.com/v6/latest/USD")# ответ получим из вопроса с сайта
            response.raise_for_status() #проверяем на ошибки, если ответ 200, то все хорошо, если нет отрабатываем исключения
            data=response.json() #ответ от json
            if code in data["rates"]: #если внутри rates есть код валют, то можно обрабатывать
                exchange_rate=data["rates"][code]# курс обмена из словаря (date rates) выбираем значение по ключу
                c_name=cur[code]
                mb.showinfo("курс обмена", f"курс: {exchange_rate:.2f}{c_name} за 1 доллар")# выводим окно. .2f означает количество символов после запятой, чтобы отражались лишь сотые (f-это формат)
            else:
                mb.showerror("ошибка", f"валюта {code} не найдена")
        except Exception as e: # обрабатываем исключения
            mb.showerror("ошибка", f"произошла ошибка: {e}")
    else: # если поле ввода пустое
        mb.showwarning("внимание",f"введите код валюты")


cur = {
    "RUB": "российский рубль",
    "EUR": "евро",
    "GBP": "британский фунт стерлингов",
    "JPY": "японская йена",
    "CNY": "китайский юань",
    "KZT": "казахский тенге",
    "UZS": "узбекский сум",
    "CHF": "швейцарский франк",
    "AED": "дирхам ОАЭ",
    "CAD": "канадский доллар"
    } # скобки фигурные, т.к. теперь будет списком отображаться


window=Tk()
window.title("курс обмена валют")
window.geometry("360x180")

Label(text="выберите код валюты").pack(padx=10, pady=10)

combobox=ttk.Combobox(values=list(cur.keys())) # присваиваем комбобоксу значение cur(список), а чтобы из списка сделать словарь присваеваем значение list
combobox.pack(padx=10, pady=10)
combobox.bind("<<comboboxSelected>>", update_c_label)

c_label=ttk.Label()#метка для отображения полной информации по названию валюты
c_label.pack(padx=10, pady=10)

Button(text="получить курс обмена к доллару",command=exchange).pack(padx=10, pady=10)# кнопка с функцией обмена

window.mainloop()
