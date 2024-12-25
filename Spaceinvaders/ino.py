import pygame

class Ino(pygame.sprite.Sprite):
    """one alien class"""

    def __init__(self, screen):
        """initializing and setting the initial position"""
        super(Ino, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/ino.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        """alien output on screen"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """moves aliens"""
        self.y += 0.2
        self.rect.y = self.y
