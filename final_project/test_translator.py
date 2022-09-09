
import unittest
from translator import  Translate_en_to_fr, Translate_fr_to_en

class TestTranslator(unittest.TestCase):
    def test_Translate_en_to_fr_assertEqual(self):
        self.assertEqual(Translate_en_to_fr('hello'),'Bonjour')
    
    def test_Translate_en_to_fr_assertNotEqual(self):
        self.assertNotEqual(Translate_en_to_fr('hello'),'hello')
        
    def test_Translate_fr_to_en_assertEqual(self):
        self.assertEqual(Translate_fr_to_en('bonjour'),'Hello')

    def test_Translate_fr_to_en_assertNotEqual(self):
        self.assertNotEqual(Translate_fr_to_en('bonjour'),'bonjour')
    
if __name__=='__main__':
  unittest.main()
