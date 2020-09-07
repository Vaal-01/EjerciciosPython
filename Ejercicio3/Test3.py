import unittest
from ejercicio3 import calcularDescuento

class Test(unittest.TestCase):

    def test_calcularDescuento(self):

        self.assertEquals(200.0,calcularDescuento(2000,"l"))
        self.assertEquals(0,calcularDescuento(10000,"s"))

        
if __name__ == "__main__":
   unittest.main()