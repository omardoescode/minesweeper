import pygame


class MusicPlayer:
    def __init__(self):
        # Initiate the music mixer
        pygame.mixer.init()
        pygame.mixer.set_num_channels(
            1000
        )  # TODO: Optimize this step to have dynamic number of channels as needed
        self.running_music = None
        self.is_muted = False

    # string -> ()
    # An abstract function for running any music infinitely, given its filename, and the number of loops
    # -1 means infinitely
    def play_music(self, filename, loops=1):
        pygame.mixer.music.load(rf"./assets/music/{filename}")
        pygame.mixer.music.play(loops, 0)
        self.running_music = filename

    # Play the music
    play_default_music = lambda self: self.play_music("default.mp3", -1)
    play_winning_music = lambda self: self.play_music("game_victory.mp3", -1)
    play_losing_music = lambda self: self.play_music("losing.mp3", -1)
    play_board_music = lambda self: self.play_music("board.mp3", -1)
    play_dig_sound = lambda self, channel: self.play_sound(
        channel, "./assets/music/dig.mp3"
    )
    play_flag_sound = lambda self, channel: self.play_sound(
        channel, "./assets/music/flag.mp3"
    )
    play_beep_sound = lambda self, channel: self.play_sound(
        channel, "./assets/music/explode.mp3"
    )
    play_correct_sound = lambda self, channel: self.play_sound(
        channel, "./assets/music/correct.mp3"
    )

    # Play the effects music
    def play_sound(self, channel, path, loop=0):
        pygame.mixer.Channel(channel).play(pygame.mixer.Sound(path), loops=loop)

    def stop_sound(self, channel):
        pygame.mixer.Channel(channel).stop()

    # string -> boolean
    # Check what file is playing as a background music
    def check_music(self, filename):
        return self.running_music == filename

    check_default_music = lambda self: self.check_music("default.mp3")

    # () -> ()
    # Mute the running music if not muted and vice versa
    def toggle_mute_music(self):
        # Toggle the mixer
        value = 1 if self.is_muted else 0
        pygame.mixer.music.set_volume(value)

        # Toggle the value
        self.is_muted = not self.is_muted
