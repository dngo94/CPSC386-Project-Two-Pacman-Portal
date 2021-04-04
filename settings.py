class Settings():
    """A class to store all settings for PacMan."""

    def __init__(self):
        """Initialize the game's settings."""
        self.screen_width = 683  # 910  931
        self.screen_height = 840  # 1000
        self.bg_color = (0, 0, 0)
        self.speed = 1
        self.init_dynamic_settings()
        # self.launch_bg_color = (0, 0, 0)
        # self.launch_text_color = (255, 255, 255)
        # self.launch_title_color = (0, 255, 0)

    def init_dynamic_settings(self):
        self.ship_speed_factor = 5
        self.bullet_speed_factor = 1
        self.alien_speed = 1
        self.ufo_speed = -0.5
        self.fleet_direction = 1
        self.ufo_fleet_direction = 1
        self.alien_points = 10
        self.speedup_scale = 1.1

    def increase_speed(self):
        scale = self.speedup_scale
        self.alien_speed *= scale

