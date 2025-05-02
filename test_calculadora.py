import unittest
from calculadora import multiplicar_numeros

class TestMultiplicacion(unittest.TestCase):
    
    def test_multiplicacion_correcta(self):
        self.assertEqual(multiplicar_numeros(3, 4), 12)  # Test verdadero

    def test_multiplicacion_incorrecta(self):
        self.assertNotEqual(multiplicar_numeros(3, 4), 10)  # Test falso (intencional para comprobar fallo)

if __name__ == '__main__':
    unittest.main()