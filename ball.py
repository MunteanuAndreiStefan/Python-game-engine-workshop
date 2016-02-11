
# ball.py

import os, sys
import pygame
from pygame.locals import *
from collections import defaultdict
import pypybox2d as b2d


class Resources(object):
    __ASSETS = 'assets'
    class __NullSound(object):
        def play(self):
            pass

    class __NullFont(object):
        def render(self):
            pass

    @classmethod
    def load_image(cls, name, colorkey=None):
        fullname = os.path.join(cls.__ASSETS, name)
        try:
            image = pygame.image.load(fullname)
        except pygame.error as message:
            print 'Cannot load image:', fullname
            raise SystemExit, message

        image = image.convert()
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, RLEACCEL)

        return image, image.get_rect()

    @classmethod
    def load_sound(cls, name):
        if not pygame.mixer or not pygame.mixer.get_init():
            return cls.__NullSound()

        fullname = os.path.join(cls.__ASSETS, name)
        try:
            sound = pygame.mixer.Sound(fullname)
        except pygame.error as message:
            print 'Cannot load sound:', fullname
            raise SystemExit, message

        return sound

    @classmethod
    def load_font(cls, name, size):
        if not pygame.font:
            return cls.__NullFont()

        return pygame.font.Font(name, size)


class GameInput(object):
    def __init__(self):
        self.__key_map = defaultdict(lambda: False)

    def process_key(self, key, isdown):
        self.__key_map[key] = isdown

    def is_key_down(self, key):
        return self.__key_map[key]


class GamePhysics(object):
    __TIME_STEP = 1.0 / 60
    __VEL_ITERATIONS = 8
    __POS_ITERATIONS = 3

    def __init__(self):
        self.world = b2d.World(gravity=(0, 10*100))

    def update(self):
        self.world.step(self.__TIME_STEP, self.__VEL_ITERATIONS, self.__POS_ITERATIONS)


class GameObject(pygame.sprite.Sprite):
    def __init__(self, parent, name):
        super(GameObject, self).__init__()
        self.parent = parent
        self.image, self.rect = Resources.load_image(name)

    def update(self):
        raise NotImplementedError('abstract method')


class DynamicObject(object):
    def __init__(self, *args, **kwargs):
        super(DynamicObject, self).__init__(*args, **kwargs)
        self.__init_physics()

    def __init_physics(self):
        phys = self.parent.game_physics
        shape, position = self._get_body_desc()
        fix = b2d.fixture.Fixture(shape=shape, density=1.0)
        self.phys_body = phys.world.create_dynamic_body(fixtures=fix, bullet=False, position=position)

    def _get_body_desc(self):
        raise NotImplementedError('abstract method')


class StaticObject(object):
    def __init__(self, *args, **kwargs):
        super(StaticObject, self).__init__(*args, **kwargs)
        self.__init_physics()

    def __init_physics(self):
        phys = self.parent.game_physics
        shape, position = self._get_body_desc()
        fix = b2d.fixture.Fixture(shape=shape, density=1.0)
        self.phys_body = phys.world.create_static_body(fixtures=fix, position=position)

    def _get_body_desc(self):
        raise NotImplementedError('abstract method')


class Ball(DynamicObject, GameObject):
    def __init__(self, parent):
        super(Ball, self).__init__(parent, 'ball.gif')
        self.__hit_sound = Resources.load_sound('ding.wav')

    def _get_body_desc(self):
        return b2d.body.shapes.Circle(radius=float(self.rect.width) / 2.0), (100, 100)

    def update(self):
        r = float(self.rect.width) / 4.0
        self.rect.x, self.rect.y = self.phys_body.position.x - r, self.phys_body.position.y - r


class Ground(StaticObject, GameObject):
    def __init__(self, parent):
        super(Ground, self).__init__(parent, 'ground.bmp')

    def _get_body_desc(self):
        return b2d.body.shapes.Polygon(box=(640, 20)), (0, 460)

    def update(self):
        self.rect.x, self.rect.y = self.phys_body.position.x, self.phys_body.position.y


class Engine(object):
    __RESOLUTION = (640, 480)
    __TITLE = 'Ball game'
    __BG_COLOR = (240, 240, 240)

    def __init__(self):
        self.__init_pygame()
        self.__load_resources()
        self.game_input = GameInput()
        self.game_physics = GamePhysics()

    def __init_pygame(self):
        pygame.init()
        self.__screen = pygame.display.set_mode(self.__RESOLUTION)
        pygame.display.set_caption(self.__TITLE)

    def __load_resources(self):
        self.__background = pygame.Surface(self.__screen.get_size()).convert()
        self.__background.fill(self.__BG_COLOR)

        font = Resources.load_font(None, 36)
        text = font.render('A ball falling', True, (10, 10, 10))
        self.__background.blit(text, text.get_rect(centerx=self.__background.get_width()/2))

    def run(self):
        clock = pygame.time.Clock()
        allsprites = pygame.sprite.RenderPlain([Ground(self), Ball(self)])

        while True:
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == QUIT:
                    return
                elif event.type == KEYDOWN or event.type == KEYUP:
                    if event.key == K_ESCAPE:
                        return
                    self.game_input.process_key(event.key, event.type == KEYDOWN)

            self.game_physics.update()
            allsprites.update()

            self.__screen.blit(self.__background, (0, 0))
            allsprites.draw(self.__screen)
            pygame.display.flip()


def main():
    e = Engine()
    e.run()

if __name__ == '__main__':
    main()
