import tkinter as tk
import tkinter.scrolledtext as st
from tkinter import messagebox as mb
from tkinter import filedialog as fl
import os 

filename=''

def message():
    mb.showinfo('相関の情報','部分の関数のコードはインタネットで調べて自分で作ります。')
def author():
    mb.showinfo('制作人員','R20E3011 謝 佩恒')

def myopen():
    global filename

    types = [("テキストファイル", "*.txt")]

    filename=fl.askopenfilename(defaultextension='.txt',filetypes = types)

    if filename=='':
        filename=None
    else:
        root.title('txtのエディタ'+os.path.basename(filename))
        textPad.delete(1.0,tk.END)
        f=open(filename,'r')
        textPad.insert(1.0,f.read())
        f.close()

def new():
    global root,filename,textPad
    root.title('名前のないファイル')
    filename=None
    textPad.delete(1.0,tk.END)

def save():
    global filename
    try:
        f=open(filename,'w')
        msg=textPad.get(1.0,tk.END)
        f.write(msg)
        f.close()
    except:
        namesave()

def namesave():
    types = [("テキストファイル", "*.txt")]
    f=fl.asksaveasfilename(initialfile='名前のないファイル.txt',defaultextension='.txt',filetypes = types)
    global filename
    filename=f

    fh = open(f,'w')
    msg=textPad.get(1.0,tk.END)
    fh.write(msg)
    fh.close()
    root.title('txtのエディタ'+os.path.basename(f))
def cut():
    global textPad
    textPad.event_generate('<<Cut>>')
def copy():
    global textPad
    textPad.event_generate('<<Copy>>')
def paste():
    global textPad
    textPad.event_generate('<<Paste>>')


def undo():
    global textPad
    textPad.event_generate('<<Undo>>')
def redo():
    global textPad
    textPad.event_generate('<<Redo>>')
def selectall():
    global textPad
    textPad.tag_add('sel','1.0','end')

def popup(event):
    global editmenu
    editmenu.tk_popup(event.x_root,event.y_root)

root = tk.Tk()
root.title('R20E3011 謝 佩恒')
root.geometry("700x400")


menubar = tk.Menu(root)
root.config(menu = menubar)


filemenu = tk.Menu(menubar,tearoff=0)
filemenu.add_command(label = '新規作成',command= new)
filemenu.add_command(label = '開く',command= myopen)
filemenu.add_command(label = '保存',command= save)
filemenu.add_command(label = '名前を付けて保存',command= namesave)
menubar.add_cascade(label = 'ファイル',menu = filemenu)

editmenu = tk.Menu(menubar,tearoff=0)
editmenu.add_command(label = '元に戻す',command = undo)
editmenu.add_command(label = 'やり直し',command = redo)
editmenu.add_command(label = 'コピー',command = copy)
editmenu.add_command(label = '切り取り',command = cut)
editmenu.add_command(label = '貼り付け',command = paste)
editmenu.add_separator()
editmenu.add_command(label = 'すべて選択',command = selectall)
menubar.add_cascade(label = '編集',menu = editmenu)

aboutmenu = tk.Menu(menubar,tearoff=0)
aboutmenu.add_command(label = '相関の情報',command = message)
aboutmenu.add_command(label = '制作人員',command = author)
menubar.add_cascade(label = '相関情報',menu = aboutmenu)

textPad = st.ScrolledText(root,undo=True)
textPad.pack(expand=True, fill='both')

root.mainloop()