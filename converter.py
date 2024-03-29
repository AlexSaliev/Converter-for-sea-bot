import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import pandas as pd
# подключаем gui библиотеку  tkinter  и настраеваем ее
root= tk.Tk()
root.title('Конвертер для Никиты')
canvas1 = tk.Canvas(root, width = 500, height = 300, bg = 'lightsteelblue2', relief = 'raised')
canvas1.pack()
# приветсвенная строка
label1 = tk.Label(root, text='Привет, Никита', bg = 'lightsteelblue2')
label1.config(font=('helvetica', 20))
canvas1.create_window(150, 60, window=label1)
# функция выбора и чтения имени файла в дереве
def getTxt ():
    global read_file
    
    import_file_path = filedialog.askopenfilename()
    # создание записи навзания и пути файла в UI
    label1 = tk.Label(root, text=import_file_path, bg = 'lightsteelblue2')
    canvas1.create_window(150, 160, window=label1)
    read_file = pd.read_csv(import_file_path)
    
browseButtonTxt = tk.Button(text="Выбери файл",width=18, command=getTxt, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 130, window=browseButtonTxt)
# функция смены расширения файла
def convertToCsv ():
    global read_file
    
    export_file_path = filedialog.asksaveasfilename(defaultextension='.csv')
    read_file.to_csv (export_file_path, index = None)
# кнопка сохранения
saveAsButtonCsv = tk.Button(text='Преобразовать в CSV',width=18, command=convertToCsv, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 187, window=saveAsButtonCsv)
# функция закрытия приложения
def exitApplication():
    MsgBox = tk.messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
    if MsgBox == 'yes':
       root.destroy()
# кнопка закрыть приложение     
exitButton = tk.Button (root, width=18, text='Закрыть',command=exitApplication, bg='brown', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 270, window=exitButton)

root.mainloop()
