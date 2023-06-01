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



def tutorial():
    mainlabel.config(text = "Uh oh, we are being attacked")    


mainlabel = Label(root, text = "Welcome to Butoland", command = tutorial).pack()
root.mainloop()

#lets see if this works

# from tkinter import *

# #Title: Epic Boss Battle

# #Description: Welcome to Word of Gods, in here you can venture around and have chances of meeting fearsome enemies, as well as making cool memories.
# # 
# #A button to where to go, Get buffs after defeating enemies, make enemy codes in functions. Hp, attack, drop chance   
# root = Tk()

# #               *Window Settings*
# root.configure(bg = "BLUE")



# rootHeight = 1000
# rootWidth  = 950
# screenHeight = root.winfo_screenheight()
# screenWidth  = root.winfo_screenwidth()
# x = (screenWidth  / 2 ) - (rootWidth  / 2)
# y = (screenHeight / 2 ) - (rootHeight / 2)

# root.geometry(f'{rootHeight}x{rootWidth}+{int(x)}+{int(y)}')


# #               ****Events of Games****

# #     Tutorial

# def welcoming1():
#     mainlabel.config(text = "I give up")




# #                *Main Part of Program*
# mainlabel = Label(root, text = "Welcome!", bg = "blue", fg = "white").pack()

# go = Button(root, text = "Continue", padx = 10, pady = 10, command = welcoming1).pack()




# root.mainloop()

# #lets see if this works

