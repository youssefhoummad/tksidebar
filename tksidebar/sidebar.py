from tkinter import Frame, Label, PhotoImage
from tkinter import ttk
from winreg import *


class Sidebar(Frame):
    PADDING = (0, 6)

    def __init__(self, master, accent_color=None, bg=None, bg_hover=None, bg_press=None, **kwargs):
        super().__init__(master)


        self.accent_color = accent_color or getAccentColor()
        self.bg = bg or '#EFF4F8'
        self.bg_hover = bg_hover or '#E8EBF0'
        self.bg_press = bg_press or '#D6D9DE'

        self.config(bg=self.bg)
        super().config(**kwargs)

        if not 'width' in kwargs:
            self.config(width=200)

        self.buttons = list()
      
    

    def config(self, **kwargs):
      if ('bg' or 'background') in kwargs:
        self.bg = kwargs.get('bg' or 'background')
        super().config(bg=self.bg)
      
      if 'accent_color' in kwargs:
        self.accent_color = kwargs.get('accent_color')
      if 'bg_hover' in kwargs:
        self.bg_hover = kwargs.get('bg_hover')
      if 'bg_press' in kwargs:
        self.bg_press = kwargs.get('bg_press')
      
      super().config(**kwargs)
      
    configure = config
      

    def add_header(self, widget):
        if self.buttons:
            raise "The header widget must be the first before other sidebar items"
        
        widget.config(bg=self['bg'])
        widget.pack(fill='x', padx=self.PADDING, pady=self.PADDING)

    def add_button(self, text, icon_path, command, at_bottom=False):
        # Create button Sidebar
        sb = SButton(self, text, icon_path, command, 
                      accent_color=self.accent_color, 
                      bg=self.bg, 
                      bg_hover=self.bg_hover, 
                      bg_press=self.bg_press
                    )

        if not at_bottom:
            sb.pack(fill='x', padx=self.PADDING, pady=1)
        else:
            sb.pack(side='bottom', fill='x', padx=self.PADDING, pady=1)
        
        self.buttons.append(sb)



class SButton(Frame):

  instances=set()

  def __init__(self, parent, text, icon=None, command=None,
    accent_color = "#0067C0",
    bg = '#EFF4F8',
    bg_hover = '#E8EBF0',
    bg_press = '#D6D9DE',
    **kwargs):
    super().__init__(parent, **kwargs)
    self.ACCENT_COLOR, self.BG, self.BG_HOVER, self.BG_PRESS = accent_color, bg, bg_hover, bg_press
    self.JUSTIFY = kwargs.get('justify', 'left')
    
    self.config(bg=self.BG)

    self.command= command
    self.active = False

    # edge border for active button
    self.border = Frame(self, bg=self.BG, width=4, height=18)
    # icon label
    _img = PhotoImage(file=icon)
    self.icon = Label(self, image=_img, bg=self.BG)
    self.icon.image = _img
    # text label
    self.text = Label(self, text=text, bg=self.BG) #  font=('Segoe UI',10,"normal")

    # pack border & icon & text
    self.border.pack(side=self.JUSTIFY, pady=3)
    self.icon.pack(side=self.JUSTIFY, pady=6, padx=(8,6))
    self.text.pack(side=self.JUSTIFY)


    self.bind("<ButtonPress-1>", self.on_press)
    self.bind("<ButtonRelease-1>", self.on_release)
    self.bind("<Enter>", self.on_hover)
    self.bind("<Leave>", self.on_leave)

    for w in self.winfo_children():
      w.bind("<ButtonPress-1>", self.on_press)
      w.bind("<ButtonRelease-1>", self.on_release)
      w.bind("<Enter>", self.on_hover)
      w.bind("<Leave>", self.on_leave)


    type(self).instances.add(self)

  
  def on_hover(self, e):
    if self.active:
      self.on_press(None)
    else:
      self.config(bg=self.BG_HOVER)
      self.text.config(bg=self.BG_HOVER)
      self.icon.config(bg=self.BG_HOVER)
    self.text.config(fg='black')
    
  
  def on_press(self, e):
    self.config(bg=self.BG_PRESS)
    self.text.config(bg=self.BG_PRESS, fg='gray')
    self.icon.config(bg=self.BG_PRESS)
    self.border.config(bg=self.ACCENT_COLOR)
    

    for btn in type(self).instances:
      btn.on_disactive()
    self.on_active()


  def on_leave(self, e):
    if self.active:
      self.on_press(None)
    else:
      self.icon.config(bg=self.BG)
      self.border.config(bg=self.BG)
      self.config(bg=self.BG)
      self.text.config(bg=self.BG)
    self.text.config(fg='black')
      

  def on_release(self, e):
    self.on_hover(e=None)
    self.command()

  def on_active(self):
    self.active = True
    self.border.config(bg=self.ACCENT_COLOR)
    self.config(bg=self.BG_PRESS)
    self.text.config(bg=self.BG_PRESS)
    self.icon.config(bg=self.BG_PRESS)

  def on_disactive(self):
    self.active = False
    self.border.config(bg=self.BG)
    self.config(bg=self.BG)
    self.text.config(bg=self.BG)
    self.icon.config(bg=self.BG)




def getAccentColor():  
    """
    Return the Windows 10 accent color used by the user in a HEX format
    """
    registry = ConnectRegistry(None,HKEY_CURRENT_USER)
    key = OpenKey(registry, r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Accent')
    key_value = QueryValueEx(key,'AccentColorMenu')
    accent_int = key_value[0]
    accent = accent_int-4278190080
    accent = str(hex(accent)).split('x')[1]
    accent = accent[4:6]+accent[2:4]+accent[0:2]
    return '#'+accent
