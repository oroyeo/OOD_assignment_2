import unittest
# import datetime
# from podcast import Podcast
# from audio_file import AudioFile
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
        self.librarydefault = Library(args)
        pass

    def tearDown(self):
        """Introduces an end log point for each test"""
        self.logPoint()


    def logPoint(self):
        """Creates the log point function to be run after each set up and tear down"""
        currentTest = self.id().split('.')[-1]
        callingFunction = inspect.stack()[1][3]
        print('in %s - %s()' % (currentTest, callingFunction))

    def test_van_darkholme(self):
        print('fuck you too')
