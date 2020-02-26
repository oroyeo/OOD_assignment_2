from audio_library import AudioLibrary


def main():
    library1 = AudioLibrary('libarry')
    print(library1.library_name)
    library1.library_name = '12312312321'
    print(library1.library_name)






if __name__ == "__main__":
    main()