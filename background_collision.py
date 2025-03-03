import pyxel
from lib.player import Player
from lib.map import DrawMap

from lib.global_values import GlobalValues
from lib.wave_screen import wave_horizontal

SCREEN_WIDTH = 376
SCREEN_HEIGHT = 212

class App:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, fps=60, display_scale=2, capture_scale=2, capture_sec=20, title="background_collision")
        # リソースファイルを読み込むけど、イメージバンクもタイルマップも読み込まない
        # pyxel.load("background_collision.pyxres", True, True)
        # マップチップをイメージバンク0に
        pyxel.images[0] = pyxel.Image.from_image(
            "assets/background.png", incl_colors=False
        )
        # キャラクターをイメージバンク1に
        pyxel.images[1] = pyxel.Image.from_image(
            "assets/characters.png", incl_colors=False
        )
        # Tiledで作ったマップデータを読み込む
        for index in range(4):
            pyxel.tilemaps[index] = pyxel.Tilemap.from_tmx("assets/test.tmx", index)
        
        self.global_values = GlobalValues()
        
        # 最背面
        self.background = DrawMap(0, 0, 0, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 0)
        # 背面だけどデザイン上、最背面の上に乗せるもの
        self.overwrap = DrawMap(0, 0, 1, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 0)
        # キャラクターの上に被さるもの
        self.foreground = DrawMap(0, 0, 2, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 0)
        # 衝突判定用
        self.collision = DrawMap(0, 0, 3, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 0)
        
        self.player = Player(140, 80)
        
        pyxel.run(self.update, self.draw)
    
    def update(self):
        self.player.update()
        self.background.update()
        self.foreground.update()
        self.overwrap.update()
        self.collision.update()
        wave_horizontal(8, 24, 96, 0, 2, 2, 0)
    
    def draw(self):
        pyxel.cls(5)
        self.background.draw()
        self.overwrap.draw()
        self.player.draw()
        self.foreground.draw()
        # self.collision.draw()
        
        self.debug({
            "global_x": self.global_values.screen_position["x"],
            "global_y": self.global_values.screen_position["y"],
            "player_x": self.player.x,
            "player_y": self.player.y,
            "player_dx": self.player.dx,
            "player_dy": self.player.dy,
            "global_x": self.player.global_x,
            "global_y": self.player.global_y,
            "collision": self.player.collision
        })
    
    def debug(self, values):
        x = 2
        y = 2
        for key, value in values.items():
            pyxel.text(x, y, f"{key}, {value}", 0)
            y += 8
App()
