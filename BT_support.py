import sys
import tkinter as tk
import tkinter.ttk as ttk

def set_Tk_var():
    global che49
    che49 = tk.IntVar()
    global che57
    che57 = tk.IntVar()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import unknown
    unknown.vp_start_gui()




