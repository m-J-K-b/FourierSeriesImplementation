import pygame as pg


class DrawingPad:
    def __init__(self, app, res):
        self.app = app

        self.RES = self.WIDTH, self.HEIGHT = res
        self.AR = self.HEIGHT / self.WIDTH
        self.surface = pg.Surface(res)
        self.x = (app.WIDTH - self.WIDTH) / 2
        self.y = (app.HEIGHT - self.HEIGHT) / 2
        
        self.minx, self.maxx = -2, 2
        self.miny, self.maxy = -2 * self.AR, 2 * self.AR
        self.x_range = self.maxx - self.minx
        self.y_range = self.maxy - self.miny

        self.drawing_points = []
        self.points = []
        self.complex_points = []

        self.deleting = False
        self.deletion_pos = (0, 0)

    def map_points(self):
        self.points = []
        for p in self.drawing_points:
            self.points.append((p[0] / self.WIDTH * self.x_range + self.minx, p[1] / self.HEIGHT * self.y_range + self.miny))

    def get_complex_points(self):
        self.complex_points = []
        self.map_points()
        for p in self.points:
            self.complex_points.append(complex(p[0], p[1]))
        return self.complex_points

    def update(self):
        mx, my = self.app.mx, self.app.my
        mx = max(self.x, min(self.x + self.WIDTH - 1, mx)) - self.x
        my = max(self.y, min(self.y + self.HEIGHT - 1, my)) - self.y
        if self.app.mb[0]:
            self.drawing_points.append((mx, my))
        elif self.app.mb[2]:
            self.deleting = True
            self.deletion_pos = (mx, my)
            for p in self.drawing_points:
                d = (p[0] - mx)**2 + (p[1] - my)**2
                if d < 40**2:
                    self.drawing_points.remove(p)
        else:
            self.deleting = False
    
    def draw(self):
        self.surface.fill((30, 30, 30))
        if len(self.drawing_points) > 1:
            pg.draw.lines(self.surface, (255, 255, 255), True, self.drawing_points, 1)
        if self.deleting:
            pg.draw.circle(self.surface, (120, 120, 120), self.deletion_pos, 40, 1)

        self.app.screen.blit(self.surface, (self.x, self.y))