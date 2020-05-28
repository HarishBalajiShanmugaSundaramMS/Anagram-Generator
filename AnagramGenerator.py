
#? Required Packages
import time
import tkinter as tk
from itertools import permutations
from tkinter import *
from tkinter import messagebox

import enchant
from googletrans import Translator

root = tk.Tk()
#? Sets Title
root.title('Anagram Generator')
#? Restricts Resizing
root.resizable(0, 0)
root.config(bg='#011627')
root.wm_attributes('-alpha', '0.98')
fr =tk.Frame(root)
fr.config(bg='#011627')
list_length=0
radValue=IntVar()
totalTime=0.0
#status = tk.Label(root, text='Time Taken : ' + str(totalTime)+' seconds', relief=SUNKEN, anchor=W)

def selectionCall():
    selection=str(radValue.get())    
    if (selection=='1'):
        print('Selected Theme: ','Light')
        root.config(bg='#FFFFFF')
        label01.config(bg='#FFFFFF', fg='#000000')
        entry01.config(bg='#FFFFFF', fg='#000000')
        text01.config(bg='#FFFFFF', fg='#000000',)
        optionmenu01.config(bg='#FFFFFF', fg='#000000')
        fr.config(bg='#FFFFFF')
        r1.config(bg='#FFFFFF', fg='#000000')
        r2.config(bg='#FFFFFF', fg='#000000')
        r3.config(bg='#FFFFFF', fg='#000000')
        button01.config(fg='green')
        button02.config(fg='red')
        #status.config(bg='#FFFFFF', fg='#000000')

    if (selection=='2'):
        print('Selected Theme: ','Dark')
        root.config(bg='#011627')
        label01.config(bg='#011627', fg='#01BAEF')
        entry01.config(bg='#011627', fg='#01BAEF')
        text01.config(bg='#011627', fg='#01BAEF')
        optionmenu01.config(bg='#01BAEF', fg='#011627')
        fr.config(bg='#011627')
        r1.config(bg='#011627', fg='#01BAEF')
        r2.config(bg='#011627', fg='#01BAEF')
        r3.config(bg='#011627', fg='#01BAEF')
        button01.config(fg='green')
        button02.config(fg='red')
        #status.config(bg='#011627', fg='#01BAEF')
    
    elif (selection=='3'):
        print('Selected Theme: ','Contrast')
        root.config(bg='#000000')
        label01.config(bg='#000000', fg='#FFFFFF')
        entry01.config(bg='#000000', fg='#FFFFFF')
        text01.config(bg='#000000', fg='#FFFFFF')
        optionmenu01.config(bg='#FFFFFF', fg='#000000')
        fr.config(bg='#000000')
        r1.config(bg='#000000', fg='#FFFFFF')
        r2.config(bg='#000000', fg='#FFFFFF')
        r3.config(bg='#000000', fg='#FFFFFF')
        button01.config(fg='#000000')
        button02.config(fg='#000000')
        #status.config(bg='#011627', fg='#01BAEF')

r1=tk.Radiobutton(fr,text='Light ☀︎', variable=radValue, value=1,command=selectionCall, font=('calibri', 16, 'bold'))
r1.config(bg='#011627', fg='#01BAEF')
r2=tk.Radiobutton(fr,text='Dark ☾', variable=radValue, value=2,command=selectionCall, font=('calibri', 16, 'bold'))
r2.config(bg='#011627', fg='#01BAEF')
r3=tk.Radiobutton(fr,text='Contrast ☯︎', variable=radValue, value=3,command=selectionCall, font=('calibri', 16, 'bold'))
r3.config(bg='#011627', fg='#01BAEF')

fr.grid(row=7, column=0, padx=5, pady=5, sticky=W+E+N+S)
r1.grid(row=0, column=0, padx=5, pady=5, sticky=W+E+N+S)
r2.grid(row=0, column=1, padx=5, pady=5, sticky=W+E+N+S)
r3.grid(row=0, column=2, padx=5, pady=5, sticky=W+E+N+S)

