import pygame
class MusicPlayer:
    def __init__(self):
        # Initiate the music mixer
        pygame.mixer.init()
        pygame.mixer.set_num_channels(1000)
    

    # string -> ()
    # An abstract function for running any music infinitely, given its path
    def play_music(self,path):
        pygame.mixer.music.load(path)
        pygame.mixer.music.play(-1, 0)
    
    def play_sound(self,channel, path, loop=0):
        pygame.mixer.Channel(channel).play(pygame.mixer.Sound(path), loops=loop)

    def stop_sound(self,channel):
        pygame.mixer.Channel(channel).stop()
        
    # Play the music
    # TODO: Change these paths to the proper paths once created
    play_default_music = lambda self: self.play_music('./assets/music/default.mp3')
    play_winning_music = lambda self: self.play_music('./assets/music/default.mp3')
    play_losing_music = lambda self: self.play_music('./assets/music/default.mp3')
    play_board_music = lambda self: self.play_music('./assets/music/default.mp3')
    play_dig_sound = lambda self, channel: self.play_sound(channel, './assets/music/dig.mp3')
    play_flag_sound = lambda self, channel: self.play_sound(channel, './assets/music/flag.mp3')
    play_beep_sound = lambda self, channel: self.play_sound(channel, './assets/music/beep.mp3')