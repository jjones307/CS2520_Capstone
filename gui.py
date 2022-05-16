from textwrap import wrap
from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter.ttk import *

from Generator import *
from TrainerCodegui import *

################################### MAIN WINDOW CREATION ################################### 
window = Tk()
window.title("FANTASY NAME GENERATOR")
window.geometry('850x500')
window.minsize(750, 450)

# reset button
def resetAll():
    print("Reset pressed")

    combo.current(0) #set the selected item
    trainInput.delete('1.0', END)

    nameOut.configure(state='normal')
    nameOut.delete('1.0', END)
    nameOut.insert(INSERT, '')
    nameOut.configure(state='disabled')
resetBtn = Button(window, text= "Reset", command=resetAll)
resetBtn.place(relx=.4, rely=.99, anchor=S)
# end reset button

################################### USER SELECT LANGUAGE OPTION ################################### 
langPrompt = Label(window, text="Select Language:")
langPrompt.place(relx=.5, rely=.0, anchor=N)

combo = Combobox(window)
combo.configure(state='readonly')
combo['values']= ('Italian', 'Spanish', 'French', 'German')
combo.current(0) #set the selected item
combo.grid(column=0, row=1)
combo.place(relx=.5, rely=.05, anchor=N)


################################### USER ENTER TRAINER TEXT ################################### 
def trainPress():
    currentLang = combo.get()

    train(currentLang, trainInput.get("1.0","end-1c"))


    messagebox.showinfo(title='Language Trainer', message='Succesfully trained' )
    print(currentLang)
    print(trainInput.get("1.0","end-1c"))

inPrompt = Label(window, text="Enter sample text:")
inPrompt.place(relx=.5, rely=.2, anchor=N)

trainInput = scrolledtext.ScrolledText(window,width=60,height=11, wrap=WORD)
trainInput.insert(INSERT,"Enter text here.")
trainInput.configure(state='normal')
trainInput.place(relx=.5, rely=.25, anchor=N)

trainBtn = Button(window, text="TRAIN", command= trainPress)
trainBtn.place(relx=.5, rely=.65, anchor=N)

################################### NAME GENERATION ################################### 
def genPress():
    print("Generator pressed")

    currentLang = combo.get()
    newName = generate(currentLang)

    nameOut.configure(state='normal')
    nameOut.delete('1.0', END)
    nameOut.insert(INSERT, newName)
    nameOut.configure(state='disabled')

genBtn = Button(window, text="GENERATE NAME", command= genPress)
genBtn.place(relx=.4, rely=.8, anchor=NE)

nameOut = Text(window, width=30, height=1)
nameOut.configure(state='disabled')
nameOut.place(relx=.41, rely=.8, anchor=NW)

# Create a Button to call close()
exitBtn = Button(window, text= "Exit", command=window.quit)
exitBtn.place(relx=.6, rely=.99, anchor=S)

window.mainloop()
