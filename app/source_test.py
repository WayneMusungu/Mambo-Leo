import unittest
from models import sources

Source = sources.Source

class SourceTest(unittest.TestCase):
    '''
    Test class to test  of the source class
    '''
    def setUp(self):
        '''
        Method to run before every Test
        '''
        self.new_source= Source( "abc-news","ABC News","Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.","http://abcnews.go.com","en","us")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news))

if __name__ == '__main__':
    unittest.main() 