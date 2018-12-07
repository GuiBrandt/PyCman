import pygame
from enum import Enum

class Sound(Enum):
    """Enumeração de tipos de tile no mapa"""
    WAKA_SOUND = 0
    POWER_SOUND = 1
    DIE_SOUND = 2

class AudioManager:

    __SOUND_DICT = {
        Sound.WAKA_SOUND : './assets/wakawaka.wav',
        Sound.POWER_SOUND : './assets/power.wav',
        Sound.DIE_SOUND : './assets/pacman_death.wav',
    }

    def init():
        for sound in range(0, 3):
            pygame.mixer.Channel(sound).load(AudioManager.__SOUND_DICT[sound])
    
    def play_sound (sound):
        for i in range(0, 3):
            pygame.mixer.music.stop()

        if sound == Sound.DIE_SOUND:
            pygame.mixer.music.load(AudioManager.__SOUND_DICT[sound])
            pygame.mixer.music.play(0)
        else:
            pygame.mixer.music.load(AudioManager.__SOUND_DICT[sound])
            pygame.mixer.music.play(-1)