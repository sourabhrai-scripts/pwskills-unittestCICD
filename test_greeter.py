import unittest
from greeter import Greeter

class TestGreeter(unittest.TestCase):
    
    def test_say_hello(self):
        g = Greeter("Sourabh")
        self.assertEqual(g.say_hello(),"Hello, Sourabh!")


if __name__ == "__main__":
    unittest.main()
