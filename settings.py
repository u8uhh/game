class Settings:

    def __init__(self):
        # Screen settings
        self.screen_width = 1100
        self.screen_height = 700
        self.bg_color = (130, 130, 130)

        # ship settings
        self.ship_speed = 1.3
        self.ship_limit = 7
        # bullet
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 10

        # alien settings
        self.fleet_drop_speed = 10

        # як гра має прискорюватися
        self.speedup_scale = 1.1

        self.score_scale = 1.7

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """initialize"""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        # fleet_direction 1 представляє напрямок праворуч -1 -- left.
        self.fleet_direction = 1

        # get score
        self.alien_points = 60

    def increase_speed(self):
        """Збільшення налаштування швидкості та вартості прибульців."""
        self.bullet_speed *= self.speedup_scale
        self.ship_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)

