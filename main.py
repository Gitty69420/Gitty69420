def __init__(self):
    pygame.init()
    self.screen = pygame.display.set_mode((app.WIDTH, app.HEIGHT))
    pygame.display.set_caption("Shooter")
    self.clock = pygame.time.Clock()

    self.assets = app.load_assets()

    font_path = os.path.join("assets", "PressStart2P.ttf")
    self.font_small = pygame.font.Font(font_path, 18)
    self.font_large = pygame.font.Font(font_path, 32)

    self.background = self.create_random_background(
        app.WIDTH, app.HEIGHT, self.assets["floor_tiles"]
    )

    self.running = True
    self.game_over = False

    self.reset_game()
    
class Player:
    def __init__(self, x, y, assets):
        self.x = x
        self.y = y

        self.speed = app.PLAYER_SPEED
        self.animations = assets["player"]
        self.state = "idle"
        self.frame_index = 0
        self.animation_timer = 0
        self.animation_speed = 8

        self.image = self.animations[self.state][self.frame_index]
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.facing_left = False
