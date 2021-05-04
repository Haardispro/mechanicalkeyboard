from tkinter import *
from playsound import playsound

#Skeleton
w = Tk()
w.title("Mechanical Keyboard switch sound tester")
w.configure(bg="#010101")
w.geometry("800x600")

#Heading
at = "Mechanical Keyboard switch sound tester"
Font_tuple = ("JetBrains Mono", 20, "bold")
head = Label(w, text=at, fg="white", bg="#010101", font=Font_tuple)
head.grid(row=0, column=0, padx=70, pady=40)

#Functions
def blue():
    playsound(r"C:\Users\haard\OneDrive\Desktop\More_Projects\mechanicalkeyboard\blue.mp3")
def brown():
    playsound(r"C:\Users\haard\OneDrive\Desktop\More_Projects\mechanicalkeyboard\brown.mp3")   
def panda():
    playsound(r"C:\Users\haard\OneDrive\Desktop\More_Projects\mechanicalkeyboard\panda.mp3")
def kiwi():
    playsound(r"C:\Users\haard\OneDrive\Desktop\More_Projects\mechanicalkeyboard\kiwi.mp3")
def tange():
    playsound(r"C:\Users\haard\OneDrive\Desktop\More_Projects\mechanicalkeyboard\tang.mp3")
def inks():
    playsound(r"C:\Users\haard\OneDrive\Desktop\More_Projects\mechanicalkeyboard\inks.mp3")
def jades():
    playsound(r"C:\Users\haard\OneDrive\Desktop\More_Projects\mechanicalkeyboard\jade.mp3")
def creams():
    playsound(r"C:\Users\haard\OneDrive\Desktop\More_Projects\mechanicalkeyboard\cream.mp3")
#Buttons
b_font = ("JetBrains Mono", 15, "bold")
a = Button(w, text="Cherry Blue", font=b_font, command=blue) 
a.grid(row=1, column=0, pady=10)
b = Button(w, text="Cherry Brown(Linears)", font=b_font, command=brown)
b.grid(row=2, column=0, pady=0)
c = Button(w, text="Holy Pandas", font=b_font, command=panda)
c.grid(row=3, column=0, pady=10)
d = Button(w, text="C3 Kiwis", font=b_font, command=kiwi)
d.grid(row=4, column=0, pady=0)
e = Button(w, text="C3 Tangerines", font=b_font, command=tange)
e.grid(row=5, column=0, pady=10)
f = Button(w, text="Gateron Black Inks", font=b_font, command=inks)
f.grid(row=6, column=0, pady=0)
g = Button(w, text="Kailh Box Jades", font=b_font, command=jades)
g.grid(row=7, column=0, pady=10)
h = Button(w, text="NovelKeys Creams", font=b_font, command=creams)
h.grid(row=8, column=0, pady=0)


"""
Add .mp3 files for different switches
Switches:
Cherry Blue
Cherry Brown
Holy Panda
C3 Kiwis
C3 Tangerines
Gateron Black Inks
Box Jades
NovelKeys Creams

"""

w.mainloop()