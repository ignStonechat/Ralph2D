import pygame
import pathlib

class Window():
    def __init__(self, title='Ralph2D Window', width=255, height=255):
        self.path = str(pathlib.Path(__file__).parent.resolve())
        self.title = title

        self.display = pygame.display
        self.window = self.display.set_mode((width, height))
        self.surface = self.display.get_surface()

        self.display.set_caption(title)
        icon_surface = pygame.image.load(self.path + '/media/icon.png')
        self.display.set_icon(icon_surface)

        self.last_mouse_position = (0, 0)
        self.keydown = []
        self.keyup = []
        self.objects = []


    def quit(self):
        pygame.display.quit()

    def update(self):
        self.keydown = []
        self.keyup = []
        # Update the events
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN: self.keydown.append(pygame.key.name(event.key))
            elif event.type == pygame.KEYUP: self.keyup.append(pygame.key.name(event.key))
            elif event.type == pygame.MOUSEMOTION: self.last_mouse_position = pygame.mouse.get_pos()
        # Update the objects
        for object in self.objects:
            object.update()
        pygame.display.update()

    def set_title(self, title=''):
        self.title = title
        self.display.set_caption(title)

    def set_icon(self, path_to_icon):
        icon_surface = pygame.image.load(path_to_icon)
        self.display.set_icon(icon_surface)

    def get_mouse_pos(self):
        return self.last_mouse_position

    def get_keys_down(self):
        return self.keydown
    
    def get_keys_up(self):
        return self.keyup



    def clear(self):
        self.window.fill((0, 0, 0))

    def draw_rectangle(self, color, x, y, width, height, thickness=0, border_radius=-1, top_left_radius=-1,
                       top_right_radius=-1, bottom_left_radius=-1, bottom_right_radius=-1):

        pygame.draw.rect(self.window, color, pygame.Rect(x, y, width, height), width=thickness,
                         border_radius=border_radius, border_top_left_radius=top_left_radius, border_top_right_radius=top_right_radius,
                         border_bottom_left_radius=bottom_left_radius, border_bottom_right_radius=bottom_right_radius)

    def draw_circle(self, color, x, y, radius, thickness=0):
        pygame.draw.circle(self.window, color, (x, y), radius, thickness)


    def draw_image(self, image, x, y):
        self.window.blit(image, (x, y))

    def draw_image_centered(self, image, x, y, original_width, original_height):
        rect = image.get_rect(center = (original_width/2+x, original_height/2+y))
        self.window.blit(image, (rect.x, rect.y))


    def use_object(self, object):
        self.objects.append(object)