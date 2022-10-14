import cmath

import pygame as pg

from .complex_function import complex_to_euclidean


class FourierSeries:
    def __init__(self, app, complex_function, sample_point_num):
        self.app = app

        self.complex_function = complex_function
        self.change_sample_point_num(sample_point_num)

        self.show_epicycles = True
        self.show_function = True
        self.show_sample_points = True
        self.show_function_points = True

    def change_sample_point_num(self, sample_point_num):
        self.sample_point_num = sample_point_num
        self.sample_points = [self.complex_function.f(i / sample_point_num) for i in range(sample_point_num)]
        point_rect = self.get_point_rect([complex_to_euclidean(c) for c in self.complex_function.points])
        self.scalar = self.app.HEIGHT * 0.75 / max(point_rect[3], point_rect[2])
        self.offx = point_rect[6] - self.app.WIDTH / 2 / self.scalar
        self.offy = point_rect[7] - self.app.HEIGHT / 2 / self.scalar
        self.sample_points_drawing_data = [((x - self.offx) * self.scalar, (y - self.offy) * self.scalar) for x, y in [complex_to_euclidean(c) for c in self.sample_points]]

        self.frequencys = []

        self.path = []
        self.epicycle_data = []

        self.get_requencys()

    def fft(self, k):
        return sum([self.sample_points[n] * cmath.exp(-1j * 2 * cmath.pi * k * n / self.sample_point_num) for n in range(self.sample_point_num)])

    def get_requencys(self):
        for k in range(0, self.sample_point_num):
            self.frequencys.append(self.fft(k))

    def calc_path(self):
        ftx, fty = 0, 0
        self.epicycle_data = []
        for k in range(-int(self.sample_point_num / 2), int(self.sample_point_num / 2) + 1):
            e = cmath.exp(-1j * 2 * cmath.pi * k * self.app.t) * self.frequencys[k] / self.sample_point_num
            ftx += e.real
            fty += e.imag
            self.epicycle_data.append((ftx, fty, abs(e)))
        self.path.append((ftx, fty))
    
    def get_point_rect(self, points):
        minx, maxx = min(points, key = lambda x: x[0])[0], max(points, key = lambda x: x[0])[0]
        miny, maxy = min(points, key = lambda x: x[1])[1], max(points, key = lambda x: x[1])[1]
        width, height = maxx - minx, maxy - miny
        centerx = width / 2 + minx
        centery = height / 2 + miny
        return (minx, miny, width + 1e-4, height + 1e-4, maxx, maxy, centerx, centery)

    def draw(self):
        self.calc_path()

        if self.show_function:
            self.complex_function.draw(self.app.screen, (100, 100, 100), self.scalar, self.offx, self.offy, show_nodes = self.show_function_points)

        if self.show_sample_points:
            for p in self.sample_points_drawing_data:
                pg.draw.circle(self.app.screen, (128, 128, 255), p, 2)
        
        if len(self.path) > 1:
            pg.draw.lines(self.app.screen, (255, 255, 255), False, [((x - self.offx) * self.scalar, (y - self.offy) * self.scalar) for x, y in self.path], 1)


        if self.show_epicycles:
            prev_e = (-self.offx * self.scalar, -self.offy * self.scalar)
            for x, y, r in self.epicycle_data:
                p = ((x - self.offx) * self.scalar, (y - self.offy) * self.scalar)
                pg.draw.line(self.app.screen, (120, 120, 120), prev_e, (p))
                pg.draw.circle(self.app.screen, (120, 120, 120), p, r * self.scalar, 1)
                prev_e = p
        
        last_point = self.path[-1]
        x, y = last_point
        pg.draw.circle(self.app.screen, (255, 128, 128), (((x - self.offx) * self.scalar, (y - self.offy) * self.scalar)), 4)
