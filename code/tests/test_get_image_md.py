import unittest
from unittest.mock import patch, mock_open
from datetime import datetime
import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from get_image_md import get_image_date, get_image_name, get_absolute_path, get_image_md

class TestGetImageMd(unittest.TestCase):

    @patch('get_image_md.exifread.process_file')
    @patch('get_image_md.open', new_callable=mock_open)
    def test_get_image_date(self, mock_file, mock_process_file):
        mock_tags = {'EXIF DateTimeOriginal': mock_open(read_data='2021:01:01 12:00:00')}
        mock_process_file.return_value = mock_tags
        
        result = get_image_date('test.jpg')
        self.assertEqual(result, datetime(2021, 1, 1, 12, 0, 0))

    def test_get_image_name(self):
        result = get_image_name('/path/to/test.jpg')
        self.assertEqual(result, 'test.jpg')

    @patch('get_image_md.os.path.abspath')
    def test_get_absolute_path(self, mock_abspath):
        mock_abspath.return_value = '/absolute/path/to/test.jpg'
        result = get_absolute_path('test.jpg')
        self.assertEqual(result, '/absolute/path/to/test.jpg')

    @patch('get_image_md.get_image_date')
    @patch('get_image_md.get_image_name')
    @patch('get_image_md.get_absolute_path')
    def test_get_image_md(self, mock_get_absolute_path, mock_get_image_name, mock_get_image_date):
        mock_get_image_date.return_value = datetime(2021, 1, 1, 12, 0, 0)
        mock_get_image_name.return_value = 'test.jpg'
        mock_get_absolute_path.return_value = '/absolute/path/to/test.jpg'

        result = get_image_md('test.jpg')
        self.assertEqual(result, ('test.jpg', datetime(2021, 1, 1, 12, 0, 0), '/absolute/path/to/test.jpg'))

if __name__ == '__main__':
    unittest.main()
