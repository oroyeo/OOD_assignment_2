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
            description = "The library '{}' has {} audio files, ({} song and {} podcasts)"\
                .format(self._library_name,
                       len(self._audio_files),
                       len(self._songs),
                       len(self._podcasts))
        if len(self._podcasts) == 1:
            description = "The library '{}' has {} audio files, ({} songs and {} podcast)"\
                .format(self._library_name,
                       len(self._audio_files),
                       len(self._songs),
                       len(self._podcasts))
        if len(self._podcasts) == 1 and len(self._songs) == 1:
            description = "The library '{}' has {} audio files, ({} song and {} podcast)"\
                .format(self._library_name,
                       len(self._audio_files),
                       len(self._songs),
                       len(self._podcasts))

        else:
            if len(self._podcasts) == 1:
                description = "The library '{}' has {} audio files, ({} songs and {} podcasts)" \
                    .format(self._library_name,
                            len(self._audio_files),
                            len(self._songs),
                            len(self._podcasts))
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
        if type(filename) == AudioFile and filename in self._audio_files:
            self._audio_files.remove(filename)
            if type(filename) == Song and filename in self._songs:
                self._songs.remove(filename)
            elif type(filename) == Podcast and filename in self._podcasts:
                self._podcasts.remove(filename)
        else:
            raise ValueError('Entered filename is not an audio file')


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
        pass

    def unlike_audio_file(self, audio_file: AudioFile):
        pass

    def search(self, search_term: str):
        pass

    def get_number_of_audio_files(self) -> int:
        pass

    def list_audio_file(self) -> list:
        pass

    def list_podcasts(self) -> list:
        pass

    def list_songs(self) -> list:
        pass

    def get_library_info(self) -> str:
        pass

    def get_recently_played(self) -> list:
        pass
