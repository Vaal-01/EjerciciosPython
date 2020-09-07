import unittest
from ejercicio1 import validacion

class Test(unittest.TestCase):

    def test_validacion(self):
        self.assertTrue(validacion(14))
        self.assertFalse(validacion(31))

if __name__ == "__main__":
   unittest.main()
