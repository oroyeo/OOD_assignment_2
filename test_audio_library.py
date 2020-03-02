import unittest
# import datetime
# from podcast import Podcast
# from audio_file import AudioFile
import inspect
from audio_library import AudioLibrary
from abc import abstractmethod

class TestLibrary(unittest.TestCase):
    """A class that holds the tests to be run for the library Class


        Roy Ortega - A01078553. Adrian Chan, Nathan Broyles
        ACIT 2515 - Set B
        February 13, 2020
    """

    def setUp(self):
        """Sets up each test by initializing default objects"""
        self.logPoint()
        self.library = AudioLibrary("test")

    def tearDown(self):
        """Introduces an end log point for each test"""
        self.logPoint()


    def logPoint(self):
        """Creates the log point function to be run after each set up and tear down"""
        currentTest = self.id().split('.')[-1]
        callingFunction = inspect.stack()[1][3]
        print('in %s - %s()' % (currentTest, callingFunction))

    def test_library_construction(self):
        """TP-010A Tests successful creation of a library class"""
        self.assertIsInstance(self.library, Library)


    def test_constructor_valid(self):
        """TP-010B Tests for a valid parameter"""
        self.assertRaises(ValueError, Library, 'test', 'test')

    def test_library_name_valid(self):
        """TP-020A Tests for a valid parameter"""
        self.assertEqual(type(self.library.name), str, "test_library_name should be type str")

    def test_library_name_invalid(self):
        """TP-020A Tests for a valid parameter"""
        with self.assertRaises(ValueError):
            self.library.name = 5

    def test_artist_valid(self):
        """TP-030A Tests for a valid paramenter"""
        self.assertEqual(type(self.library.artists), list, "library artists should be type list")
    
    def test_add_audio_file(self):
        """TP-040A Tests for a valid parameter"""
        self.library.add_audio_file()
        self.assertIn(test_audio_file, self.library.list_audio_files(), "test_audio_file should be added to Library")

    def test_add_audio_file_invalid(self):
        """TP-040B Tests for an invalid parameter"""
        with assertRaises(ValueError):
            self.library.add_audio_file("bad_test")

    def test_remove_audio_file_valid(self):
        """TP-050A Tests for a valid parameter"""
        self.library.add_audio_file(test_audio_file)
        self.library.remove_audio_file(test_audio_file)
        self.assertNotIn(test_audio_file, Library, "test_audio_file should not be in Library")

    def test_remove_audio_file_invalid(self):
        """TP-050B Tests for an invalid parameter"""
        with self.assertRaises(ValueError):
            self.library.remove_audio_file("bad_test")


    def test_add_playlist_valid(self):
        """TP-060A Tests for a valid parameter"""
        self.library.add_playlist(test_playlist)
        self.assertIn(test_playlist, self.library.playlists, "test_playlist shoud be added to Library")

    def test_add_playlist_invalid(self):
        """TP-060B Tests for an invaild parameter"""
        with self.assertRaises(ValueError):
            self.library.add_playlist("bad_test")
    
    def test_remove_playlist_valid(self):
        """TP-070A Tests for a valid parameter"""
        self.library.add_playlist(test_playlist)
        self.library.remove_playlist(test_playlist)
        self.assertNotIn(test_playlist, self.library.playlists, "test_playlist should not be in Library")
    
    def test_remove_playlist_invalid(self):
        """TP-070B Tests for an invalid parameter"""
        with self.assertRaises(ValueError):
            self.library.remove_playlist(5)


    def test_like_audio_file_valid(self):
        """TP-080A Tests for a valid parameter"""
        self.library.add_audio_file(test_audio_file)
        self.library.like_audio_file(test_audio_file)
        self.assertIn(test_audio_file, self.library._liked_audio_files, "test_audio_file should be in library._liked_audio_files")
    
    def test_like_audio_file_invalid(self):
        """TP-080B Tests for an invalid parameter"""
        with self.assertRaises(ValueError):
            self.library.like_audio_file('bad_test')
    
    def test_unlike_audio_file_valid(self):
        """TP-090A Tests for a valid parameter"""
        self.library.add_audio_file(test_audio_file)
        self.library.like_audio_file(test_audio_file)
        self.library.unlike_audio_file(test_audio_file)
        self.assertNotIn(test_audio_file, self.library._liked_audio_files,
                         "test_audio_file should not be in library._liked_audio_files")

    def test_unlike_audio_file_invalid(self):
        """TP-090B Tests for an invalid parameter"""
        with self.assertRaises(ValueError):
            self.library.unlike_audio_file("bad_test")

    def test_search_valid(self):
        """TP-100A Tests for a valid parameter"""
        self.library.add_audio_file(test_audio_file)
        self.library.search(test_audio_file)
        self.assertIn(test_audio_file, self.library.list_audio_files,
                      "test_audio_file is in library, search function works")

    def test_search_invalid(self):
        """TP-100B Tests for an invalid parameter"""
        with self.assertRaises(ValueError):
            self.library.search(5)
    
    def test_get_number_of_audio_files_valid(self):
        """TP-101A Tests for a valid output"""
        self.library.add_audio_file(test_audio_file)
        test_number = library.get_number_of_audio_files()
        self.assertEqual(type(test_number), int, "library.search() returns type int")
    
    def test_get_number_of_audio_files_invalid(self):
        """TP-101B Tests for an invalid output"""
        self.assertFalse(type(library.get_number_of_audio_files()) == str,
                         "library.search() does not return type int")

    def test_list_audio_files_valid(self):
        """TP-102A Tests for a valid output"""
        self.library.add_audio_file(test_audio_file)
        test_list = library.list_audio_files()
        self.assertTrue(type(test_list) == list, "library.list_audio_files() returns type list")
    
    def test_list_audio_files_invalid(self):
        """TP-102B Tests for an invalid output"""
        self.assertFalse(type(self.library.list_audio_files()) == list,
                         "library.list_audio_files() does not return type list")


    def test_list_podcasts(self):
        """TP-103A Tests for a valid list of podcasts"""
        self.assertTrue(type(self.library.list_podcasts()) == list, "Should be a list")

    def test_list_songs(self):
        """TP 104A Tests for a valid list of songs"""
        self.assertTrue(type(self.library.list_songs()) == list, "Should be a list")

    def test_get_library_info(self):
        """TP-105A Tests for a valid string return"""
        self.assertEqual(self.library.get_library_info() == str, "Should return a string")

    def test_get_recently_played(self):
        """TP-106A Tests for a valid return of the recently played list"""
        self.assertEqual(type(self.library.get_recently_played), str, "Should be a string")


if __name__ == '__main__':
    unittest.main()

