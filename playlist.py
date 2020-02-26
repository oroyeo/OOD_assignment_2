from datetime import datetime
from usage_stats import UsageStats
from song import Song
from typing import List

class Playlist:
    """ Represents an abstract playlist

    Name: Roy Ortega
    Set: 2B
    Date: January 23, 2020
    """

    def __init__(self, name:str, description: str):
        """Creates a new instance of a playlist"""
        self._name = name
        self._description = description
        self._playlist = []
        self._usage = UsageStats(datetime.now())
        self.__validate_info(name, description)


    @staticmethod
    def __validate_info(name: str, description: str):
        """Validates values of the arguments on creation of the playlist"""
        if type(name) != str or type(description) != str:
            raise ValueError('Value Error: One or more of your arguments is not a string')


    @property
    def name(self) -> str:
        """Gets the current name of the playlist instance"""
        return self._name


    @name.setter
    def name(self, new_name: str):
        """Sets a new name for this specific playlist instance"""
        if type(new_name) == str:
            self._name = new_name
        else:
            raise ValueError('input must be of type (str)')


    @property
    def description(self) -> str:
        """Gets the current description for the instance playlist"""
        return self._description


    @description.setter
    def description(self, new_description: str):
        """Sets a new description for the playlist instance"""
        if type(new_description) == str:
            self._description = new_description
        else:
            raise ValueError('input must be of type (str)')


    def add_song(self, song: Song, posn: int = None):
        """Adds a song to the playlist instance"""

        if type(song) != Song or type(posn) == str:
            raise ValueError('song is not a string or posn is not an int')

        if posn is None:
            self._playlist.append(song)

        elif type(song) == Song or (type(posn) == int and type(posn) is not None) :
            if posn < 0:
                raise IndexError('Integer entered must be above 0')
            else:
                self._playlist.insert(posn, song)


    def remove_song(self, song:Song):
        """Removes a song from the specific playlist instance"""
        if song not in self._playlist:
            raise ValueError("song does not exist in the playlist")

        if type(song) == Song:
            self._playlist.remove(song)
        else:
            raise ValueError("song should be entered as a string")


    def move_song(self, song: Song, posn: int):
        """Moves a song to a new position within this playlist instance"""

        if type(song) != Song or type(posn) != int:
            raise ValueError('song must be of type (str) and position of type (int)')

        elif song not in self._playlist:
            print('Song does not exist, please check the spelling of your song')
        else:
            self.remove_song(song)
            self.add_song(song, posn)

            if posn > len(self._playlist): # Adds the song to the end if the specified value is greater than the index
                self.add_song(song)


    def list_songs(self) -> List:
        """Lists the song titles within the playlist"""
        posn = 0
        song_list = []
        print("   {:20} {:20} {:20} {}".format('Title', 'Artist', 'Album', 'Runtime'))
        while posn < len(self._playlist):
            current_song = self._playlist[posn]
            current_song = current_song.meta_data()
            number = posn + 1
            title = current_song['title']
            artist = current_song['artist']
            album = current_song['album']
            runtime = current_song['runtime']
            song_list.append("{}. {:<20} {:<20} {:<20} {}".format(number, title, artist, album, runtime))
            posn += 1
        return song_list


    def find_song(self, title: str = None, artist: str = None, album: str = None) -> int or None: # Doesn't work
        """Finds a song by title, artist, or album within this playlist instance"""
        intersect_set = set()

        if title is None and artist is None and album is None:
            raise ValueError('you need at least one argument to search for the')
        else:
            title_set = set()
            artist_set = set()
            album_set = set()
            posn = 0
            while posn < len(self._playlist):
                current_song = self._playlist[posn]
                if type(title) == str and title.lower() == current_song.title.lower():
                    title_set.add(current_song)
                elif type(artist) == str and artist.lower() == current_song.artist.lower():
                    artist_set.add(current_song)
                elif type(album) == str and album.lower() == current_song.album.lower():
                    album_set.add(current_song)
                posn += 1

            for song in title_set:
                intersect_set.add(song)
            for song in artist_set:
                intersect_set.add(song)
            for song in album_set:
                intersect_set.add(song)
            intersect_list = list(intersect_set)
            intersect_list.sort()

            if len(intersect_list) == 0:
                return None
            else:
                return self._playlist.index(intersect_list[0])


    def get_song_by_position(self, posn: int) -> Song:
        """Gets a song by it's position in the playlist instance"""
        if type(posn) == int and (0 <= posn < len(self._playlist)):
                return self._playlist[posn]
        elif (type(posn) == int and posn > len(self._playlist)) or (type(posn) == int and posn < 0):
            raise IndexError('position does not exist in the playlist, please check your input')
        else:
            raise ValueError('position must be an integer')


    def number_of_songs(self) -> int:
        """Returns the number of songs in the playlist"""
        return len(self._playlist)


    def update_usage_stats(self):
        """Updates the usage stats for this playlist instance"""
        self._usage.increment_usage_stats()


    def get_usage_stats(self) -> str:
        """Returns usage stats for the playlist instance"""
        date_added = self._usage.date_added
        last_played = self._usage.last_played
        play_count = self._usage.play_count
        stats = "The song was added on {}, and was last played on {}. Times played: {}".format(date_added,
                                                                                                     last_played,
                                                                                                     play_count)
        return stats