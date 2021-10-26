import pygame
from constants import *

class Circle:

    def __init__(self, location, rect):
        self.location = location
        self.rect = rect


class Cross:

    def __init__(self, location, rect):
        self.location = location
        self.rect = rect

class Square:

    def __init__(self, pos, rect):
        self.pos = pos
        self.rect = rect
