import unittest
from ejercicio2 import caracteres

class Test(unittest.TestCase):

    def test_caracteres(self):
        #El 'Fallido'
       # self.assertEquals("El primer caracter es: A y el último es: p",caracteres("Arquitectura"))
        #El 'Correcto'
        self.assertEquals("El primer caracter es: A y el último es: a",caracteres("Arquitectura"))

if __name__ == "__main__":
   unittest.main()