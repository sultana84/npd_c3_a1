import unittest
import exercise

class OutcomeTest(unittest.TestCase):

   def test_is_x_strings(self):
       x = exercise.Yourdict
       x.a = 'bananas'
       self.assertEqual(x.a, 'bananas')
       x.b = 'apples'
       self.assertNotEqual(x.b, 'cherries')

   def test_is_non_strings(self):
       x = exercise.Yourdict
       x.a = 'bananas'
       x.b = 'apples'
       self.assertIsNotNone(x.a, '1')
       self.assertIsNotNone(x.b, '2')
              
if __name__ == '__main__':
    unittest.main()
