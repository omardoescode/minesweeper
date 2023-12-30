import pygame
class MusicPlayer:
    def __init__(self):
        pygame.mixer.init()
    
    def play_default_music(self):
        pygame.mixer.music.load("./assets/music/default.mp3")
        pygame.mixer.music.play(-1, 0)
