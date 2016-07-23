import unittest
import exercise

class OutcomeTest(unittest.TestCase):

   def test_is_x_values(self):
       x = exercise.Yourdict
       x.a = 'bananas'
       self.assertEqual(x.a, 'bananas')
       x.b = 'apples'
       self.assertNotEqual(x.b, 'cherries')
       
if __name__ == '__main__':
    unittest.main()
