import pygame
import os
import threading

class SoundPlayer:
    def __init__(self, sounds_folder="sounds"):
        self.sounds_folder = sounds_folder
        pygame.mixer.init()
        self.load_sounds()
    
    def load_sounds(self):
        self.sounds = {
            'personal': 'personal.mp3',
            'group': 'group.mp3', 
            'priority': 'priority.mp3'
        }
    
    def play_sound(self, sound_type):
        """Play sound based on message type"""
        if sound_type not in self.sounds:
            sound_type = 'personal'
        
        sound_file = os.path.join(self.sounds_folder, self.sounds[sound_type])
        
        if os.path.exists(sound_file):
            def play():
                try:
                    pygame.mixer.music.load(sound_file)
                    pygame.mixer.music.play()
                except Exception as e:
                    print(f"Error playing sound: {e}")
            
            sound_thread = threading.Thread(target=play)
            sound_thread.daemon = True
            sound_thread.start()
        else:
            print(f"Sound file not found: {sound_file}")

if __name__ == "__main__":
    # Test sound player
    sp = SoundPlayer()
    sp.play_sound('personal')