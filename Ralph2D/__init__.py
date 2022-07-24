import time
import pygame
import os
import pathlib

class Window():
    def __init__(self, title='', width=255, height=255):
        self.path = str(pathlib.Path(__file__).parent.resolve())
        self.title = title

        self.display = pygame.display
        self.window = self.display.set_mode((width, height))
        self.surface = self.display.get_surface()

        self.display.set_caption(title)
        icon_surface = pygame.image.load(self.path + '/icon.jpg')
        self.display.set_icon(icon_surface)

    def quit(self):
        pygame.display.quit()

    def update(self):
        pygame.display.update()

    def set_title(self, title=''):
        self.title = title
        self.display.set_caption(title)



    def clear(self):
        self.window.fill((0, 0, 0))

    def draw_rectangle(self, color, x, y, width, height):
        pygame.draw.rect(self.window, color, pygame.Rect(x, y, width, height))




def limit_fps(fps=60, time_passed=0):
    '''
        WARNING: Actually affects FPS (not a joke)

        time_passed = Time it took to complete a loop
    '''
    sleep_size = 1/fps-time_passed
    if sleep_size >= 0:
        time.sleep(sleep_size)