from audio_library import AudioLibrary
from song import Song
from audio_file import AudioFile
from podcast import Podcast


def main():
    library1 = AudioLibrary('libarry')
    print(library1.library_name)
    library1.library_name = '12312312321'
    song1 = Song('Crazy', 'Gnarls Barkley', '3:02', r".\Music\Crazy.mp3", 'St. Elsewhere')
    print(type(song1))
    print(library1)
    library1.add_audio_file(song1)
    print(library1)
    print(library1._songs, library1._audio_files)





if __name__ == "__main__":
    main()