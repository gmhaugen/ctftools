import unittest
import sys
sys.path.append("..")
from tools import base64encdec

class TestBase64encdec(unittest.TestCase):
    def test_encode(self):
        self.assertEqual(base64encdec.encode("hello world"), "aGVsbG8gd29ybGQ=")
    
    def test_decode(self):
        self.assertEqual(base64encdec.decode("aGVsbG8gd29ybGQ="), "hello world")