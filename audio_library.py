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

    def add_audio_file(self, audio_file: AudioFile):
        pass

    def remove_audio_file(self, audio_file: AudioFile):
        pass

    def add_playlist(self, playlist: Playlist):
        pass

    def remove_playlist(self, playlist: Playlist):
        pass

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



