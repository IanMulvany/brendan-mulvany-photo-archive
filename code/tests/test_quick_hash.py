import unittest
from unittest.mock import patch, mock_open
import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from quick_hash import get_md5_hash, get_perceptual_hash

class TestQuickHash(unittest.TestCase):

    @patch('quick_hash.open', new_callable=mock_open, read_data=b'test data')
    def test_get_md5_hash(self, mock_file):
        result = get_md5_hash('test.jpg')
        self.assertEqual(result, 'eb733a00c0c9d336e65691a37ab54293')

    @patch('quick_hash.Image.open')
    @patch('quick_hash.imagehash.phash')
    def test_get_perceptual_hash(self, mock_phash, mock_image_open):
        mock_phash.return_value = 'test_hash'
        result = get_perceptual_hash('test.jpg')
        self.assertEqual(result, 'test_hash')

if __name__ == '__main__':
    unittest.main()
