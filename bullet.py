import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """一个对飞船发射子弹进行管理的类"""

    def __init__(self, ai_settings, screen, ship):
        """在飞船所处的位置创建一个子弹的对象"""
        super(Bullet, self).__init__()
        self.screen = screen

        # 创建一个子弹的矩形
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
