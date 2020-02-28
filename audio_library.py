from typing import Dict, List
from datetime import datetime, time
from audio_file import AudioFile
from song import Song
from playlist import Playlist
from podcast import Podcast


class AudioLibrary:
    """ Represents an abstract audio library, this is a subclass of the
        AudioFile class

    Name: Roy Ortega, Adrian Chan, Nathan Broyles
    Set: 2B
    Date: February 25, 2020
    """

    _PROGRESS_FORMAT = "%M"
    _DATE_FORMAT = "%Y-%m-%d"

    def __init__(self, library_name: str):
        """Creates an object instance of a library class"""
        self._library_name = library_name
        self._liked_audio_files = []
        self._audio_files = []
        self._songs = []
        self._podcasts = []
        self._playlists = []
        self._recently_played = []
        self._artists = []

    def __str__(self) -> str:
        """Could be the 'get_library_info' function since it returns the formatted string"""
        description = ''
        if len(self._songs) == 1:
            description = "The library '{}' has {} audio file(s), ({} song and {} podcasts)" \
                .format(self._library_name,
                        len(self._audio_files),
                        len(self._songs),
                        len(self._podcasts))
        if len(self._podcasts) == 1:
            description = "The library '{}' has {} audio file(s), ({} songs and {} podcast)" \
                .format(self._library_name,
                        len(self._audio_files),
                        len(self._songs),
                        len(self._podcasts))
        if len(self._podcasts) == 1 and len(self._songs) == 1:
            description = "The library '{}' has {} audio file(s), ({} song and {} podcast)" \
                .format(self._library_name,
                        len(self._audio_files),
                        len(self._songs),
                        len(self._podcasts))
        if len(self._podcasts) == 1:
            description = "The library '{}' has {} audio files, ({} songs and {} podcasts)" \
                .format(self._library_name,
                        len(self._audio_files),
                        len(self._songs),
                        len(self._podcasts))
        if len(self._audio_files) == 0:
            description = "The library '{}' has 0 audio files, (0 songs and 0 podcasts)".format(self._library_name)

        return description

    @staticmethod
    def __validate_library(library_name):
        """Validates library parameter argument"""
        if type(library_name) != str:
            raise ValueError('library name must be a string')

    @property
    def library_name(self) -> str:
        """Gets the current library name for this object instance"""
        return self._library_name

    @library_name.setter
    def library_name(self, new_name: str):
        """Sets a new name for this current object instance"""
        if type(new_name) != str:
            raise ValueError('new library name should be a string')
        else:
            self._library_name = new_name

    def add_audio_file(self, filename):
        """Adds an audio file to the library and its respective subclass list"""
        if not isinstance(filename, AudioFile):
            raise ValueError('Entered filename is not an audiofile')
        if filename not in self._audio_files:
            self._audio_files.append(filename)
            self.__add_song_helper(filename)
            self.__add_podcast_helper(filename)
        else:
            print('File already exists in your library')

    def __add_song_helper(self, filename):
        """Adds the file to the song list if it is a song"""
        if isinstance(filename, Song):
            if filename not in self._songs:
                self._songs.append(filename)

    def __add_podcast_helper(self, filename):
        """Adds the file to the song list if it is a song"""
        if isinstance(filename, Podcast):
            if filename not in self._podcasts:
                self._podcasts.append(filename)

    def remove_audio_file(self, filename):
        """Removes an audio file from the library and its respective subclass list"""
        if not isinstance(filename, AudioFile):
            raise ValueError('Entered filename is not an audiofile')
        if filename in self._audio_files:
            self._audio_files.remove(filename)
            self.__remove_song_helper(filename)
            self.__remove_podcast_helper(filename)
        else:
            print('File does not exist in your library')

    def __remove_song_helper(self, filename):
        if isinstance(filename, Song):
            self._songs.remove(filename)

    def __remove_podcast_helper(self, filename):
        if isinstance(filename, Podcast):
            self._podcasts.remove(filename)

    def add_playlist(self, playlist):
        """Adds a playlist to the library"""
        if isinstance(playlist, Playlist):
            if playlist not in self._playlists:
                self._playlists.append(playlist)
            else:
                print('Playlist already exists')
        else:
            raise ValueError('entered value is not a playlist')

    def remove_playlist(self, playlist):
        """Removes a playlist from the library"""
        if isinstance(playlist, Playlist):
            if playlist in self._playlists:
                self._playlists.remove(playlist)
            else:
                print('That playlist is not in your existing playlists')
        else:
            raise ValueError('argument is not a playlist object')

    def like_audio_file(self, audio_file: AudioFile):

        """Likes an audio file and adds it to the list"""
        if isinstance(audio_file, AudioFile):
            if audio_file not in self._liked_audio_files:
                self._liked_audio_files.append(audio_file)
            else:
                print('Audio file is already liked')
        else:
            raise ValueError('Argument is not an audio file')

    def unlike_audio_file(self, audio_file: AudioFile):
        """Unlikes an audio file by removing it from the liked audio files list"""
        if isinstance(audio_file, AudioFile):
            if audio_file in self._liked_audio_files:
                self._liked_audio_files.remove(audio_file)
            else:
                print('Audio file is not liked')
        else:
            raise ValueError('Argument is not an audio file')

    def search(self, search_term: str) -> int:
        """Finds a song by title, artist, or album within this library instance"""
        intersect_set = set()

        if search_term is None:
            raise ValueError('you need at least one argument to search')
        else:
            title_set = set()
            artist_set = set()
            album_set = set()
            posn = 0
            while posn < len(self._audio_files):
                current_file = self._audio_files[posn]
                if type(search_term) == str and search_term.lower() == current_file.title.lower():
                    title_set.add(current_file)
                elif type(search_term) == str and search_term.lower() == current_file.artist.lower():
                    artist_set.add(current_file)
                elif type(search_term) == str and search_term.lower() == current_file.album.lower():
                    album_set.add(current_file)
                posn += 1

            for audio_file in title_set:
                intersect_set.add(audio_file)
            for audio_file in artist_set:
                intersect_set.add(audio_file)
            for audio_file in album_set:
                intersect_set.add(audio_file)
            intersect_list = list(intersect_set)
            intersect_list.sort()

            if len(intersect_list) == 0:
                raise ValueError('No file found matching search term')
            else:
                return self._audio_files.index(intersect_list[0])

    def get_number_of_audio_files(self) -> int:

        return len(self._audio_files)

    def list_audio_file(self):
        num = 1
        if len(self._audio_files) > 0:
            print('Your current audio files are:')
            for file in self._audio_files:
                print('{}. {}'.format(num, file.title))
                num += 1
        else:
            print('You currently have no audio files')

    def list_songs(self):
        num = 1
        if len(self._songs) > 0:
            print('Your current audio files are:')
            for file in self._songs:
                print('{}. {}'.format(num, file.title))
                num += 1
        else:
            print('You currently have no songs')

    def list_podcasts(self):
        num = 1
        if len(self._podcasts) > 0:
            print('Your current audio files are:')
            for file in self._podcasts:
                print('{}. {}'.format(num, file.title))
                num += 1
        else:
            print('You currently have no podcasts')


    def get_recently_played(self):
        num = 1
        if len(self._recently_played) > 0:
            print('Your recently played audio files are:')
            for file in self._recently_played:
                print('{}. {}'.format(num, file.title))
                num += 1
        else:
            print('You have no recently played songs')


