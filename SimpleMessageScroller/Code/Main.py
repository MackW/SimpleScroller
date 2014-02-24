'''
Created on Feb 24, 2014

@author: mack
'''
import os, sys,random
import pygame
from pygame.locals import *

if not pygame.font: print 'Warning, fonts disabled'

class SimpleScroller:
    msg="This is a test Scrolling message  "
    def MainLoop(self): 
        clock=pygame.time.Clock()
        font = pygame.font.Font(None, 72)                                                                                        
        text = font.render(self.msg, 1, (0, 255, 0))                               
        textpos = text.get_rect(x=self.width,centery=278)
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    sys.exit()
            self.screen.fill((0,0,0),textpos)
            self.screen.blit(text, textpos)
            textpos = text.get_rect(x=textpos.x-2,centery=278)
            if (textpos.x) * -1 > textpos.width:
                textpos = text.get_rect(x=self.width,centery=278)
            pygame.display.flip()
            clock.tick(30)        
    
    def __init__(self, width=1024,height=768):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width
                                               , self.height))
if __name__ == "__main__":
    MainWindow = SimpleScroller()
    MainWindow.MainLoop()