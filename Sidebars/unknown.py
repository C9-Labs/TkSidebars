#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 6.2
#  in conjunction with Tcl version 8.6
#    Sep 14, 2021 08:22:41 PM IST  platform: Windows NT

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import unknown_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    unknown_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    unknown_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("606x414+312+181")
        top.minsize(120, 1)
        top.maxsize(1370, 729)
        top.resizable(1,  1)
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=-0.017, rely=-0.024, relheight=1.036
                , relwidth=0.137)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#000000")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.253, rely=0.068, height=20, width=53)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(anchor='sw')
        self.Label1.configure(background="#000000")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#ec7bf2")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Home''')

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.253, rely=0.156, height=21, width=53)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(anchor='sw')
        self.Label2.configure(background="#000000")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#ffffff")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Settings''')

        self.Label3 = tk.Label(self.Frame1)
        self.Label3.place(relx=0.265, rely=0.254, height=13, width=58)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(anchor='sw')
        self.Label3.configure(background="#000000")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#ffffff")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''Help''')

        self.Label4 = tk.Label(self.Frame1)
        self.Label4.place(relx=0.253, rely=0.312, height=21, width=54)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(anchor='sw')
        self.Label4.configure(background="#000000")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#ffffff")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''About''')

        self.Label5 = tk.Label(self.Frame1)
        self.Label5.place(relx=0.0, rely=0.914, height=20, width=89)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(background="#690f96")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(text='''v1.0''')

        self.menubar = tk.Menu(top,font="TkMenuFont",bg='#8000ff',fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.menubar.add_command(
                label="Home")
        self.menubar.add_command(
                activebackground="#000000",
                activeforeground="#000000",
                background="#000000",
                font="-family {Segoe UI} -size 9",
                foreground="#ffffff",
                label="Settings")
        self.menubar.add_command(
                label="Help")
        self.menubar.add_command(
                label="About")

    @staticmethod
    def popup1(event, *args, **kwargs):
        Popupmenu1 = tk.Menu(root, tearoff=0)
        Popupmenu1.configure(activebackground="#ececec")
        Popupmenu1.configure(activeborderwidth="1")
        Popupmenu1.configure(activeforeground="#000000")
        Popupmenu1.configure(background="#d9d9d9")
        Popupmenu1.configure(borderwidth="1")
        Popupmenu1.configure(disabledforeground="#a3a3a3")
        Popupmenu1.configure(foreground="#000000")
        Popupmenu1.post(event.x_root, event.y_root)

if __name__ == '__main__':
    vp_start_gui()




