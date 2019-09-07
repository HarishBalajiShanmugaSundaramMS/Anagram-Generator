import timeit
import tkinter as tk
from itertools import permutations
from tkinter import *
import enchant

root = tk.Tk()

root.title('Anagram Generator')
root.resizable(0, 0)
root.config(bg='#25D366')


def clearText():
    text01.delete('1.0', END)
    entry01.delete('0', END)


#?Try these examples
#*coder
#*post
#*soldier
#*ielts
#*earth
#*spider

def generateAnagram():
    d = enchant.Dict('en_US')
    #word = 'TESLA'
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
        # print(mylist[j])
        quote = str(mylist[j] + '\n')
        text01.insert(END, quote)


label01 = tk.Label(root, text='Enter a Word', font=('calibri', 40, 'bold'))
label01.config(bg='#25D366')
entry01 = tk.Entry(root, text='Enter a Word', font=('calibri', 20, 'bold'))
button01 = tk.Button(root, text='Generate', command=generateAnagram)
button02 = tk.Button(root, text='Clear', command=clearText)


text01 = tk.Text(root, font=('calibri', 20, 'bold'))
text01.config(width=20, height=10, bg='aqua')


label01.grid(row=0, column=0, padx=5, pady=5, sticky=W)
entry01.grid(row=1, column=0, padx=5, pady=5, sticky=W+E+N+S)

button01.grid(row=2, column=0, padx=5, pady=5, sticky=W+E+N+S)
text01.grid(row=3, column=0, padx=5, pady=5, sticky=W+E+N+S)

button02.grid(row=4, column=0, padx=5, pady=5, sticky=W+E+N+S)


root.mainloop()

