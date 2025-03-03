import pyxel
from .key_input import KeyInput
from .outline import outline_blt
from .bg_collision import bg_collision
from .global_values import GlobalValues

SPRITES = [
    #x, y, w, h
    (8, 32, 16, 16),  #上
    (8, 0, 16, 16),   #下
    (8, 16, 16, 16),  #左
    (8, 16, -16, 16),  #右
]
ANIME_FRAME = [0, 1, 2, 1]
ACCELL = 1.5
OBLIQUE = 1.3
SCALE = 1

class Player:
    
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.anime = 0
        self.frame = len(ANIME_FRAME)
        self.direction = 2
        self.moving = False
        self.global_values = GlobalValues(self.x, self.y)
        # self.global_values.screen_position["x"] = 
        # self.global_values.screen_position["y"] = 
        self.global_x = 0
        self.global_y = 0
        self.collision = False
            
        self.center_width = pyxel.width // 2 - 8
        self.center_height = pyxel.height // 2 - 8
    
    def update(self):
        # 移動チェック初期化
        self.dx = 0
        self.dy = 0
        oblique = 0
        self.moving = False
        if KeyInput.is_pressed(KeyInput.UP):
            self.dy = -ACCELL
            self.direction = 0
            self.moving = True
            oblique += 1
        if KeyInput.is_pressed(KeyInput.DOWN):
            self.dy = ACCELL
            self.direction = 1
            self.moving = True
            oblique += 1
        if KeyInput.is_pressed(KeyInput.LEFT):
            self.dx = -ACCELL
            self.direction = 2
            self.moving = True
            oblique += 1
        if KeyInput.is_pressed(KeyInput.RIGHT):
            self.dx = ACCELL
            self.direction = 3
            self.moving = True
            oblique += 1
        if KeyInput.is_pressed(KeyInput.XBUTTON):
            self.dx = 0
            self.dy = 0
            oblique = 0
        
        # 移動中のみアニメーションさせる
        if self.moving:
            if pyxel.frame_count % 8 == 0:
                self.anime += 1
        else:
            self.anime = 0
            
        # 斜め移動
        if oblique>1:
            self.dx = OBLIQUE * (1 if self.dx>0 else -1)
            self.dy = OBLIQUE * (1 if self.dy>0 else -1)
        
        # グローバルの座標を取得
        global_pos = self.global_values.screen_position
        global_x = global_pos["x"]
        global_y = global_pos["y"]
        
        # スクロール位置
        if self.x % self.center_width < 2:
            global_x += self.dx
            global_x = sorted((0, global_x, self.global_values.MAP_WIDTH - pyxel.width))[1]
        if self.y % self.center_height < 2:
            global_y += self.dy
            global_y = sorted((0, global_y, self.global_values.MAP_HEIGHT - pyxel.height))[1]
            
        # 表示上のキャラクターの位置
        tmp_x = self.x
        tmp_y = self.y
        if (global_x == 0 or global_x == self.global_values.MAP_WIDTH - pyxel.width):
            tmp_x = sorted((2, tmp_x + self.dx, pyxel.width - 18))[1]
        else:
            tmp_x = self.center_width
        if (global_y == 0 or global_y == self.global_values.MAP_HEIGHT - pyxel.height):
            tmp_y = sorted((2, tmp_y + self.dy, pyxel.height - 18))[1]
        else:
            tmp_y = self.center_height
            
        # グローバルなキャラクター座標
        self.global_x = global_x + tmp_x
        self.global_y = global_y + tmp_y
        
        self.collision = bg_collision(3, self.global_x, self.global_y, (1, 0))
        if not self.collision:
            self.x = tmp_x
            self.y = tmp_y
            # 画面の移動を連動させる
            self.global_values.screen_position = {"x":global_x, "y":global_y}
    
    def draw(self):
        sprite = SPRITES[self.direction]
        animate = (sprite[0] + (ANIME_FRAME[self.anime % self.frame]) * 16, *sprite[1:])
        pyxel.elli(self.x + 2, self.y + 15, 12, 3, 1)
        outline_blt(1, self.x, self.y, 1, *animate, 0, 0, SCALE)
