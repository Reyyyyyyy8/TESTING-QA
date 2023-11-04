import unittest

def my_function(n):
    return n**2

class TestMyFunction(unittest.TestCase):
    def test_my_function(self):
        self.assertEqual(my_function(3), 9)
        self.assertEqual(my_function(4), 16)
        self.assertEqual(my_function(5), 25)

if __name__ == '__main__':
    unittest.main()