from tkinter import *
window = Tk()

def click():
    print("hello")



window.title("kuhals")
window.geometry("420x420")
icon=PhotoImage(file="alive.png")
window.iconphoto(True,icon)
window.config(background="#EBB3FB")


butto=Button(window,text="type")
butto.config(command=click)
butto.config(bg="#C13383")
butto.config(fg="#CC56FF")
butto.config(activebackground="#CC56FF")
image=PhotoImage(file="alive.png")
butto.config(image=image)
butto.pack()



window.mainloop()