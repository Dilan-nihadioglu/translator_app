from tkinter import *
from tkinter.ttk import Combobox
import textblob
import googletrans
from tkinter import messagebox,ttk

language=googletrans.LANGUAGES
language_values=list(language.values())
lang1=language.keys()

def Translate():
    second_article.delete(1.0,END)
    words=""
    try:
        for key,value in language.items():
            if value==choice1.get():
                from_language_key=key
        for key,value in language.items():
            if value==choice2.get():
                to_language_key=key
        words=textblob.TextBlob(first_article.get(1.0,END))
        words=words.translate(from_lang=str(from_language_key),to=str(to_language_key))
        second_article.insert(1.0,words)
    except Exception as e:
        messagebox.showerror("translator","error")
        print(e)

def clear():
    first_article.delete(1.0,END)
    second_article.delete(1.0,END)


w=Tk()
w.title("Execute Translation")
w.geometry("850x300+600+150")
w.resizable(False,False)
w.tk_setPalette("#48D1CC")
f=Frame(w)
f.place(relx=0.06,rely=0.2,width=310,height=140)

first_article=Text(bg="white",relief="solid",font=15)
first_article.place(relx=0.05,rely=0.2,width=300,height=140)
sc=Scrollbar(f)
sc.pack(side="right",fill="y")
sc.configure(command=first_article.yview)
first_article.configure(yscrollcommand=sc.set)

translate=Button(text="Translate",bg="pink",fg="black",font="Algerian 15 bold",command=Translate)
translate.place(relx=0.38,rely=0.8)


f2=Frame(w)
f2.place(relx=0.53,rely=0.2,width=310,height=140)

second_article=Text(bg="white",relief="solid",font=15)
second_article.place(relx=0.52,rely=0.2,width=300,height=140)
sc2=Scrollbar(f2)
sc2.pack(side="right",fill="y")
sc2.configure(command=second_article.yview)
second_article.configure(yscrollcommand=sc2.set)
choice1=ttk.Combobox(w,values=language_values)
choice1.place(relx=0.15,rely=0.1)
choice1.set("Choice")
choice2=ttk.Combobox(w,values=language_values)
choice2.place(relx=0.66,rely=0.1)
choice2.set("Choice")

clear_button=Button(text="Clear all",command=clear,bg="pink",fg="black",font="algerian 15 bold")
clear_button.place(relx=0.9,rely=0.0)





mainloop()
