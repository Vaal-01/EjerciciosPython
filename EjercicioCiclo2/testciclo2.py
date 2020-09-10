import unittest

from ciclo2 import calcularaño


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(2077,calcularaño())
        
if __name__ == '__main__':
    unittest.main()