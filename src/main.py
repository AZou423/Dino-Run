import pygame
from controller import Controller
from player import Player
from obstacles import Obstacles


def main():
    #initialize pygame, create instance of controller object, call mainloop through controller
    
    pygame.init()
    game_controller = Controller()
    game_controller.mainloop()


# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()
