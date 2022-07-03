from factorial import factorial

if __name__ == '__main__':
    
    import unittest
    
    class TestFactorial(unittest.TestCase):
        
        def test_type(self):
            self.assertRaises(TypeError, factorial, 1.25)
            
        def test_negative_value(self):
            self.assertRaises(ValueError, factorial, -1)
            
        def test_value(self):
            self.assertEqual(factorial(5), 120)
            self.assertEqual(factorial(6), 720)
            self.assertEqual(factorial(10), 3628800)
            
    unittest.main(verbosity=1)
