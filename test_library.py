import unittest
# import datetime
# from podcast import Podcast
# from audio_file import AudioFile
import inspect
from abc import abstractmethod

class TestLibrary(unittest.TestCase):
    """A class that holds the tests to be run for the library Class


        Roy Ortega - A01078553
        ACIT 2515 - Set B
        February 13, 2020
    """

    def setUp(self):
        """Sets up each test by initializing default objects"""
        self.logPoint()
        self.library_default = Library(args)

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
        self.assertIsInstance(self.library_default, Library)


    def test_constructor_valid(self):
        """TP-010B Tests for a valid parameter """
        self.assertRaises(ValueError, Library, 'test', 'test')




if __name__ == '__main__':
    unittest.main()

