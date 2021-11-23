import sys
import tkinter as tk
import tkinter.ttk as ttk
import drafts_support
import BotTweeter
from BotTweeter import vp_start_gui
import json
import os

def vp_start_gui():
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    drafts_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    global w, w_win, root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    drafts_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        _bgcolor = '#d9d9d9'
        _fgcolor = '#000000'
        _compcolor = '#d9d9d9'
        _ana1color = '#d9d9d9'
        _ana2color = '#ececec'

        top.geometry("600x173+765+302")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1,  1)
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")
        
        f = open('drafts.paul.town', 'r')
        global currentpage
        currentpage = 1
        lines = 0
        for line in f:
            if line != "\n":
                lines += 1
        f.close()

        global Dtweet
        global DTID
        global Dmedia
        Dtweet = str
        DTID = str
        Dmedia = str

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.4, rely=0.675, height=41, width=114)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='Page: '+str(currentpage))
        self.Label1.configure(font="-family {Arial} -size 16 -weight bold")
        self.Label1.configure(highlightcolor="black")

        def display_draft():
            global currentpage
            global cdraft
            with open('drafts.paul.town') as rawdrafts:
                draftlist = list(rawdrafts)
            print(draftlist[currentpage-1])
            cdraft = json.loads(draftlist[currentpage-1])
            self.Button1.config(text=cdraft.get('tweet'))

        def next():
            global currentpage
            global cdraft
            if currentpage < lines:
                currentpage += 1
                print(currentpage)
                self.Label1.config(text='Page: '+str(currentpage))
                self.Button2['state'] = 'normal'
                display_draft()
            if currentpage == lines:
                self.Button3['state'] = 'disabled'
                display_draft()
            
        def prev():
            global currentpage
            if currentpage >= 2:
                currentpage -= 1
                self.Button3['state'] = 'normal'
                self.Label1.config(text='Page: '+str(currentpage))
                if currentpage == 1:
                    self.Button2['state'] = 'disabled'
                display_draft()
                
        def select_draft():
            global cdraft
            global Dtweet
            global DTID
            global Dmedia
            Dtweet = cdraft.get('tweet')
            if 'TID' in cdraft:
                DTID = cdraft.get('TID')
            if 'media' in cdraft:
                Dmedia = cdraft.get('media')

            #BotTweeter.Toplevel1().__init__(self).draftmode()
            with open('temp.dump', 'w') as f:
                json.dump(cdraft, f)
            os.execv(sys.executable, ['python BotTweeter.py'] + sys.argv)

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.017, rely=0.04, height=94, width=577)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='Button')
        self.Button1.configure(command=select_draft)

        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.017, rely=0.636, height=54, width=117)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='Previous')
        self.Button2['state'] = 'disabled'
        self.Button2.configure(command=prev)
        self.Button2.configure(font="-family {Arial} -size 18 -weight bold")
        self.Button2.configure(highlightcolor="black")

        self.Button3 = tk.Button(top)
        self.Button3.place(relx=0.783, rely=0.636, height=54, width=117)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='Next')
        self.Button3.configure(command=next)
        self.Button3.configure(font="-family {Arial} -size 18 -weight bold")
        self.Button3.configure(highlightcolor="black")

        if lines == 1:
            self.Button2['state'] = 'disabled'
            self.Button3['state'] = 'disabled'

        display_draft()

if __name__ == '__main__':
    vp_start_gui()





