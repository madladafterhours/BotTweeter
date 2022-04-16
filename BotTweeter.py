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
        top.title("BotTweeter 1.3.1")
        top.configure(background=_bgcolor)
        top.configure(highlightbackground=_bgcolor)
        top.configure(highlightcolor="black")

        self.title = tk.Label(top)
        self.title.place(relx=0.301, rely=0.029, height=32, width=220)
        self.title.configure(text='BotTweeter 1.3.1',
                              background=_bgcolor, font="-size 20 -weight bold")

        self.sig = tk.Label(top)
        self.sig.place(relx=0.417, rely=0.114, height=32, width=71)
        self.sig.configure(text='by madlad', background=_bgcolor, font=" size 12")

        self.captionLabel = tk.Label(top)
        self.captionLabel.place(relx=0.0, rely=0.149, height=18, width=124)
        self.captionLabel.configure(text='Tweet caption', background=_bgcolor, font="-size 13")

        cb1 = tk.IntVar()
        cb2 = tk.IntVar()

        self.replyID = tk.Entry(top)
        self.replyID.place(relx=0.017, rely=0.714, height=20, relwidth=0.337)
        self.replyID.configure(font="-family {Courier New} -size 11")


        self.replyIDLabel = tk.Label(top)
        self.replyIDLabel.place(relx=0.017, rely=0.629, height=18, width=74)
        self.replyIDLabel.configure(text='Tweet ID', background=_bgcolor, font="-size 13")

        self.filenameLabel = tk.Label(top)
        self.filenameLabel.place(relx=0.017, rely=0.8, height=18, width=124)
        self.filenameLabel.configure(text='Media filename', background=_bgcolor, font="-size 13")

        self.filename = tk.Entry(top)
        self.filename.place(relx=0.017, rely=0.886, height=20, relwidth=0.337)
        self.filename.configure(font="-family {Courier New} -size 11")

        self.caption = tk.Text(top)
        self.caption.place(relx=0.017, rely=0.229, relheight=0.269, relwidth=0.877)
        self.caption.configure(font="-family {Segoe UI} -size 11", wrap="word")

        def endis():
            print(self)
            if cb1.get() == 0:
                self.replyID['state'] = 'disabled'
            else:
                self.replyID['state'] = 'normal'
            if cb2.get() == 0:
                self.filename['state'] = 'disabled'
            else:
                self.filename['state'] = 'normal'

        self.Checkbutton2 = tk.Checkbutton(top)
        self.Checkbutton2.place(relx=0.174, rely=0.514, relheight=0.086, relwidth=0.245)
        self.Checkbutton2.configure(background=_bgcolor, command=endis, variable=cb2, text='Contains media', justify='left', font="-size 13")

        self.Checkbutton1 = tk.Checkbutton(top)
        self.Checkbutton1.place(relx=0.017, rely=0.514, relheight=0.086, relwidth=0.123)
        self.Checkbutton1.configure(font="-size 13", background=_bgcolor, variable=cb1, command=endis, text='Reply', justify='left')

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
                        if self.replyID.get() != '':
                            if self.filename.get() != '':
                                if os.path.isfile(self.filename.get()) == True:
                                    try:
                                        draft = {'tweet':self.caption.get('1.0','end-1c'), 'TID':self.replyID.get(), 'media':self.filename.get()}
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
                        if self.caption.get('1.0','end-1c') != '':
                            if self.replyID.get() != '':
                                draft = {'tweet':self.caption.get('1.0','end-1c'), 'TID':self.replyID.get()}
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
                        if self.filename.get() != '':
                            if os.path.isfile(self.filename.get()) == True:
                                try:
                                    draft = {'tweet':self.caption.get('1.0','end-1c'), 'media':self.filename.get()}
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
                        if self.caption.get('1.0','end-1c') != '':
                            draft = {'tweet':self.caption.get('1.0','end-1c')}
                            json.dump(draft, f)
                            f.write('\n')
                            print('Draft saved!')
                            mbox.showinfo('Success!','Draft has been saved')
                        else:
                            mbox.showinfo('Error','Your tweet is empty')

        def tweet():
            if cb1.get() == 1:
                if cb2.get() == 1:
                    if self.replyID.get() != '':
                        if self.filename.get() != '':
                            if len(self.caption.get('1.0','end-1c')) <= 280:
                                if os.path.isfile(self.filename.get()) == True:
                                    try:
                                        api.update_status_with_media(self.filename.get(), status = self.caption.get('1.0','end-1c'), in_reply_to_status_id = self.replyID.get(), auto_populate_reply_metadata=True)
                                        print('Tweet sent!')
                                        os._exit(0)
                                    except Exception as e:
                                        crash(exc = traceback.format_exc())
                                        exit()
                                else:
                                    mbox.showinfo('Error','''No such file exists in this script's folder''')
                            else:
                                mbox.showinfo('Error',f'''Your tweet is over the character limit ({len(self.caption.get('1.0','end-1c'))})''')
                        else:
                            mbox.showinfo('Error','Please specify a media file')
                    else:
                        mbox.showinfo('Error','There is no tweet ID')
                else:
                    if self.caption.get('1.0','end-1c') != '':
                        if len(self.caption.get('1.0','end-1c')) <= 280:
                            if self.replyID.get() != '':
                                api.update_status(status = self.caption.get('1.0','end-1c'), in_reply_to_status_id = self.replyID.get(), auto_populate_reply_metadata=True)
                                print('Tweet sent!')
                                os._exit(0)
                            else:
                                mbox.showinfo('Error','There is no tweet ID')
                        else:
                            mbox.showinfo('Error',f'''Your tweet is over the character limit ({len(self.caption.get('1.0','end-1c'))})''')
                    else:
                        mbox.showinfo('Error','Your tweet is empty')

            else:
                if cb2.get() == 1:
                    if self.filename.get() != '':
                        if len(self.caption.get('1.0','end-1c')) <= 280:
                            if os.path.isfile(self.filename.get()) == True:
                                try:
                                    api.update_status_with_media(self.caption.get('1.0','end-1c'), self.filename.get())
                                    print('Tweet sent!')
                                    os._exit(0)
                                except Exception as e:
                                    crash(exc = traceback.format_exc())
                                    exit()
                            else:
                                mbox.showinfo('Error','''No such file exists in this script's folder''')
                        else:
                            mbox.showinfo('Error',f'''Your tweet is over the character limit ({len(self.caption.get('1.0','end-1c'))})''')
                    else:
                        mbox.showinfo('Error','Please specify a media file')
                else:
                    if self.caption.get('1.0','end-1c') != '':
                        if len(self.caption.get('1.0','end-1c')) <= 280:
                            api.update_status(self.caption.get('1.0','end-1c'))
                            print('Tweet sent!')
                            os._exit(0)
                        else:
                            mbox.showinfo('Error',f'''Your tweet is over the character limit ({len(self.caption.get('1.0','end-1c'))})''')
                    else:
                        mbox.showinfo('Error','Your tweet is empty')

        self.sendTweet = tk.Button(top)
        self.sendTweet.place(relx=0.555, rely=0.540, height=85, width=200)
        self.sendTweet.configure(font="-size 14 -weight bold", command=tweet, text='Send Tweet!', pady="0", background=_bgcolor)

        self.saveDraft = tk.Button(top)
        self.saveDraft.place(relx=0.555, rely=0.800, height=45, width=98)
        self.saveDraft.configure(command=read_drafts, text='Drafts', pady="0", background=_bgcolor, font="-size 14 -weight bold")

        self.saveDraft = tk.Button(top)
        self.saveDraft.place(relx=0.732, rely=0.800, height=45, width=98)
        self.saveDraft.configure(font="-family {Segoe UI} -size 14 -weight bold", background=_bgcolor, pady="0", text='Save', command=save_drafts)

        if os.stat('temp.dump').st_size != 0:
            with open('temp.dump', 'r') as tempdump:
                templist = list(tempdump)
            open("temp.dump", "w").close()
            if str(templist[0]) != '':
                print('not empty')
                cdraft = json.loads(templist[0])
                BTDtweet = cdraft.get('tweet')
                self.caption.insert(1.0, BTDtweet)
                if 'TID' in cdraft:
                    self.Checkbutton1.select()
                    BTDTID = cdraft.get('TID')
                    self.replyID.delete(0,tk.END)
                    self.replyID.insert(0,BTDTID)
                if 'media' in cdraft:
                    self.Checkbutton2.select()
                    BTDmedia = cdraft.get('media')
                    self.filename.delete(0,tk.END)
                    self.filename.insert(0,BTDmedia)
        endis()

if __name__ == '__main__':
    vp_start_gui()
