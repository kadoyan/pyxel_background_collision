#Make wave
import pyxel
from collections import deque

def wave_horizontal(width:int, height:int, u:int, v:int, shift, scale:int, bank, fill = True):
    """
    Horizontal wavy scroll

    Args:
        width (int): Width of the target area
        height (int): Height of the target area
        u (int): X axis of the target area
        v (int): Y axis of the target area
        shift (int): Wave height
        scale (int): Wave width
        bank (Image): Image Object
        fill: False -> Fill the edge with 0
    """
    if pyxel.frame_count % 10 == 0:
        ptr_target = pyxel.images[bank].data_ptr()
        
        for y in range(v, v + height, 1):
            start = y * 256 + u
            end = y * 256 + u + width
            source = ptr_target[start:end]
            #Shift data
            if fill:
                shifted_list = deque(source)
                shifted_list.rotate(1)
            else:
                shifted_list = shift_list(source, shift_volume, 0)
            ptr_target[start:end] = shifted_list

def shift_list(lst:list, shift:int, fill_value=0):
    if shift > 0:
        # Right
        return [fill_value] * shift + lst[:-shift]
    elif shift < 0:
        # Left
        return lst[-shift:] + [fill_value] * (-shift)
    else:
        # none
        return lst
