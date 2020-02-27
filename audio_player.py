from time import sleep
import vlc
import os

#os.add_dll_directory(r'C:\Program Files\VideosLAN\VLC')

def play_stuff(mp3_file):
    player = vlc.MediaPlayer(mp3_file)
    player.play()
    sleep(5)
    player.pause()
    sleep(3)
    player.pause()
    sleep(5)
    player.stop()

if __name__ == "__main__":
    mp3_file = r"C:\Users\llone\Desktop\BCIT LEVEL 1\ACIT 2515\assignment 1\OOD_assignment_2\Music\6.mp3"
    play_stuff(mp3_file)