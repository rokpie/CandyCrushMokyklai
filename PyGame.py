import sys
import pygame as p
from Candy import *
p.init()

screen = p.display.set_mode((800, 400))
p.display.set_caption("Candy")

while True:
    for event in p.event.get():
        if event.type == p.QUIT:
            p.quit()


