import pygame
class MusicPlayer:
    def __init__(self):
        # Initiate the music mixer
        pygame.mixer.init()
    

    # string -> ()
    # An abstract function for running any music infinitely, given its path
    def play_music(self,path):
        pygame.mixer.music.load(path)
        pygame.mixer.music.play(-1, 0)
    
    # Play the music
    # TODO: Change these paths to the proper paths once created
    play_default_music = lambda self: self.play_music('./assets/music/default.mp3')
    play_winning_music = lambda self: self.play_music('./assets/music/default.mp3')
    play_losing_music = lambda self: self.play_music('./assets/music/default.mp3')
    play_board_music = lambda self: self.play_music('./assets/music/default.mp3')