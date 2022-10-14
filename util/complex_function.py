import pygame as pg


def complex_to_euclidean(c):
    return (c.real, c.imag)

class ComplexFunction:
    def __init__(self, points):
        self.points = points
        self.N = len(points)
        self.t_interval = 1 / self.N
        self.real_points = [complex_to_euclidean(c) for c in self.points]

    def f(self, t):
        index1 = int(self.N * t) % self.N
        index2 = (index1 + 1) % self.N
        p1, p2 = self.points[index1], self.points[index2]
        t1 = float(index1) / float(self.N)
        return p1 + (p2 - p1) * ((t - t1 + 1e-4) / self.t_interval)

    def draw(self, surf, color, scalar = 1, offx = 0, offy = 0, show_nodes = True):
        points = []
        for p in self.real_points:
            x, y = p
            x, y = (x - offx) * scalar, (y - offy) * scalar
            points.append((x, y))
            if show_nodes:
                pg.draw.circle(surf, color, (x, y), 3)
        pg.draw.lines(surf, color, True, points, 1)