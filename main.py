from tkinter import *
from tkinter import ttk

from method import Mytranslator

app= Tk()
app.geometry('400x520')
app.title('Google Translate mady by Somnath')
app.resizable(0,0)
app.config(bg='green')
app.wm_iconbitmap('google.ico')


def get():
    s= srcLangs.get()
    d= destLangs.get()
    message= sourceText.get(1.0,END)
    translator= Mytranslator()
    text= translator.run(txt=message,src=s,dest=d)
    destText.delete(1.0,END)
    destText.insert(END,text)


appName= Label(app,
               text='Google Translate',
               font=('arial',22),
               bg='blue',
               fg='goldenrod1',
               height=2)
appName.pack(side=TOP,fill=BOTH,pady=0)


frame= Frame(app).pack(side=BOTTOM)
sourceText = Text(frame,font=('arial',10),height=11,wrap=WORD)
sourceText.pack(side=TOP,padx=5,pady=5)

transBtn= Button(text='Translate',
                 font=('arial',10,'bold'),
                 fg='yellow',
                 bg='green',
                 activebackground='blue',relief=GROOVE,command=get)
transBtn.pack(side=TOP,pady=15)

langs=Mytranslator().langs

srcLangs= ttk.Combobox(frame,value=langs,width=10)
srcLangs.place(x=30,y=280)
srcLangs.set('english')

destLangs= ttk.Combobox(frame,value=langs,width=10)
destLangs.place(x=280,y=280)
destLangs.set('bengali')

destText= Text(frame,font=('arial',10),height=11,wrap=WORD)
destText.pack(side=TOP,padx=5,pady=5)


app.mainloop()
