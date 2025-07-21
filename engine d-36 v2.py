from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter.filedialog as fd
import tkinter.messagebox
import os

def close_win(event): #выход
    root.destroy()

def pathes():
        global path_file
        path_file.clear()
        try:
            with open('config.txt', 'r', encoding='utf-8') as file1:  #открытие файла config.txt для чтения
                for line in file1:
                    path_file.append(line.strip().replace('\\','/'))  #strip() - удаляет начальные и конечные пробелы
        except IOError:
            with open('config.txt', 'w', encoding='utf-8') as file1:  #если нет config.txt, то создается
                for line in file1:
                    path_file.append(line.strip().replace('\\','/'))  
        for elem in path_file:
            if elem == '' or elem == '\n':  #удаление лишних пустых строк
                path_file.remove(elem)
        if len(path_file) == 3: #если в списке с путями 3 элемента, то происходит соответствие с переменными, иначе ошибка
            path_model = path_file[0]
            path_lectures = path_file[1]
            path_test = path_file[2]
        else:
            tkinter.messagebox.showwarning(title="Внимание", message='Файл "config.txt" заполнен не полностью!\nПожалуйста, внесите в него 3 пути в следующем порядке: "3D-модель, лекции, тестирование"')
       
def settings():
    global path_file

    def close_settings(event): #закрыть окно настроек
        root.deiconify() #сделать главное окно на первом плане
        root_settings.destroy()
    
    def set_path(event): #сохранение путей, прописанных в полях
        global path_file
        root.deiconify() #сделать главное окно на первом плане
        path_model=entry_model.get()
        path_lectures=entry_lectures.get()
        path_test=entry_test.get()
        path_file.clear()
        path_file.append(path_model)
        path_file.append(path_lectures)
        path_file.append(path_test)
        with open('config.txt', 'w', encoding='utf-8') as txt_file:
            for elem in path_file:
                txt_file.write(elem+'\n')
        root_settings.destroy()

    def choose_path_model(event): #выбор модели
        filetypes=(("Исполнительный файл", "*.exe"),)
        filepath=fd.askopenfilename(title="Открыть 3D-модель", initialdir="/", filetypes=filetypes)
        entry_model.delete(0, END)
        entry_model.insert(1, filepath)

    def choose_path_test(event): #выбор теста
        filetypes=(("Исполнительный файл", "*.exe"),)
        filepath=fd.askopenfilename(title="Открыть тест", initialdir="/", filetypes=filetypes)
        entry_test.delete(0, END)
        entry_test.insert(1, filepath)

    def choose_path_lectures(event): #выбор лекций
        filepath=fd.askdirectory(title="Открыть папку с лекциями")
        entry_lectures.delete(0, END)
        entry_lectures.insert(1, filepath)

    def close_settings_win(): #закрыть окно настроек через системную иконку "закрыть"
        root.deiconify()
        root_settings.destroy()
        
    but_settings_font='courier 12'
    but_settings_width=15
    
    root_settings=Tk()
    root_settings.title('Settings')
    root_settings.resizable(False, False)
    root_settings.iconbitmap('icon.ico') #установка иконки

    fra_settings=Frame(root_settings, width=800, height=300, bg='#f5eca2')
    fra_settings.grid(row=0,column=0)

    entry_model=Entry(fra_settings, font=but_font, width = 60)
    entry_model.place(x = 20, y = 40)
    lab_model=Label(fra_settings, bg = '#f5eca2', text = "3D-модель:", font = but_settings_font, justify = LEFT)
    lab_model.place(x = 20, y = 10)
    but_choose_model=Button(fra_settings, text="Выбрать", font=but_settings_font, bg=color_for_button)
    but_choose_model.place(x=700, y=38)
    but_choose_model.bind("<Button-1>", choose_path_model)

    entry_lectures=Entry(fra_settings, font=but_font, width = 60)
    entry_lectures.place(x = 20, y = 110)
    lab_lectures=Label(fra_settings, bg = '#f5eca2', text = "Лекции:", font = but_settings_font, justify = LEFT)
    lab_lectures.place(x = 20, y = 80)
    but_choose_lectures=Button(fra_settings, text="Выбрать", font=but_settings_font, bg=color_for_button)
    but_choose_lectures.place(x=700, y=108)
    but_choose_lectures.bind("<Button-1>", choose_path_lectures)

    entry_test=Entry(fra_settings, font=but_font, width = 60)
    entry_test.place(x = 20, y = 180)
    lab_test=Label(fra_settings, bg = '#f5eca2', text = "Тест:", font = but_settings_font, justify = LEFT)
    lab_test.place(x = 20, y = 150)
    but_choose_test=Button(fra_settings, text="Выбрать", font=but_settings_font, bg=color_for_button)
    but_choose_test.place(x=700, y=178)
    but_choose_test.bind("<Button-1>", choose_path_test)

    but_save=Button(fra_settings, text="Сохранить", width=but_settings_width, font=but_font, bg=color_for_button)
    but_save.place(x=210, y=240)
    but_save.bind("<Button-1>", set_path)
    but_cancel=Button(fra_settings, text="Отмена", width=but_settings_width, font=but_font, bg=color_for_button)
    but_cancel.place(x=410, y=240)    
    but_cancel.bind("<Button-1>", close_settings)

    root_settings.protocol("WM_DELETE_WINDOW", close_settings_win) #закрытие окна настроек через системный выход

    pathes()
    entry_model.insert(1, path_file[0])
    entry_lectures.insert(1, path_file[1])
    entry_test.insert(1, path_file[2])
            
