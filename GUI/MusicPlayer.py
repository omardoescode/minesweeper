import pygame
class MusicPlayer:
    def __init__(self):
        # Initiate the music mixer
        pygame.mixer.init()
    

    # string -> ()
    # An abstract function for running any music infinitely, given its path, and the number of loops
    # -1 means infinitely
    def play_music(self,path, loops):
        pygame.mixer.music.load(path)
        pygame.mixer.music.play(loops, 0)
    
    # Play the background music
    # TODO: Change these paths to the proper paths once created
    play_default_music = lambda self: self.play_music('./assets/music/default.mp3', -1)
    play_winning_music = lambda self: self.play_music('./assets/music/default.mp3', -1)
    play_losing_music = lambda self: self.play_music('./assets/music/default.mp3', -1)
    play_board_music = lambda self: self.play_music('./assets/music/default.mp3', -1)

    # Play the effects music
    # TODO: Add the music for flagged, unflagging, digging, start of a zero_chain, and so on
    # TODO: They all must be of loops=1