from typing import Dict
from datetime import datetime, time
from audio_file import AudioFile
from song import Song
from playlist import Playlist
from podcast import Podcast

class Audio_Library():
    """ Represents an abstract audio library, this is a subclass of the
        AudioFile class

    Name: Roy Ortega, Adrian Chan, Nathan Broyles
    Set: 2B
    Date: February 25, 2020
    """

    _PROGRESS_FORMAT = "%M"
    _DATE_FORMAT = "%Y-%m-%d"

    def __init__(self, title: str, artist: str, runtime: str, path_name: str, series: str,
                 episode_date: datetime, season: str = None, episode_number: int = None):
        """Creates an object instance of the song subclass"""



    