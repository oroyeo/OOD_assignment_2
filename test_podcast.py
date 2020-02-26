import unittest
import datetime
from podcast import Podcast
from audio_file import AudioFile
import inspect

class TestPodcast(unittest.TestCase):
    """A class that holds the tests to be run


        Roy Ortega - A01078553
        ACIT 2515 - Set B
        February 13, 2020
    """

    def setUp(self):
        """Sets up each test by initializing default objects"""
        self.logPoint()
        self.podcastdefault = Podcast('Fight Companion #046', 'Joe Rogan', '240:00',
                           r'.\Podcasts\Fight Companion #046.mp3', 'The Joe Rogan Experience',
                           datetime.datetime(2020, 1, 9))
        self.podcastseason = Podcast('Fight Companion #046', 'Joe Rogan', '240:00',
                           r'.\Podcasts\Fight Companion #046.mp3', 'The Joe Rogan Experience',
                           datetime.datetime(2020, 1, 9), '2020')
        self.podcastall = Podcast('Fight Companion #046', 'Joe Rogan', '240:00',
                           r'.\Podcasts\Fight Companion #046.mp3', 'The Joe Rogan Experience',
                           datetime.datetime(2020, 1, 9), '2020', 17)

    def tearDown(self):
        """Introduces an end log point for each test"""
        self.logPoint()


    def logPoint(self):
        """Creates the log point function to be run after each set up and tear down"""
        currentTest = self.id().split('.')[-1]
        callingFunction = inspect.stack()[1][3]
        print('in %s - %s()' % (currentTest, callingFunction))


    def test_constructor_creation(self):
        """TP-010A Tests the successful creation of a Podcast and Audio class"""
        self.assertIsInstance(self.podcastdefault, Podcast)
        self.assertIsInstance(self.podcastseason, AudioFile)
        self.assertIsInstance(self.podcastseason, Podcast)
        self.assertIsInstance(self.podcastall, Podcast)

    def test_constructor_path(self):
        """TP-010B Tests for a valid file path"""
        self.assertRaises(FileNotFoundError, Podcast, 'Fight Companion #046', 'Joe Rogan', '240:00',
                          r'.\Pdcasts\Fight Companion #046.mp3', 'The Joe Rogan Experience',
         datetime.datetime(2020, 1, 9), '2020', 17)


    def test_constructor_invalid(self):
        """TP-010C Tests invalid arguments of a Podcast"""
        self.assertRaises(ValueError, Podcast, 1, 'Joe Rogan', '240:00',
                          r'.\Podcasts\Fight Companion #046.mp3', 'The Joe Rogan Experience',
         datetime.datetime(2020, 1, 9), '2020', 17)
        self.assertRaises(TypeError, Podcast, 1, 'Joe Rogan', '240:00',
                          r'.\Podcasts\Fight Companion #046.mp3', 'The Joe Rogan Experience')


    def test_get_description_valid(self):
        """TP-020A Tests if the description returns a valid string"""
        self.assertEqual(type(self.podcastdefault.get_description()), str, "Should return a string")

    def test_get_description_output(self):
        """TP-020B Tests the proper output of a description"""
        self.assertEqual(self.podcastdefault.get_description(),
                         'The Joe Rogan Experience: Fight Companion #046, January 09 (0 mins)')
        self.assertEqual(self.podcastseason.get_description(),
                         'The Joe Rogan Experience: Fight Companion #046, January 09, Season 2020 (0 mins)')
        self.assertEqual(self.podcastall.get_description(),
                         'The Joe Rogan Experience: Fight Companion #046, January 09, Season 2020 Episode 17 (0 mins)')

    def test_getters(self):
        """TP-030A Tests that the Podcast getters provide the proper info"""
        self.assertEqual(self.podcastdefault.artist, 'Joe Rogan', 'Should be Joe Rogan')
        self.assertEqual(self.podcastdefault.title, 'Fight Companion #046', 'Should be The Fight Companion #046')
        self.assertEqual(self.podcastdefault.series, 'The Joe Rogan Experience', 'Should be The Joe Rogan Experience')
        self.assertEqual(self.podcastdefault.season, None, 'Should be None')
        self.assertEqual(self.podcastdefault.progress, datetime.time(0, 0), 'Should be None')
        self.assertEqual(self.podcastdefault.user_rating, None, 'Should be None')
        self.assertEqual(self.podcastdefault.runtime, '240:00', 'Should be 240:00')


    def test_getter_type(self):
        """TP-030B Tests that the Podcast getter types are the proper type"""
        self.assertEqual(type(self.podcastdefault.artist), str, 'Should be a string')
        self.assertEqual(type(self.podcastdefault.title), str, 'Should be a string')
        self.assertEqual(type(self.podcastdefault.series), str, 'Should be a string')
        self.assertIsNone(self.podcastdefault.season, 'Should be None')
        self.assertEqual(type(self.podcastdefault.progress), datetime.time, 'Should be None')
        self.assertIsNone(self.podcastdefault.user_rating, 'Should be None')
        self.assertEqual(type(self.podcastdefault.runtime), str, 'Should be a string')


    def test_setters(self):
        """TP-040A Tests that the Podcast setters properly set their corresponding values"""
        self.podcastdefault.progress = datetime.time(0, 5)
        self.podcastdefault.user_rating = 5

        self.assertEqual(self.podcastdefault.progress, '05', 'Should return a formatted datetime to 05')
        self.assertEqual(self.podcastdefault.user_rating, 5, 'Should be an integer of 5')

    # FIX THIS LOL
    def test_setter_value(self):
        """TP-040B Tests that the setters raise a value error if an improper value is entered"""
        with self.assertRaises(ValueError):
            self.podcastdefault.user_rating = '5'
        with self.assertRaises(ValueError):
            self.podcastdefault.progress = 12

    def test_meta_dict_type(self):
        """TP-050A Tests that the meta_dict method returns a dictionary"""
        self.assertEqual(type(self.podcastdefault.meta_data()), dict, 'Should be of a type dict')
    #
    def test_meta_dict_output(self):
        """TP-050B Tests that meta_dict returns the proper output"""
        self.assertEqual(self.podcastdefault.meta_data(), {'artist': 'Joe Rogan',
                         'date_added': '2020-02-12',
                         'episode_date': '2020-01-09',
                         'episode_number': None,
                         'last_played': None,
                         'progress': datetime.time(0, 0),
                         'rating': None,
                         'runtime': '240:00',
                         'season': None,
                         'series': 'The Joe Rogan Experience',
                         'title': 'Fight Companion #046'},
                         "Should be {'artist': 'Joe Rogan',date_added': '2020-02-12',"
                         "'episode_date': '2020-01-09','episode_number': None,'last_played': None,"
                         "'progress': datetime.time(0, 0),'rating': None,'runtime': '240:00','season': None,"
                         "'series': 'The Joe Rogan Experience','title': 'Fight Companion #046'}")

    def test_usage_stats_valid(self):
        """TP-060A Tests the Audiofile usagestats type """
        self.assertEqual(self.podcastdefault.get_usage_stats().play_count, 0)
        self.assertEqual(self.podcastdefault.get_usage_stats().last_played, None)
        self.assertEqual(self.podcastdefault.get_usage_stats().date_added, '2020-02-12')

        self.podcastdefault.update_usage_stats()

        self.assertEqual(self.podcastdefault.get_usage_stats().play_count, 1)
        self.assertEqual(self.podcastdefault.get_usage_stats().last_played, '2020-02-12')
        self.assertEqual(self.podcastdefault.get_usage_stats().date_added, '2020-02-12')

    def test_file_location(self):
        """TP-070A Tests the AudioFile file_location returns a string an proper output"""
        self.assertTrue(self.podcastdefault.file_location())
        self.assertEqual(type(self.podcastdefault.file_location()), str, 'Should be a string')
        self.assertEqual(self.podcastdefault.file_location(),
                         'The file (Fight Companion #046.mp3) is located in the path (.\Podcasts)',
                         'Should be The file (Fight Companion #046.mp3) is located in the path (.\Podcasts)')

    def test_lists(self):
        self.assertEqual(type(self.podcastdefault.meta_data()), dict, '')



if __name__ == '__main__':
    unittest.main()