# ?=========Try these examples===============================================
# *     coder            edit              sonic
# *     post             name              boredom
# *     resort           last              letters
# *     ielts            protein           printer
# *     earth            dancer            pear
# *     spider           medical           oracle
# ?==========================================================================

# ?==========Function Definitions Begins Here================================

def clearText():
    text01.configure(state='normal')
    text01.delete('1.0', END)
    entry01.delete('0', END)
    text01.configure(state='disabled')

def onReturn(event):
    generateAnagram()

def generateAnagram():
    text01.configure(state='normal')
    translator = Translator()

    if len(entry01.get()) == 0:
        msg = messagebox.showwarning('Empty Input', 'Please Enter A Word')
    else:
        databaselist = []
        counter = 99
        startTime = time.time()
        ss = var.get()
        print(ss, dd[ss])
        d = enchant.Dict(dd[ss])
        word = str(entry01.get())
        word = word.upper()
        L = list(word)
        perm = permutations(L)
        mylist = []
        for i in list(perm):
            wow = ''.join(i)
            result = d.check(wow)
            if(result == True):
                mylist.append(wow)
                mylist = list(dict.fromkeys(mylist))

        length = len(mylist)
        for j in range(length):
            quote = str(mylist[j] + '\n')
            text01.insert(END, quote)
            print(mylist[j])
            databaselist.append(mylist[j])
            list_length = len(databaselist)
        endTime = time.time()
        totalTime = round(endTime-startTime, 3)
        print(totalTime)
        print(databaselist)
        print(ss)
        
    text01.configure(state='disabled')

# ?===========Function Definition Ends Here==================================

label01 = tk.Label(root, text='Enter a Word', font=('calibri', 40, 'bold'))
label01.config(bg='#011627', fg='#01BAEF')
entry01 = tk.Entry(root, text='Enter a Word', font=('calibri', 20, 'bold'))
entry01.config(bg='#011627', fg='#01BAEF')

labelFrame = tk.LabelFrame(root, text='Recorded Anagrams')
labelFrame.config(bg='#011627', fg='#01BAEF', borderwidth=2,
                  width=600, background='#011627')

entry01.focus()  # * Sets Focus
entry01.bind('<Return>', onReturn)
button01 = tk.Button(root, text='Generate Anagrams ✔︎',
                     command=generateAnagram, fg='green', font=('calibri', 16, 'bold'))
button02 = tk.Button(root, text='Clear ✘', command=clearText, fg='red', font=('calibri', 16, 'bold'))

text01 = tk.Text(root, font=('calibri', 20, 'bold'), state='disabled')
text01.config(width=20, height=10, bg='#011627', fg='#01BAEF')
dd = {'German': 'de-DE', 'French': 'fr-FR', 'British English': 'en-GB',
      'Australian English': 'en-AU', 'American English': 'en-US'}
temp1 = []
temp2 = []
for key in dd:
    temp1.append(dd[key])
    temp2.append(key)
    optionlist01 = temp1
    var = tk.StringVar(root)
    var.set(key)
    optionmenu01 = tk.OptionMenu(root, var, *temp2)
    optionmenu01.config(bg='#01BAEF', fg='#011627', font=('calibri', 16, 'bold'))
# ?==============Widget Arrangement in Grid==================================
optionmenu01.grid(row=0, column=0, padx=5, pady=5, sticky=W+E+N+S)
label01.grid(row=1, column=0, padx=5, pady=5, sticky=W+E+N+S)
entry01.grid(row=2, column=0, padx=5, pady=5, sticky=W+E+N+S)
button01.grid(row=3, column=0, padx=5, pady=5, sticky=W+E+N+S)
text01.grid(row=4, column=0, padx=5, pady=5, sticky=W+E+N+S)
button02.grid(row=5, column=0, padx=5, pady=5, sticky=W+E+N+S)
#status.grid(row=6, sticky=W+E+N+S)

# ?==========================================================================
root.mainloop()
