
class Settings:
    """A class to store all settings for Alien Invasion"""
   
    def __init__(self):
        """Initialise the game static settings"""
        
        #screen settings
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230, 230, 230)

        #ship settings
        self.ship_limit = 2

        #bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        #Alien Settings
        self.fleet_drop_speed = 10

        #How quickly the game speeds up and scoring increases
        self.speedup_scale = 1.5
        self.score_scale = 2

        self.initialise_dynamic_settings()

    def initialise_dynamic_settings(self):
        
        self.ship_speed = 0.75
        self.bullet_speed = 1.5
        self.alien_speed = 0.1

        #fleet direction of 1 represents right -1 represents left
        self.fleet_direction = 1

        #Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and point value"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)

