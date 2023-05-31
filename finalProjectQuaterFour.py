from tkinter import *

#Title: Epic Boss Battle

#Description: Welcome to Word of Gods, in here you can venture around and have chances of meeting fearsome enemies, as well as making cool memories.
# 
#A button to where to go, Get buffs after defeating enemies, make enemy codes in functions. Hp, attack, drop chance   
root = Tk()

rootHeight = 1000
rootWidth  = 950
screenHeight = root.winfo_screenheight()
screenWidth  = root.winfo_screenwidth()
x = (screenWidth  / 2 ) - (rootWidth  / 2)
y = (screenHeight / 2 ) - (rootHeight / 2)

root.geometry(f'{rootHeight}x{rootWidth}+{int(x)}+{int(y)}')

root.mainloop()

#lets see if this works
