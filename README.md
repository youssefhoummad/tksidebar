# tk_sidebare
tkinter widgte to add a sidebare to your apps.

## How to install

`pip install tk_sidebare`


## How to use
is simple

```
import tkinter as tk
from tk_sidebare import Sidebare

root = tk.Tk()
sidebare = Sidebare(root)

sidebare.add_button("path to icon1.png", "some string", command1)
sidebare.add_button("path to icon2.png", "some string", command2)
sidebare.add_button("path to icon3.png", "another string", command2, at_bottom=True)

root.mainloop()
```


## notice
you can add options to sidebare

`sidebare = Sidebare(root, bg='#EFF4F8', bg_hover='green', bg_press='yellow', accent_color='purple')`

the background color `bg` must be in hex 

you can also add header to sidebare
`sidebare.add_header(widget)`