def inst(): #чтение файла инструкции программы
    if os.path.exists('inst.txt')==True:
        f=open('inst.txt', 'r', encoding='utf-8')
        readd=f.read()
        f.close()
        tkinter.messagebox.showinfo(title="Инструкция", message=readd)
    else:
        tkinter.messagebox.showerror(title="Ошибка", message='Файл "inst.txt" не обнаружен')

def info(): #чтение файла "О программе"
    if os.path.exists('info.txt')==True:
        f=open('info.txt', 'r', encoding='utf-8')
        readd=f.read()
        f.close()
        tkinter.messagebox.showinfo(title="О программе", message=readd)
    else:
        tkinter.messagebox.showerror(title="Ошибка", message='Файл "info.txt" не обнаружен')

def author(): #чтение файла "Об авторе"
    if os.path.exists('author.txt')==True:
        f=open('author.txt', 'r', encoding='utf-8')
        readd=f.read()
        f.close()
        tkinter.messagebox.showinfo(title="Об авторе", message=readd)
    else:
        tkinter.messagebox.showerror(title="Ошибка", message='Файл "author.txt" не обнаружен')

def choose_model(event): #запуск модели
    global path_file
    pathes()
    try:
        name='model.exe'
        if name in path_file[0]:
            if path_file[0] != '':
                os.startfile(path_file[0])
        else:
            tkinter.messagebox.showerror(title="Ошибка", message='Файл модели должен иметь название ' + name)
    except FileNotFoundError:
        tkinter.messagebox.showerror(title="Ошибка", message='Файл не найден!')

def choose_test(event): #запуск теста
    global path_file
    pathes()
    try:
        if 'test.exe' in path_file[2]:
            if path_file[2] != '':
                os.startfile(path_file[2])
        else:
            tkinter.messagebox.showerror(title="Ошибка", message='Файл теста должен иметь название' + name)
    except FileNotFoundError:
        tkinter.messagebox.showerror(title="Ошибка", message='Файл не найден!')
        
