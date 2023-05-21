# import tkinter as tk

# if you are still working under a Python 2 version, 
# comment out the previous line and uncomment the following line
# import Tkinter as tk
from Tkinter import *

root = Tk()
logo = PhotoImagem(file="Python-Logo-Free-Download-PNG.png")

w1 = Label(root,image=logo).pack(side="right")

explanation = """At present, only GIF and PPM/PGM
formats are supported, but an interface 
exists to allow additional image file
formats to be added easily."""

w2 = tk.Label(root, 
              justify=tk.LEFT,
              padx = 10, 
              text=explanation).pack(side="left")

root.mainloop()


# w = Label(root, text="Hello Tkinter!") # import as tk = tk.Label
# w.pack()

# root.mainloop()