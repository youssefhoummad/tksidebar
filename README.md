## tk_sidebare
tkinter widgte to add a sidebare to your apps.

## How to use
is simple

```
import tkinter as tk
from tk_sidebare import Sidebare

root = tk.Tk()
sidebare = Sidebare(root)

sidebare.add_button("path to icon1", "some string", command1)
sidebare.add_button("path to icon2", "some string", command2)
sidebare.add_button("path to icon3", "another string", command2, at_bottom=True)

root.mainloop()
```


## notice
you can add options to sidebare

`sidebare = Sidebare(root, bg='red', bg_hover='green', bg_press='yellow', accent_color='purple')`

the color must be in hex 

you can also add header to sidebare
`sidebare.add_header(widget)`