def choose_lectures(event): #запуск теста
    global path_file, click
    pathes()
    try:
        def print_hide(click): #функция скрывает/показывает img/listbox
            if click%2 == 0:
                panel_lectures.place_forget()   #скрыть картинку
                listbox.place(x=325, y=40)   #показать список лекций
            else:
                panel_lectures.place(x=325, y=40)   #показать картинку
                listbox.place_forget()   #скрыть список лекций

        click+=1
        list_files=[]
        def items_selected(event):  #функция для открытия выбранного файла
            selected_indices=listbox.curselection()  #индекс выбранного файла
            selected_file=",".join([listbox.get(i) for i in selected_indices]) #выбранный файл
            if '/' in path_file[1]:
                os.startfile(path_file[1]+'/'+selected_file) #открытие выбранного файла
            else:
                tkinter.messagebox.showerror(title="Ошибка!", message="Файл не найден! Укажите абсолютный путь к каталогу с лекциями\nНапример: 'C:\Новая папка\Лекции по двигателю'\nВыбрать папку с лекциями можно через Меню-Управление учебным материалом" )
        
        def files(path): #функция для получения файлов с каталога
            for file in os.listdir(path):
                if os.path.isfile(os.path.join(path, file)):
                    yield file
                            
        for file in files(path_file[1]):  #добавление файлов в список
                list_files.append(file)
                        
        files_var=StringVar(value=list_files)
        listbox=Listbox(fra, listvariable=files_var, height=31, width=56, selectmode='single')
        listbox.place(x=325, y=40)
        listbox.bind('<<ListboxSelect>>', items_selected)
        print_hide(click)   
    except FileNotFoundError:
        tkinter.messagebox.showerror(title="Ошибка", message='Файл не найден!')
    
root=Tk()
root.title('Engine D-36')
root.resizable(False, False)
root.iconbitmap('icon.ico') #установка иконки

fra=Frame(root, width=1000, height=650, bg='#f5eca2')
fra.grid(row=0,column=0)

but_width=21
but_font='courier 14'
color_for_button='#FFF380' #цвет для кнопок
click=1 #счетчик нажатия на кнопку "Лекции"
path_file=[]

mainmenu=Menu(root) 
root.config(menu=mainmenu)

filemenu=Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Управление учебным материалом", command=settings)
filemenu.add_separator()
filemenu.add_command(label="Выход", command=lambda:root.destroy())

helpmenu=Menu(mainmenu, tearoff=0)
helpmenu.add_command(label="Инструкция", command=inst)
helpmenu.add_command(label="О программе", command=info)
helpmenu.add_command(label="Об авторе", command=author)

mainmenu.add_cascade(label="Меню", menu=filemenu)
mainmenu.add_cascade(label="Справка", menu=helpmenu)

panel_model = Label(root)
panel_model.place(x=40, y=40)
but_model=Button(fra, text="3D-модель", width=but_width, font=but_font, bg=color_for_button)
but_model.place(x=42, y=544)
but_model.bind("<Button-1>", choose_model)

panel_lectures = Label(root)
panel_lectures.place(x=325, y=40)
but_lectures=Button(fra, text="Лекции", width=but_width + 9, font=but_font, bg=color_for_button)
but_lectures.place(x=325, y=544)
but_lectures.bind("<Button-1>", choose_lectures)

panel_test = Label(root)
panel_test.place(x=715, y=40)
but_test=Button(fra, text="Тестирование", width=but_width, font=but_font, bg=color_for_button)
but_test.place(x=715, y=544)
but_test.bind("<Button-1>", choose_test)

if os.path.exists("model.jpg")==True and os.path.exists("lectures.jpg")==True and os.path.exists("test.jpg")==True:            
    path1 = "model.jpg"
    path2 = "lectures.jpg"
    path3 = "test.jpg"
    
    img_model = ImageTk.PhotoImage(Image.open(path1))
    img_lectures = ImageTk.PhotoImage(Image.open(path2))
    img_test = ImageTk.PhotoImage(Image.open(path3))

    panel_model["image"] = img_model
    panel_lectures["image"] = img_lectures
    panel_test["image"] = img_test

    panel_model["width"] = 238
    panel_lectures["width"] = 338
    panel_test["width"] = 238

    panel_model["height"] = 500
    panel_lectures["height"] = 500
    panel_test["height"] = 500
else:
    panel_model["bg"] = '#bfb984'
    panel_lectures["bg"] = '#bfb984'
    panel_test["bg"] = '#bfb984'

    panel_model["width"] = 34
    panel_lectures["width"] = 48
    panel_test["width"] = 34

    panel_model["height"] = 33
    panel_lectures["height"] = 33
    panel_test["height"] = 33
    
root.mainloop()
