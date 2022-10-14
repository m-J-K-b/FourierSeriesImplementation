import pygame as pg


class CheckBox:
    def __init__(self, x, y, w, h, c1, c2):
        self.rect = pg.Rect(x, y, w, h)
        self.c1 = c1
        self.c2 = c2

        self.active = False
        self.hovered = False
        self.pressed = False
        self.prev_pressed = False

    def is_hovered(self, mp):
        self.hovered = False
        if self.rect.collidepoint(mp):
            self.hovered = True

    def is_pressed(self, mb):
        self.pressed = False
        if self.hovered and mb[0]:
            self.pressed = True

    def set_vals(self):
        if self.pressed and not self.prev_pressed:
            self.active = not self.active

    def update(self, mp, mb):
        self.is_hovered(mp)
        self.is_pressed(mb)
        self.set_vals()
        self.prev_pressed = self.pressed
    
    def draw(self, surf):
        pg.draw.rect(surf, self.c2 if self.active else self.c1, self.rect, border_radius = int(self.rect.height * 0.2))
