# if, while, for, switch/case, functions, classes, exceptions, datatypes

# x = 23
# if x == 42:
#     print 'the universe is fine'
# elif x == 23:
#     print 'random string'
# else:
#     print 'else' 

# while x > 0:
#     x -= 1
#     print x

# for i in range(10):
#     print i

# def fun1(p1, p2):
#     print p1+p2

# fun1(1, 2)

# def throw1():
#     raise Exception("some error")

# class MyEx(Exception):
#     pass

# try:
#     throw1()
# except Exception as e:
#     print 'i have an exception::', e

#float, int, date, dict, list(vector)

# print 2.0
# print 2
# from datetime import datetime
# print datetime.now()
# print {1: 'value1', 2: 'value2'}
# print [1, 2, 3]

# x = {1: 'value1', 2: 'value2'}
# try:
#     print x[10]
# except KeyError as ke:
#     print 'i dont have the key: ', ke

# x[10] = ['this is dog', 10]
# print x[10]


# x = [1, 'a', 2, 3, 4]
# # print x[0]
# # print x[-1]
# # print x[:]
# y = x[:]
# y[0] = 42
# print x


# class BaseClass(object):
#     def __init__(self):
#         self.x = 42
#         self.init2()
#         print 'init base'

#     def init2(self):
#         self.x2 = self.x + 10
#         print 'base init2'

# class Class1(BaseClass):
#     def __init__(self, p):
#         super(Class1, self).__init__()
#         self.p = p

#     def init2(self):
#         print 'derived init2'

# c = Class1('this is p')
# b = BaseClass()

# print c.p

# x = (1, 2, 3)
# a1, a2, a3 = x
# print a1, a2
# a1, a2 = a2, a1
# print a1, a2

# x = lambda p: p+1
# print x(41)
# x = lambda: 42
# print x()


# def crash(n):
#     if n == 0:
#         return

#     print n
#     crash(n-1)

# crash(10)



# import os, sys
# import pygame
# from pygame.locals import *



# def load_image(name, colorkey=None):
#     fullname = os.path.join('assets', name)
#     try:
#         image = pygame.image.load(fullname)
#     except pygame.error as message:
#         print 'Cannot load image:', fullname
#         raise SystemExit, message

#     image = image.convert()
#     if colorkey is not None:
#         if colorkey is -1:
#             colorkey = image.get_at((0,0))
#         image.set_colorkey(colorkey, RLEACCEL)

#     return image, image.get_rect()

# class GameObject(pygame.sprite.Sprite):
#     def __init__(self, name):
#         super(GameObject, self).__init__()
#         self.image, self.rect = load_image(name)

#     def update(self):
#         raise NotImplementedError('abstract method')

# class Ball(GameObject):
#     def __init__(self):
#         super(Ball, self).__init__('ball.gif')
#         self.speed = [10, 10]

#     def update(self):
#         self.rect = self.rect.move(self.speed)
#         if self.rect.top < 0 or self.rect.bottom > 480:
#             self.speed[1] = -self.speed[1]
#         if self.rect.left < 0 or self.rect.right > 640:
#             self.speed[0] = -self.speed[0]


# # initialize
# pygame.init()

# screen = pygame.display.set_mode((640, 480))
# allsprites = pygame.sprite.RenderPlain([Ball()])
# background = pygame.Surface(screen.get_size()).convert()
# background.fill((163, 73, 164))

# def update():
#     allsprites.update()

# def render():
#     screen.blit(background, (0, 0))
#     allsprites.draw(screen)
#     pygame.display.flip()

# clock = pygame.time.Clock()
# def wait():
#     clock.tick(30)


# while True:
#     update()
#     render()
#     wait()



# def fun(*args, **kwargs):
#     print args
#     print kwargs

# fun(1, 2, param='p1')








































