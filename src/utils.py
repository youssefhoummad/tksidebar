
from winreg import *

# https://stackoverflow.com/a/44046627
# thanks to: Jakub Bláha
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



def color_variant(hex_color, brightness_offset=-10):
    """ takes a color like #87c95f and produces a lighter or darker variant """
    if len(hex_color) != 7:
        raise Exception("Passed %s into color_variant(), needs to be in #87c95f format." % hex_color)
    rgb_hex = [hex_color[x:x+2] for x in [1, 3, 5]]
    new_rgb_int = [int(hex_value, 16) + brightness_offset for hex_value in rgb_hex]
    new_rgb_int = [min([255, max([0, i])]) for i in new_rgb_int] # make sure new values are between 0 and 255
    # hex() produces "0x88", we want just "88"
    return "#" + "".join([hex(i)[2:] for i in new_rgb_int])




import math

def isLightOrDark(hexColor):
    value = hexColor.lstrip('#')
    lv = len(value)
    [r,g,b]= tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))
    hsp = math.sqrt(0.299 * (r * r) + 0.587 * (g * g) + 0.114 * (b * b))
    if (hsp>127.5):
        return 'light'
    else:
        return 'dark'

