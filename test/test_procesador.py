import unittest
from src.procesador import Analizador

class TestAnalizador(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.analizador = Analizador("data/sri_ventas_2024.csv")

    def test_ventas_totales_como_diccionario(self):
        resumen = self.analizador.ventas_totales_por_provincia()
        self.assertIsInstance(resumen, dict)

    def test_ventas_totales_todas_las_provincias(self):
        resumen = self.analizador.ventas_totales_por_provincia()
        total_provincias = len(resumen)
        self.assertEqual(total_provincias, 24)

    def test_ventas_totales_mayores_5k(self):
        resumen = self.analizador.ventas_totales_por_provincia()
        todas_las_ventas_son_grandes = True 
 
        for venta in resumen.values():

            venta_flotante = float(venta)
            if venta_flotante <= 5000:
                todas_las_ventas_son_grandes = False 
                break         

        self.assertTrue(todas_las_ventas_son_grandes)

    def test_ventas_por_provincia_inexistente(self):
            with self.assertRaises(KeyError):
                self.analizador.ventas_por_provincia("Narnia")

    def test_ventas_por_provincia_existente(self):
            resultado = self.analizador.ventas_por_provincia("pichincha")
            self.assertGreater(resultado, 0)