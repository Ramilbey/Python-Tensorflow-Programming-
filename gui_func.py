from tkinter import *
def processOk():
    print("ok button is clicked ")

def processCancel():
    print("cancel button is clicked ")

window = Tk()
btOk = Button(window, text = "OK", fg = "red", command = processOk)
btCancel = Button(window, text = "Cancel", bg="yellow", command = processCancel)
btOk.pack()
btCancel.pack()

window.mainloop()
