class Settings:
    """存储外星人入侵的所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.name = "飞机大战外星人"
        # 飞船的设置
        self.ship_speed_factor = 1.5
        self.ship_limit = 2
        # 子弹设置
        self.bullet_speed_factor = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 5
        # 外星人设置
        self.alien_speed_factor = 0.4
        self.fleet_drop_speed = 10
        self.fleet_direction = 1

