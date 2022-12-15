import unittest
import sys
sys.path.append("..")
from tools import hasher

class TestHasher(unittest.TestCase):
    def test_hashmd5(self):
        self.assertEqual(hasher.hashmd5("hello world"), "5eb63bbbe01eeed093cb22bb8f5acdc3")
    
    def test_hashsha1(self):
        self.assertEqual(hasher.hashsha1("hello world"), "2aae6c35c94fcfb415dbe95f408b9ce91ee846ed")
    
    def test_hashsha224(self):
        self.assertEqual(hasher.hashsha224("hello world"), "2f05477fc24bb4faefd86517156dafdecec45b8ad3cf2522a563582b")
    
    def test_hashsha256(self):
        self.assertEqual(hasher.hashsha256("hello world"), "b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9")
    
    def test_hashsha384(self):
        self.assertEqual(hasher.hashsha384("hello world"), "fdbd8e75a67f29f701a4e040385e2e23986303ea10239211af907fcbb83578b3e417cb71ce646efd0819dd8c088de1bd")
    
    def test_hashsha512(self):
        self.assertEqual(hasher.hashsha512("hello world"), "309ecc489c12d6eb4cc40f50c902f2b4d0ed77ee511a7c7a9bcd3ca86d4cd86f989dd35bc5ff499670da34255b45b0cfd830e81f605dcf7dc5542e93ae9cd76f")
    
    def test_hashsha3_224(self):
        self.assertEqual(hasher.hashsha3_224("hello world"), "dfb7f18c77e928bb56faeb2da27291bd790bc1045cde45f3210bb6c5")
    
    def test_hashsha3_256(self):
        self.assertEqual(hasher.hashsha3_256("hello world"), "644bcc7e564373040999aac89e7622f3ca71fba1d972fd94a31c3bfbf24e3938")
    
    def test_hashsha3_384(self):
        self.assertEqual(hasher.hashsha3_384("hello world"), "83bff28dde1b1bf5810071c6643c08e5b05bdb836effd70b403ea8ea0a634dc4997eb1053aa3593f590f9c63630dd90b")
    
    def test_hashsha3_512(self):
        self.assertEqual(hasher.hashsha3_512("hello world"), "840006653e9ac9e95117a15c915caab81662918e925de9e004f774ff82d7079a40d4d27b1b372657c61d46d470304c88c788b3a4527ad074d1dccbee5dbaa99a")