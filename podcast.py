from typing import Dict
from datetime import datetime, time
from audio_file import AudioFile


class Podcast(AudioFile):
    """ Represents an abstract podcast, this is a subclass of the
        AudioFile class

    Name: Roy Ortega
    Set: 2B
    Date: February 5, 2020
    """

    _PROGRESS_FORMAT = "%M"
    _DATE_FORMAT = "%Y-%m-%d"

    def __init__(self, title: str, artist: str, runtime: str, path_name: str, series: str,
                 episode_date: datetime, season: str = None, episode_number: int = None):
        """Creates an object instance of the song subclass"""
        super().__init__(title, artist, runtime, path_name)
        self._series = series
        self._season = season
        self._episode_date = episode_date
        self._progress = time(0,0,0)
        self._episode_number = episode_number
        self.__validate_podcast(series, episode_date, season, episode_number)
        self.__season_to_none(season)


    @staticmethod
    def __validate_podcast(series, episode_date, season, episode_number):
        """Validates podcast specific parameters"""
        if type(series) != str:
            raise ValueError('Series must be a string type')
        elif type(episode_date) != datetime:
            raise ValueError('Episode date must be a datetime type')
        elif season is not None and type(season) != str:
            raise ValueError('series and season must be a string')
        elif episode_number is not None and (type(episode_number) != int):
            raise ValueError('Episode number must either be not included or an integer')
        else:
            return True


    @property
    def series(self) -> str:
        """Returns the series of this podcast instance"""
        return self._series


    @property
    def season(self) -> str:
        """Returns the season of this podcast instance"""
        return self._season


    @property
    def progress(self) -> time:
        """Returns the progress for the specific podcast instance"""
        return self._progress


    @progress.setter
    def progress(self, new_progress: time):
        """Sets the progress to a different time"""
        if type(new_progress) is time:
            self._progress = new_progress.strftime("%M")
        else:
            raise ValueError('Argument is not of type datetime')


    def __season_to_none(self, season:str):
        """Turns the season to none if the user inputs '' to skip it"""
        if season == '':
            self._season = None

    def get_description(self) -> str:
        """Returns a string that includes the relevant song information"""
        date = self._episode_date.strftime("%B %d")
        progress_format = ''
        if self._progress == time(0, 0, 0):
            progress_format = '0'
        else:
            progress_format = self._progress

        podcast_description = ''

        if self._season is None and self._episode_number is not None:
            podcast_description = '{}: {}, {}, Episode {} ({} mins)'. format(
                self._series, self._title, date, self._episode_number, progress_format)

        elif self._episode_number is None and self._season is not None:
            podcast_description = '{}: {}, {}, Season {} ({} mins)'. format(
                self._series, self._title, date, self._season, progress_format)

        elif self._season is None and self._episode_number is None:
            podcast_description = "{}: {}, {} ({} mins)"\
                .format(self._series, self._title, date, progress_format)

        else:
            podcast_description = "{}: {}, {}, Season {} Episode {} ({} mins)"\
                .format(self._series, self._title, date, self._season,
                        self._episode_number, progress_format)

        return podcast_description


    def meta_data(self) -> Dict:
        """Creates meta data for this specific song instance in the form of a dictionary"""
        podcast_date = self._episode_date.strftime(Podcast._DATE_FORMAT)

        podcast_dict = {}
        podcast_dict.update([('title', self._title), ('artist', self._artist), ('series', self._series),
                                ('date_added', self.get_usage_stats().date_added), ('runtime', self._runtime),
                                ('last_played', self.get_usage_stats().last_played), ('rating', self._user_rating),
                                ('season', self._season), ('episode_date', podcast_date),
                                ('progress', self._progress), ('episode_number', self._episode_number)])

        return podcast_dict



