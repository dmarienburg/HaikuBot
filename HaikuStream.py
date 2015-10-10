__author__ = 'David'
import tweepy
from tkinter import *
from tkinter import ttk
import HaikuMaker
from random import choice, randint


def tweep():
    auth = tweepy.OAuthHandler(consumer_key='CF2OBPRrbL9jlYT29krjC9k6d', consumer_secret='xKd4Ap9hEhbPAPAHQEj3hONvEbjmJXhKAWjBAbeNF90uI9eunQ')
    auth.set_access_token(key='2975429935-SEy1iJGy0alMnWlUqGLPQ8shVUh2zWbGNr0sauT', secret='lsWAr7Ugq2KgpnzBhC4zPvA4Ui9wPr8MmzQRdfnXeH2k8')
    api = tweepy.API(auth)
    c = randint(1, 5)

    if c == 1:
        tweep_direct(api)
    else:
        tweep_indirect(api)


def tweep_direct(api):
    my_friends_list = api.followers(api.me())
    r0 = choice(my_friends_list)
    row0.set(r0)
    r1 = str(row1.get())
    r2 = str(row2.get())
    r3 = str(row3.get())
    hshtg = str(hashtag.get())
    haiku = (r0, r1, r2, r3, hshtg)
    api.send_direct_message(r0, text='\n'.join(haiku))


def tweep_indirect(api):
    r1 = str(row1.get())
    r2 = str(row2.get())
    r3 = str(row3.get())
    hshtg = str(hashtag.get())
    haiku = (r1, r2, r3, hshtg)
    api.update_status(status='\n'.join(haiku))


def haikurun():
    h = HaikuMaker.HLines()
    row1.set(h['line1'])
    row2.set(h['line2'])
    row3.set(h['line3'])
    t = HaikuMaker.hshtg()
    hashtag.set(t)


def friend():
    auth = tweepy.OAuthHandler(consumer_key='CF2OBPRrbL9jlYT29krjC9k6d', consumer_secret='xKd4Ap9hEhbPAPAHQEj3hONvEbjmJXhKAWjBAbeNF90uI9eunQ')
    auth.set_access_token(key='2975429935-SEy1iJGy0alMnWlUqGLPQ8shVUh2zWbGNr0sauT', secret='lsWAr7Ugq2KgpnzBhC4zPvA4Ui9wPr8MmzQRdfnXeH2k8')

    api = tweepy.API(auth)

    followers = api.followers_ids('LadyMaybury')
    followers_of_followers = api.followers_ids(choice(followers))
    api.create_friendship(choice(followers_of_followers))

root = Tk()
root.title('Haiku Bot')

mainframe = ttk.Frame(root, padding='3 3 12 12')
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

row0 = StringVar()
row1 = StringVar()
row2 = StringVar()
row3 = StringVar()
hashtag = StringVar()

ttk.Label(mainframe, text='Haiku:').grid(column = 2, row=1, sticky=N)
ttk.Label(mainframe, textvariable=row1).grid(column=1, row=2, columnspan=2, sticky=W)
ttk.Label(mainframe, textvariable=row2).grid(column=1, row=3, columnspan=2, sticky=W)
ttk.Label(mainframe, textvariable=row3).grid(column=1, row=4, columnspan=2, sticky=W)
ttk.Label(mainframe, textvariable=hashtag).grid(column=1, row=5, columnspan=2, sticky=W)

ttk.Button(mainframe, text='Friend', command=friend).grid(column=2, row=6)
ttk.Button(mainframe, text='Tweet', command=tweep).grid(column=3, row=6, sticky=S)
ttk.Button(mainframe, text='Create Haiku', command=haikurun).grid(column=1, row=6, sticky=S)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

root.bind('<Return>', haikurun)

root.mainloop()