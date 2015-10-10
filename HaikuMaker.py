__author__ = 'David'
from dictionary import worddict
from random import choice, randint
import sched
import time
import multiprocessing

repeat = 'YES'

wrdcombo = {
    'noun':('verb', 'adj', 'pro', 'adv','art','ppro','prep'),
    'verb':('noun', 'adj', 'pro', 'adv','art', 'ppro', 'prep'),
    'adj':['noun','noun'],
    'pro':('adv','verb'),
    'adv':['verb','verb'],
    'art':('noun', 'adj', 'adv'),
    'ppro':('adj','noun','adv','verb'),
    'prep':('adj', 'noun')}

def wtcheck(lwt):
    if lwt == 0:
        wt = choice(list(worddict))
        return(wt)
    else:
        wt = choice(list(wrdcombo[lwt]))
        return(wt)

def HLines():
    cline1 = []
    cline2 = []
    cline3 = []
    def lineOne():
        lwt = 0
        syllables = 0
        while syllables < 5:
            type = wtcheck(lwt)
            lwt = type
            wordsyl = choice(list(worddict[type]))
            word = choice(list(worddict[type][wordsyl]))
            syllables += wordsyl
            cline1.append(word)
        if syllables != 5:
            del cline1[:]
            lineOne()
    def lineTwo():
        lwt = 0
        syllables = 0
        while syllables < 7:
            type = wtcheck(lwt)
            lwt = type
            wordsyl = choice(list(worddict[type]))
            word = choice(list(worddict[type][wordsyl]))
            syllables += wordsyl
            cline2.append(word)
        if syllables != 7:
            del cline2[:]
            lineTwo()
    def lineThree():
        lwt = 0
        syllables = 0
        while syllables < 5:
            type = wtcheck(lwt)
            lwt = type
            wordsyl = choice(list(worddict[type]))
            word = choice(list(worddict[type][wordsyl]))
            syllables += wordsyl
            cline3.append(word)
        if syllables != 5:
            del cline3[:]
            lineThree()
    lineOne()
    lineTwo()
    lineThree()
    return {'line1':(' '.join(cline1)),'line2':(' '.join(cline2)),'line3':(' '.join(cline3))}

    #print(len(' '.join(cline1))+len(' '.join(cline2))+len(' '.join(cline3)))

def hshtg():
    tg = ['#']
    a = choice(list(worddict['adj']))
    s1 = choice(list(worddict['adj'][a]))
    n = choice(list(worddict['noun']))
    s2 = choice(list(worddict['noun'][n]))
    tg.append(s1)
    tg.append(s2)
    htag = (''.join(tg))
    return htag

def mkHaiku(min,max):
    s = sched.scheduler(time.time, time.sleep)
    t = randint(min, max)
    s.enter(t, 1, HLines)
    s.enter(t, 2, hshtg)
    s.run()

def haikuTimer():
    global repeat
    while repeat == "YES":
        mkHaiku()
        repeat = input('Do you want to generate another Haiku (YES or NO)?')