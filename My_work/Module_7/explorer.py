import tkinter
import os
from tkinter import filedialog


def  file_select():
    filename = filedialog.askopenfilename(initialdir="/", title='Выберите файл',
                                          filetypes=(('Текстовые файлы', ".txt"),('Все файлы', "*")))
    text['text'] = text['text'] + '' + filename
    os.startfile(filename)


window = tkinter.Tk()
window.title('Проводник')
window.geometry('450x150')
window.configure(bg='black')
window.resizable(False,False)
text = tkinter.Label(window, text='Файл:', height=5, width=65, background='silver', foreground='blue')
text.grid( column = 1, row = 1)
button_select = tkinter.Button(window, width=20, height=3, text='Выберите файл', background='silver', foreground='blue',
                               command=file_select)
button_select.grid(column=1, row=2, pady=5)

"""
Попробуйте добавить меню к вашему блокноту с пунктами "info" и "about". В пункте "info" должно быть написано, 
как пользоваться вашим блокнотом, а в пункте "about" — информация об авторе и версии программы. 
Это будет задание для самостоятельной проработки.
Мы пытались объединить графический интерфейс с модулем os, хотя он использовался не так активно, 
так как Tkinter значительно упростил задачу навигации по файловой системе."""

window.mainloop()
