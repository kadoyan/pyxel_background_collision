import pyxel

def bg_collision(map, x, y, index):
    """Check collision in tilemap

    Args:
        map (int): Tilemap index
        x (float): X position of charcter
        y (float): Y position of charcter
        index (tuple): Tile index(x, y)
    """
    
    x1 = int((x + 3) // 8)
    y1 = int((y + 8) // 8)
    x2 = int((x + 12) // 8)
    y2 = int((y + 18) // 8)
    for yi in range(y1, y2 + 1):
        for xi in range(x1, x2 + 1):
            if pyxel.tilemaps[map].pget(xi, yi) == index:
                return True
    return False
