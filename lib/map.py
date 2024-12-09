import pyxel
from .global_values import GlobalValues

class DrawMap:
    def __init__(self, x=0, y=0, tm=0, u=0, v=0, w=256, h=212, c=0):
        self.x = x
        self.y = y
        self.tm = tm
        self.u = u
        self.v = v
        self.w = w
        self.h = h
        self.c = c
        self.global_values = GlobalValues()
        
    def update(self):
        self.u = self.global_values.screen_position["x"]
        self.v = self.global_values.screen_position["y"]
    
    def draw(self):
        pyxel.bltm(self.x, self.y, self.tm, self.u, self.v, self.w, self.h, self.c)
    
    