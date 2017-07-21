class Settings:
    """存储外星人入侵的所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (0, 0, 0)
        self.name = "飞机大战外星人"
        # 飞船的设置
        self.ship_speed_factor = 1.5
        self.ship_limit = 1
        # 子弹设置
        self.bullet_speed_factor = 2
        self.bullet_width = 4
        self.bullet_height = 15
        self.bullet_color = 255, 255, 255
        self.bullets_allowed = 5
        # 外星人设置
        self.alien_speed_factor = 0.1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
        # 增加难度设置
        self.speedup_scale = 1.5
        # 点数增加倍率
        self.score_scale = 1.5
        self.initialize_dynamic_settings()
        # 记分
        self.alien_points = 50
        # 数据文件
        self.filename = 'score.txt'

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.bullet_speed_factor = 2
        self.alien_speed_factor = 0.1
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        """提高速度设置"""
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.score_scale * self.alien_points)

