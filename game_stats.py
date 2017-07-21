class GameStats:
    """跟踪游戏的统计信息"""
    def __init__(self, ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.reset_stats()
        # 游戏启动时处于非活动状态
        self.game_active = False
        # 任何时候都不应该重置最高分
        with open(ai_settings.filename) as file_object:
            score = file_object.read()
        self.high_score = int(score)

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
