
import unittest
from translator import  Translate_en_to_fr, Translate_fr_to_en

class TestTranslator(unittest.TestCase):
  def test_Translate_en_to_fr(self):
    self.assertEqual(Translate_en_to_fr('hello'),'bonjour')
    self.assertNotEqual(Translate_en_to_fr('hello'),'hello')
    
    
  def test_Translate_en_to_fr(self):
    self.assertEqual(Translate_fr_to_en('bonjour'),'hello')
    self.assertNotEqual(Translate_fr_to_en('bonjour'),'bonjour')
    
if __name__=='__main__':
  unittest.main()
