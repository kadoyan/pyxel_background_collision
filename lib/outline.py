import pyxel

def outline_blt(color, x, y, img, u, v, w, h, transparent=0, rotate=0, scale=1):
    """Drawing mono color outline to a sprite

    Args:
        color (int): outline color
        x (float): X position on screen
        y (float): y position on screen
        img (int): Number of image bank
        u (int): X position on the image bank
        v (int): Y position on the image bank
        w (int): sprite width
        h (int): sprite height
        transparent (int): Numbner of transparent color
        rotate (float): rotate (degree)
        scale (float): scale
    """
    workArea = pyxel.Image(abs(w), abs(h))
    workArea.blt(0, 0, img, u, abs(v), abs(w), h, transparent)
    shape = workArea.data_ptr()
    
    # Convert to list
    array = list(shape)
    # Color conversion of non-transparent colors
    replaced = [color if data != transparent else transparent for data in array]
    shape[:] = replaced
    # for index, data in enumerate(shape):
    #     if data != transparent:
    #         shape[index] = color
    
    outline = (0, 0, w, h, transparent, rotate, scale)
    
    pyxel.blt(x + scale, y, workArea, *outline)
    pyxel.blt(x - scale, y, workArea, *outline)
    pyxel.blt(x, y + scale, workArea, *outline)
    pyxel.blt(x, y - scale, workArea, *outline)
    pyxel.blt(x, y, img, u, v, w, h, transparent, rotate, scale)
