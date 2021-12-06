import sys
import traceback
import tweepy
import os
from tkinter import messagebox as mbox
import os.path
import tkinter as tk
import tkinter.ttk as ttk
import BT_support
import drafts
import subprocess
from Cryptodome.Cipher import AES
uuid = str(subprocess.check_output('wmic csproduct get uuid'), 'utf-8').split('\n')[1].strip().split('-')
ekey = uuid[0]+uuid[2]+uuid[1]

with open('auth.data', 'rb') as authdata:
    authlist = authdata.read().split('\n'.encode('utf-8'))
decrypt = AES.new(ekey.encode("utf8"), AES.MODE_CFB, 'BotTweeterMadlad'.encode("utf8"))
auth = decrypt.decrypt(authlist[0]).decode('utf-8')
authsecret = decrypt.decrypt(authlist[1]).decode('utf-8')
key = decrypt.decrypt(authlist[2]).decode('utf-8')
keysecret = decrypt.decrypt(authlist[3]).decode('utf-8')

#####AUTHENTICATION#####
auth = tweepy.OAuthHandler(auth, authsecret) #ENTER INFO HERE
auth.set_access_token(key, keysecret) #ENTER INFO HERE

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication confirm")
    authed = True
except:
    print("Error during authentication")

def vp_start_gui():
    global val, w, root
    root = tk.Tk()
    BT_support.set_Tk_var()
    top = Toplevel1 (root)
    BT_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    global w, w_win, root
    root = rt
    w = tk.Toplevel (root)
    BT_support.set_Tk_var()
    top = Toplevel1 (w)
    BT_support.init(w, top, *args, **kwargs)
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

        top.geometry("575x350") #+713+216"
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1,  1)
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.313, rely=0.029, height=32, width=206)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Arial} -size 20 -weight bold")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='BotTweeter 1.2')

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.417, rely=0.114, height=32, width=71)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Segoe UI} -size 12")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='by madlad')

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.0, rely=0.149, height=18, width=124)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font="-family {Segoe UI} -size 13")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='Tweet caption')

        cb1 = tk.IntVar()
        cb2 = tk.IntVar()

        self.Entry2 = tk.Entry(top)
        self.Entry2.place(relx=0.017, rely=0.714, height=20, relwidth=0.337)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="-family {Courier New} -size 11")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(highlightbackground="#d9d9d9")
        self.Entry2.configure(highlightcolor="black")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(selectbackground="blue")
        self.Entry2.configure(selectforeground="white")

        self.Label4 = tk.Label(top)
        self.Label4.place(relx=0.017, rely=0.629, height=18, width=74)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font="-family {Segoe UI} -size 13")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='Tweet ID')

        self.Label5 = tk.Label(top)
        self.Label5.place(relx=0.017, rely=0.8, height=18, width=124)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(font="-family {Segoe UI} -size 13")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(text='Media filename')

        self.Entry3 = tk.Entry(top)
        self.Entry3.place(relx=0.017, rely=0.886, height=20, relwidth=0.337)
        self.Entry3.configure(background="white")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font="-family {Courier New} -size 11")
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(highlightbackground="#d9d9d9")
        self.Entry3.configure(highlightcolor="black")
        self.Entry3.configure(insertbackground="black")
        self.Entry3.configure(selectbackground="blue")
        self.Entry3.configure(selectforeground="white")
        self.Entry3.insert(0,'default.jpg')

        self.Text1 = tk.Text(top)
        self.Text1.place(relx=0.017, rely=0.229, relheight=0.269, relwidth=0.877)

        self.Text1.configure(background="white")
        self.Text1.configure(font="TkTextFont")
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#d9d9d9")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="blue")
        self.Text1.configure(selectforeground="white")
        self.Text1.configure(wrap="word")
        self.Text1.configure(font="-family {Segoe UI} -size 11")

        def endis():
            print(self)
            if cb1.get() == 0:
                self.Entry2['state'] = 'disabled'
            else:
                self.Entry2['state'] = 'normal'
            if cb2.get() == 0:
                self.Entry3['state'] = 'disabled'
            else:
                self.Entry3['state'] = 'normal'

        self.Checkbutton2 = tk.Checkbutton(top)
        self.Checkbutton2.place(relx=0.174, rely=0.514, relheight=0.086, relwidth=0.245)
        self.Checkbutton2.configure(activebackground="#ececec")
        self.Checkbutton2.configure(activeforeground="#000000")
        self.Checkbutton2.configure(background="#d9d9d9")
        self.Checkbutton2.configure(disabledforeground="#a3a3a3")
        self.Checkbutton2.configure(font="-family {Segoe UI} -size 13")
        self.Checkbutton2.configure(foreground="#000000")
        self.Checkbutton2.configure(highlightbackground="#d9d9d9")
        self.Checkbutton2.configure(highlightcolor="black")
        self.Checkbutton2.configure(justify='left')
        self.Checkbutton2.configure(text='Contains media')
        self.Checkbutton2.configure(variable=cb2)
        self.Checkbutton2.configure(command=endis)

        self.Checkbutton1 = tk.Checkbutton(top)
        self.Checkbutton1.place(relx=0.017, rely=0.514, relheight=0.086, relwidth=0.123)
        self.Checkbutton1.configure(activebackground="#ececec")
        self.Checkbutton1.configure(activeforeground="#000000")
        self.Checkbutton1.configure(background="#d9d9d9")
        self.Checkbutton1.configure(disabledforeground="#a3a3a3")
        self.Checkbutton1.configure(font="-family {Segoe UI} -size 13")
        self.Checkbutton1.configure(foreground="#000000")
        self.Checkbutton1.configure(highlightbackground="#d9d9d9")
        self.Checkbutton1.configure(highlightcolor="black")
        self.Checkbutton1.configure(justify='left')
        self.Checkbutton1.configure(text='Reply')
        self.Checkbutton1.configure(variable=cb1)
        self.Checkbutton1.configure(command=endis)

        def crash(exc):
            with open('crashlog.txt', 'w') as f:
                f.write(str(exc))
            mbox.showinfo('Error','''Something went wrong! Please contact the developer and send them the crashlog.txt file''', icon='error')

        def read_drafts():
            if os.stat('drafts.paul.town').st_size != 0:
                drafts.vp_start_gui()
            else:
                mbox.showinfo('Error','You have no drafts')
        def save_drafts():
            with open('drafts.paul.town', 'a') as f:
                if cb1.get() == 1:
                    if cb2.get() == 1:
                        if self.Entry2.get() != '':
                            if self.Entry3.get() != '':
                                if os.path.isfile(self.Entry3.get()) == True:
                                    try:
                                        draft = {'tweet':self.Text1.get('1.0','end-1c'), 'TID':self.Entry2.get(), 'media':self.Entry3.get()}
                                        json.dump(draft, f)
                                        f.write('\n')
                                        print('Draft saved!')
                                        mbox.showinfo('Success!','Draft has been saved')
                                    except Exception as e:
                                        crash(exc = traceback.format_exc())
                                        exit()
                                else:
                                    mbox.showinfo('Error','''No such file exists in this script's folder''')
                            else:
                                mbox.showinfo('Error','Please specify a media file')
                        else:
                            mbox.showinfo('Error','There is no tweet ID')
                    else:
                        if self.Text1.get('1.0','end-1c') != '':
                            if self.Entry2.get() != '':
                                draft = {'tweet':self.Text1.get('1.0','end-1c'), 'TID':self.Entry2.get()}
                                json.dump(draft, f)
                                f.write('\n')
                                print('Draft saved!')
                                mbox.showinfo('Success!','Draft has been saved')
                            else:
                                mbox.showinfo('Error','There is no tweet ID')
                        else:
                            mbox.showinfo('Error','Your tweet is empty')

                else:
                    if cb2.get() == 1:
                        if self.Entry3.get() != '':
                            if os.path.isfile(self.Entry3.get()) == True:
                                try:
                                    draft = {'tweet':self.Text1.get('1.0','end-1c'), 'media':self.Entry3.get()}
                                    json.dump(draft, f)
                                    f.write('\n')
                                    print('Draft saved!')
                                    mbox.showinfo('Success!','Draft has been saved')
                                except Exception as e:
                                    crash(exc = traceback.format_exc())
                                    exit()
                            else:
                                mbox.showinfo('Error','''No such file exists in this script's folder''')
                        else:
                            mbox.showinfo('Error','Please specify a media file')
                    else:
                        if self.Text1.get('1.0','end-1c') != '':
                            draft = {'tweet':self.Text1.get('1.0','end-1c')}
                            json.dump(draft, f)
                            f.write('\n')
                            print('Draft saved!')
                            mbox.showinfo('Success!','Draft has been saved')
                        else:
                            mbox.showinfo('Error','Your tweet is empty')
        
        def tweet():
            if cb1.get() == 1:
                if cb2.get() == 1:
                    if self.Entry2.get() != '':
                        if self.Entry3.get() != '':
                            if len(self.Text1.get('1.0','end-1c')) <= 280:
                                if os.path.isfile(self.Entry3.get()) == True:
                                    try:
                                        api.update_status_with_media(self.Entry3.get(), status = self.Text1.get('1.0','end-1c'), in_reply_to_status_id = self.Entry2.get(), auto_populate_reply_metadata=True)
                                        print('Tweet sent!')
                                        os._exit(0)
                                    except Exception as e:
                                        crash(exc = traceback.format_exc())
                                        exit()
                                else:
                                    mbox.showinfo('Error','''No such file exists in this script's folder''')
                            else:
                                mbox.showinfo('Error',f'''Your tweet is over the character limit ({len(self.Text1.get('1.0','end-1c'))})''')
                        else:
                            mbox.showinfo('Error','Please specify a media file')
                    else:
                        mbox.showinfo('Error','There is no tweet ID')
                else:
                    if self.Text1.get('1.0','end-1c') != '':
                        if len(self.Text1.get('1.0','end-1c')) <= 280:
                            if self.Entry2.get() != '':
                                api.update_status(status = self.Text1.get('1.0','end-1c'), in_reply_to_status_id = self.Entry2.get(), auto_populate_reply_metadata=True)
                                print('Tweet sent!')
                                os._exit(0)
                            else:
                                mbox.showinfo('Error','There is no tweet ID')
                        else:
                            mbox.showinfo('Error',f'''Your tweet is over the character limit ({len(self.Text1.get('1.0','end-1c'))})''')
                    else:
                        mbox.showinfo('Error','Your tweet is empty')

            else:
                if cb2.get() == 1:
                    if self.Entry3.get() != '':
                        if len(self.Text1.get('1.0','end-1c')) <= 280:
                            if os.path.isfile(self.Entry3.get()) == True:
                                try:
                                    api.update_status_with_media(self.Text1.get('1.0','end-1c'), self.Entry3.get())
                                    print('Tweet sent!')
                                    os._exit(0)
                                except Exception as e:
                                    crash(exc = traceback.format_exc())
                                    exit()
                            else:
                                mbox.showinfo('Error','''No such file exists in this script's folder''')
                        else:
                            mbox.showinfo('Error',f'''Your tweet is over the character limit ({len(self.Text1.get('1.0','end-1c'))})''')
                    else:
                        mbox.showinfo('Error','Please specify a media file')
                else:
                    if self.Text1.get('1.0','end-1c') != '':
                        if len(self.Text1.get('1.0','end-1c')) <= 280:
                            api.update_status(self.Text1.get('1.0','end-1c'))
                            print('Tweet sent!')
                            os._exit(0)
                        else:
                            mbox.showinfo('Error',f'''Your tweet is over the character limit ({len(self.Text1.get('1.0','end-1c'))})''')
                    else:
                        mbox.showinfo('Error','Your tweet is empty')
        
        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.555, rely=0.540, height=85, width=200)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font="-family {Segoe UI} -size 14 -weight bold")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='Send Tweet!')
        self.Button1.configure(command=tweet)

        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.555, rely=0.800, height=45, width=98)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(font="-family {Segoe UI} -size 14 -weight bold")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='Drafts')
        self.Button2.configure(command=read_drafts)

        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.732, rely=0.800, height=45, width=98)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(font="-family {Segoe UI} -size 14 -weight bold")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='Save')
        self.Button2.configure(command=save_drafts)

        if os.stat('temp.dump').st_size != 0:
            print('not empty')
            with open('temp.dump', 'r') as tempdump:
                templist = list(tempdump)
            open("temp.dump", "w").close()
            if str(templist[0]) != '':
                print('not empty')
                cdraft = json.loads(templist[0])
                print(cdraft)
                BTDtweet = cdraft.get('tweet')
                self.Text1.insert(1.0, BTDtweet)
                if 'TID' in cdraft:
                    self.Checkbutton1.select()
                    BTDTID = cdraft.get('TID')
                    self.Entry2.delete(0,tk.END)
                    self.Entry2.insert(0,BTDTID)
                if 'media' in cdraft:
                    self.Checkbutton2.select()
                    BTDmedia = cdraft.get('media')
                    self.Entry3.delete(0,tk.END)
                    self.Entry3.insert(0,BTDmedia)
        endis()

if __name__ == '__main__':
    vp_start_gui()
