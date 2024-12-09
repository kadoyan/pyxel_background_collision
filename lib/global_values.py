import pyxel

class GlobalValues:
    MAP_WIDTH = 60 * 8
    MAP_HEIGHT = 60 * 8

    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.__initialized = False
        return cls._instance
    
    def __init__(self):
        self._screen_position = {'x': 0, 'y': 0}
        
    # Player position in Global
    @property
    def screen_position(self):
        return self._screen_position
    
    @screen_position.setter
    def screen_position(self, value):
        if not isinstance(value, dict) or 'x' not in value or 'y' not in value:
            raise ValueError("screen_position must be a dictionary with 'x' and 'y'")
        self._screen_position.update(value)
