from tkinter import *

def btn_click():
    mark = 0
    
#Питання №1
    if v1.get() == 1 and v2.get() == 1 and v3.get() == 0 and v4.get() == 0:
        mark += 2
    elif v1.get() == 1 and v2.get() == 0 and v3.get() == 0 and v4.get() == 0:
        mark += 1
    elif v1.get() == 0 and v2.get() == 1 and v3.get() == 0 and v4.get() == 0:
        mark += 1

#Питання №2
    if v5.get() == 1:
        mark += 2

#Питання №3
    selected_answer3 = cb.get()
    correct_answer3 = "База даних"
    if selected_answer3 == correct_answer3:
        mark += 2
        
#Питання №4 
    if listbox.curselection()[0] == 1:
        mark += 2

#Питання №5
    if entry.get() == "Шифрування":
        mark += 2
#Питання №6
    if scale6.get() == 30:
        mark += 2
        
#Відповідь
    if mark > 6:
        lbl5["fg"] = "green"
    else:
        lbl5["fg"] = "red"
    v6.set("Ваша оцінка: "+str(mark))

tk = Tk()
tk.title("Переклад слів")
#шрифти, розмір тексту
font_title = ("Arial", 14, "bold")
font_q = ("Arial", 12, "bold")

#ПИТАННЯ №1(прапорці(декілька правильних відповідей))
lbl1 = Label(tk, text="Питанння №1", font=font_title)
lbl2 = Label(tk, text="Як перекласти слово *file* на українську мову?", font=font_q)
v1 = IntVar()
v2 = IntVar()
v3 = IntVar()
v4 = IntVar()
chb1 = Checkbutton(tk, text="Файл", variable=v1, onvalue=1, offvalue=0)
chb2 = Checkbutton(tk, text="Документ", variable=v2, onvalue=1, offvalue=0)
chb3 = Checkbutton(tk, text="Текст", variable=v3, onvalue=1, offvalue=0)
chb4 = Checkbutton(tk, text="Папка",variable=v4, onvalue=1, offvalue=0)

#ПИТАННЯ №2(одна правильна відповідь)
lbl3 = Label(tk, text="Питанння №2", font=font_title)
lbl4 = Label(tk, text="Як перекласти слово *algorithm* на українську мову?", font=font_q)
v5 = IntVar()
rbt1 = Radiobutton(tk, text="Алгоритм", variable=v5, value=1)
rbt2 = Radiobutton(tk, text="Астрономія", variable=v5, value=2)
rbt3 = Radiobutton(tk, text="Атом", variable=v5, value=3)
rbt4 = Radiobutton(tk, text="Алгоритми", variable=v5, value=4)

#ПИТАННЯ №3(одна правильна відповідь з списку)
from tkinter.ttk import Combobox
lbl6 = Label(tk, text="Питання №3", font=font_title)
lbl7 = Label(tk, text="Як перекласти слово *database* на українську мову?", font=font_q)
answers3 = ["Комп'ютер", "Вебсайт", "База даних"]
cb = Combobox(tk, values=answers3)

# ПИТАННЯ №4(одна правильна відповідь з списку Listbox)
lbl8 = Label(tk, text="Питання №4", font=font_title)
lbl9 = Label(tk, text="Як перекласти слово *debugging* на українську мову?", font=font_q)
answers4 = ["Відновлення", "Виправлення помилок", "Відпочинок", "Відладка"]
listbox = Listbox(tk, selectmode = SINGLE, width=30, height=4)
for i in answers4:
    listbox.insert(END, i)

#ПИТАННЯ №5(введення слова)

lbl12 = Label(tk, text="Питання №5", font=font_title)
lbl13 = Label(tk, text="Як перекласти слово *encryption* на українську мову?", font=font_q)
entry = Entry(tk, width = 30)


#ПИТАННЯ №6(scale)
lbl10 = Label(tk, text="Питання №6", font=font_title)
lbl11 = Label(tk, text="Скільки існує часів в англійській мові?", font=font_q)
scale6 = Scale(tk, from_=1, to=30, orient=HORIZONTAL)

#кнопка, щоб порахувати оцінку
btn = Button(tk, text="Відповісти", command=btn_click)
#щоб оцінка виводилась в тк
v6 = StringVar()
lbl5 = Label(tk, text='', textvariable=v6) 
#щоб вивелось на екрані все, що раніше прописали
lbl1.pack()
lbl2.pack()
chb1.pack()
chb2.pack()
chb3.pack()
chb4.pack()
lbl3.pack()
lbl4.pack()
rbt1.pack()
rbt2.pack()
rbt3.pack()
rbt4.pack()
lbl6.pack()
lbl7.pack()
cb.pack()
lbl8.pack()
lbl9.pack()
listbox.pack()
lbl12.pack()
lbl13.pack()
entry.pack()
lbl10.pack()
lbl11.pack()
scale6.pack()
btn.pack()
lbl5.pack()
tk.mainloop()

