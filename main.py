import random

import pygame as pg

from util.checkbox import CheckBox
from util.complex_function import *
from util.drawing_pad import DrawingPad
from util.fourier_series import FourierSeries


class App:
    def __init__(self):
        pg.init()
        self.RES = self.WIDTH, self.HEIGHT = 1000, 600
        self.screen = pg.display.set_mode(self.RES)
        self.clock = pg.time.Clock()
        self.font = pg.font.SysFont('Arial', 16)
        
        self.t = 0
        self.state = 'menu'
        
        self.mx, self.my = 0, 0
        self.mb = [False, False, False]

        self.iterations = 10
        self.iterations_surf = self.font.render('Sample points: ' + str(self.iterations), True, (255, 255, 255))

        #self.complex_function = ComplexFunction([complex(-1, -1), complex(1, -1), complex(1, 1), complex(-1, 1)])
        self.complex_function = ComplexFunction([complex(random.randint(-2, 2), random.randint(-2, 2)) for i in range(random.randint(2, 10))])
        self.fourier_series = FourierSeries(self, self.complex_function, self.iterations)
        self.drawing_pad = DrawingPad(self, (self.WIDTH * 0.75, self.HEIGHT * 0.75))


        self.menu_surf = self.screen.copy()
        self.menu_text = self.font.render('Menu', True, (255, 255, 255))

        self.show_epicycles = True
        self.show_function = True
        self.show_sample_points = True
        self.show_function_points = True
        self.check_boxes = [CheckBox(self.WIDTH * 0.2, (self.HEIGHT - 4 * 30) / 2 + i * 50 + 25, 30, 30, (120, 120, 120), (255, 128, 128)) for i in range(-2, 2)]
        self.menu_options = [
                        self.font.render('show epicycles', True, (255, 255, 255)), 
                        self.font.render('show input function', True, (255, 255, 255)),
                        self.font.render('show sample points', True, (255, 255, 255)),
                        self.font.render('show function points', True, (255, 255, 255))
                        ]
        self.menu_text_explanation = 'This is an implementation of the Fourier Series Algorithm. | How does it Work? | You can enter drawing mode through pressing TAB. | Once in drawing mode you can draw with the left mouse button. | You turn your mouse into an eraser with your right mouse button. | You can access the Menu with Escape. | In the Menu you can enable and disable certain things. | Scrolling with the mouse wheel will change the precission with which the input function is traced. | To generate a random input function you can press r'
        self.menu_text_explanation_surf = pg.Surface((self.WIDTH * 0.35, self.HEIGHT * 0.7))
        self.menu_text_explanation_surf_y = (self.HEIGHT - self.menu_text_explanation_surf.get_height()) / 2
        self.menu_text_explanation_surf_x = self.WIDTH - self.menu_text_explanation_surf_y - self.menu_text_explanation_surf.get_width()
        self.menu_text_explanation_surf.fill((25, 25, 25))
        last_x = 0
        last_y = 0
        words = self.menu_text_explanation.split(' ')
        for word in words:
            word_surf = self.font.render(word + ' ', True, (255, 255, 255))
            x = last_x
            y = last_y
            if word == '|':
                last_y += word_surf.get_height() + 15
                last_x = 0
                continue
            new_x = last_x + word_surf.get_width()
            if new_x > self.menu_text_explanation_surf.get_width():
                last_x = 0
                last_y += word_surf.get_height() + 10
                x = last_x
                y = last_y
            self.menu_text_explanation_surf.blit(word_surf, (x, y))
            last_x += word_surf.get_width()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            if self.state == 'fft':
                if event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 5:
                        self.iterations = max(self.iterations - 1, 2)
                        self.iterations_surf = self.font.render('Sample points: ' + str(self.iterations), True, (255, 255, 255))
                        self.fourier_series.change_sample_point_num(self.iterations)
                    elif event.button == 4:
                        self.iterations = min(self.iterations + 1, 1000)
                        self.iterations_surf = self.font.render('Sample points: ' + str(self.iterations), True, (255, 255, 255))
                        self.fourier_series.change_sample_point_num(self.iterations)\
            
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    if self.state == 'menu':
                        self.state = 'fft'
                    elif self.state in ['fft', 'drawing']:
                        self.state = 'menu'
                if self.state in ['fft', 'drawing']:
                    if event.key == pg.K_TAB:
                        if self.state == 'drawing':
                            self.state = 'fft'
                            if len(self.drawing_pad.drawing_points) > 1:
                                self.fourier_series.complex_function = ComplexFunction(self.drawing_pad.get_complex_points())
                                self.fourier_series.change_sample_point_num(self.iterations)
                        else:
                            self.state = 'drawing'
                    if event.key == pg.K_r:
                        self.fourier_series.complex_function = ComplexFunction([complex(random.randint(-2, 2), random.randint(-2, 2)) for i in range(random.randint(2, 10))])
                        self.fourier_series.change_sample_point_num(self.iterations)

    def update(self):
        self.mp = self.mx, self.my = pg.mouse.get_pos()
        self.mb = pg.mouse.get_pressed()
        if self.state == 'drawing':
            self.drawing_pad.update()
        elif self.state == 'fft':
            self.t += 0.002
        elif self.state == 'menu':
            [c.update(self.mp, self.mb) for c in self.check_boxes]
            self.fourier_series.show_epicycles = self.check_boxes[0].active
            self.fourier_series.show_function = self.check_boxes[1].active
            self.fourier_series.show_sample_points = self.check_boxes[2].active
            self.fourier_series.show_function_points = self.check_boxes[3].active
        pg.display.update()
        pg.display.set_caption(f'FPS: {self.clock.get_fps():.2f}, T: {self.t}')
        self.clock.tick(60)

    def draw(self):
        if self.state == 'drawing':
            self.drawing_pad.draw()
        elif self.state == 'fft':
            self.screen.fill((25, 25, 25))
            self.screen.blit(self.iterations_surf, (20, 20))
            self.fourier_series.draw()
        elif self.state == 'menu':
            self.menu_surf.fill((25, 25, 25))
            self.menu_surf.blit(self.menu_text, (20, 20))

            for i, c in enumerate(self.check_boxes):
                c.draw(self.menu_surf)
                text = self.menu_options[i]
                self.menu_surf.blit(text, (c.rect.right + 20, c.rect.top + (c.rect.height - text.get_height()) / 2))

            self.menu_surf.blit(self.menu_text_explanation_surf, (self.menu_text_explanation_surf_x, self.menu_text_explanation_surf_y))

            self.screen.blit(self.menu_surf, (0, 0))
        
    def run(self):
        while True:
            self.events()
            self.update()
            self.draw()

if __name__ == '__main__':
    app = App()
    app.run()