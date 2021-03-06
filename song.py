from typing import Dict, List
from audio_file import AudioFile
from usage_stats import UsageStats

class Song(AudioFile):
    """ Represents an abstract song, this is a subclass of the
        AudioFile class

    Name: Roy Ortega
    Set: 2B
    Date: January 31, 2020
    """

    def __init__(self, title: str, artist: str, runtime: str, path_name: str, album: str, genre: List = None):
        """Creates an object instance of the song subclass"""
        super().__init__(title, artist, runtime, path_name)
        self._album = album
        self._genre = genre
        self.__validate_song(album, genre)


    @staticmethod
    def __validate_song(album, genre):
        """Validates the song specific arguments"""
        if type(album) != str:
            raise ValueError('Album must be a string')
        elif genre is not None and (type(genre) != list):
            raise ValueError('Genre must either not be included or a list')
        else:
            return True

    def get_description(self) -> str:
        """Returns a string that includes the relevant song information"""
        song_info = "{} by {} from the album {} added on {}. Runtime is {}. Last played on {}."\
            .format(self._title, self._artist, self._album, self.get_usage_stats().date_added,
                    self._runtime, self.get_usage_stats().last_played)

        if self._genre is not None:
            genre_string = ''
            for i in self._genre:
                genre_string += ('"' + i + '"' + ', ')
            genre_string = genre_string.strip(', ')
            song_info += ' The song fits in the following genre(s) {}.'.format(genre_string)

        if self.user_rating is not None:
            song_info += " User rating is {}/5".format(self._user_rating)

        return song_info


    def meta_data(self) -> Dict:
        """Creates meta data for this specific song instance in the form of a dictionary"""
        self._song_dict = {}
        self._song_dict.update([('title', self._title), ('artist', self._artist), ('album', self._album),
                                ('date_added', self.get_usage_stats().date_added), ('runtime', self._runtime),
                                ('last_played', self.get_usage_stats().last_played), ('rating', self._user_rating),
                                ('genre', self._genre)])
        return self._song_dict

