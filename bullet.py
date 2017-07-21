import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """一个对飞船发射子弹进行管理的类"""

    def __init__(self, ai_settings, screen, ship, sb):
        """在飞船所处的位置创建一个子弹的对象"""
        super(Bullet, self).__init__()
        self.screen = screen

        # 减少积分
        sb.stats.score -= ai_settings.bullets_score

        # 创建一个子弹的矩形
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """向上移动子弹"""
        # 更新表示子弹位置的小数值
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)
