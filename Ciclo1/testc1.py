import unittest
from   ciclo1 import verificarpalabraPalindroma

class Test(unittest.TestCase):

    def test_verificarpalabraPalindroma(self):
        self.assertTrue(verificarpalabraPalindroma("reconocer"))

        self.assertFalse(verificarpalabraPalindroma("carro"))
       

if __name__ == "__main__":
   unittest.main()