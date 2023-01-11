
import tkinter as tk
from tksidebar import Sidebook



window =  tk.Tk()
window.geometry('1000x500')



sidebook = Sidebook(window) 

frame_1 = tk.Frame(bg='#A75D5D', height=500, width=400)
frame_2 = tk.Frame(bg='#0081B4', height=500, width=400)
frame_3 = tk.Frame(bg='#C780FA', height=500, width=400)
frame_4 = tk.Frame(bg='#FF7B54', height=500, width=400)
frame_5 = tk.Frame(bg='#495579', height=500, width=400)


tabs = [
('split', frame_1, r'img\icons8-cut-24.png', False),
('crop margins', frame_2,r'img\icons8-crop-24.png', False),
('rotate pages', frame_3,r'img\icons8-rotate-24.png', False),
('to images', frame_4,r'img\icons8-picture-24.png', False),
('about', frame_5, r'img\icons8-settings-24.png', True), # this on bottom
]

for name, frame, icon, bottom in tabs:
  sidebook.add(frame, text=name, icon=icon, at_bottom=bottom) # add here any options for pack (fill, expand, padx...)
sidebook.select(0)

sidebook.pack(anchor='nw', fill='both', expand=True)

window.mainloop()




