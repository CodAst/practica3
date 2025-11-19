import unittest
import os
from src.procesador import Analizador

class TestAnalizador(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Configuración inicial para todas las pruebas"""
        ruta_archivo = "datos/sri_ventas_2024.csv"
        cls.analizador = Analizador(ruta_archivo)
        cls.resumen_ventas = cls.analizador.ventas_totales_por_provincia()

    def test_0_debug_provincias(self):
        """Prueba temporal para ver las provincias reales"""
        print("\nProvincias encontradas:")
        for provincia in sorted(self.resumen_ventas.keys()):
            print(f"  '{provincia}'")

    def test_1_numero_provincias_coherente(self):
        """
        1. Validar que el número de provincias sea coherente.
        Ecuador tiene 24 provincias, pero los datos tienen 25 (incluyendo 'ND')
        """
        total_provincias = len(self.resumen_ventas)
        
        # Verificar que hay al menos 24 provincias (puede haber extras como 'ND')
        self.assertGreaterEqual(total_provincias, 24,
                              f"Se esperaban al menos 24 provincias, pero se encontraron {total_provincias}")

    def test_2_valores_numericos_no_negativos(self):
        """
        2. Verificar que los valores calculados sean numéricos y no negativos.
        """
        for provincia, total_ventas in self.resumen_ventas.items():
            # Verificar que es numérico
            self.assertIsInstance(total_ventas, (int, float),
                                f"El total de ventas para {provincia} no es numérico: {type(total_ventas)}")
            
            # Verificar que no es negativo
            self.assertGreaterEqual(total_ventas, 0,
                                  f"Las ventas de {provincia} son negativas: {total_ventas}")

    def test_3_retorna_diccionario(self):
        """
        3. Garantizar que la función retorne un diccionario.
        """
        resultado = self.analizador.ventas_totales_por_provincia()
        self.assertIsInstance(resultado, dict,
                            f"Se esperaba un diccionario, pero se obtuvo: {type(resultado)}")
        
        # Verificar que el diccionario no está vacío
        self.assertTrue(len(resultado) > 0, "El diccionario de ventas está vacío")

    def test_4_provincias_consultadas_existan(self):
        """
        4. Verificar que las provincias consultadas existan
        """
        # Provincias que SÍ deberían existir (en mayúsculas como están en los datos)
        provincias_validas = ["PICHINCHA", "GUAYAS", "AZUAY", "MANABI"]
        
        for provincia in provincias_validas:
            try:
                ventas = self.analizador.ventas_por_provincia(provincia)
                # Si no lanza excepción, la prueba pasa para esta provincia
                self.assertTrue(True)
            except KeyError:
                self.fail(f"La provincia '{provincia}' no existe en los datos")

    def test_4b_provincia_inexistente_lanza_excepcion(self):
        """
        4b. Verificar que provincias inexistentes lancen excepción
        """
        provincias_inexistentes = ["NARNIA", "WAKANDA", "MIDDLEEARTH"]
        
        for provincia in provincias_inexistentes:
            with self.assertRaises(KeyError, 
                                 msg=f"La provincia '{provincia}' no debería existir"):
                self.analizador.ventas_por_provincia(provincia)

    def test_5_valores_3_provincias_correctos(self):
        """
        5. Verificar que los valores consultados de 3 provincias sean correctos
        Compara los resultados individuales con los del resumen general
        """
        provincias_a_verificar = ["PICHINCHA", "GUAYAS", "AZUAY"]
        
        for provincia in provincias_a_verificar:
            # Obtener valor individual
            valor_individual = self.analizador.ventas_por_provincia(provincia)
            
            # Obtener valor del resumen general
            valor_resumen = self.resumen_ventas.get(provincia)
            
            # Verificar que ambos valores son iguales
            self.assertEqual(valor_individual, valor_resumen,
                           f"Valor individual de {provincia} ({valor_individual}) no coincide con el del resumen ({valor_resumen})")
            
            # Verificar que el valor es positivo (las principales provincias deberían tener ventas)
            self.assertGreater(valor_individual, 0,
                             f"Las ventas de {provincia} deberían ser mayores a 0")

    def test_6_estructura_diccionario_correcta(self):
        """
        Prueba adicional: Verificar la estructura del diccionario
        """
        for provincia, total_ventas in self.resumen_ventas.items():
            # Verificar que el nombre de la provincia es string
            self.assertIsInstance(provincia, str,
                                f"El nombre de la provincia no es string: {type(provincia)}")
            
            # Verificar que el total es float o int
            self.assertIsInstance(total_ventas, (float, int),
                                f"El total de ventas no es numérico: {type(total_ventas)}")

if __name__ == "__main__":
    unittest.main()

    def test_7_exportaciones_por_mes_retorna_diccionario(self):
        """
        Prueba para exportaciones por mes: verificar que retorna un diccionario
        """
        resultado = self.analizador.exportaciones_totales_por_mes()
        self.assertIsInstance(resultado, dict)

    def test_8_exportaciones_por_mes_valores_no_negativos(self):
        """
        Prueba para exportaciones por mes: verificar valores no negativos
        """
        resultado = self.analizador.exportaciones_totales_por_mes()
        for mes, total in resultado.items():
            self.assertIsInstance(mes, str)
            self.assertGreaterEqual(total, 0)

    def test_9_exportaciones_por_mes_todos_los_mes(self):
        """
        Prueba para exportaciones por mes: verificar que hay 12 meses
        """
        resultado = self.analizador.exportaciones_totales_por_mes()
        self.assertEqual(len(resultado), 12)  # 12 meses del año

    def test_10_provincia_mayor_importaciones_retorna_tupla(self):
        """
        Prueba para provincia con mayor importaciones: verificar que retorna una tupla
        """
        resultado = self.analizador.provincia_mayor_importaciones()
        self.assertIsInstance(resultado, tuple)
        self.assertEqual(len(resultado), 2)  # (provincia, valor)

    def test_11_provincia_mayor_importaciones_valores_correctos(self):
        """
        Prueba para provincia con mayor importaciones: verificar tipos de datos
        """
        resultado = self.analizador.provincia_mayor_importaciones()
        if resultado:  # Solo si hay datos
            provincia, valor = resultado
            self.assertIsInstance(provincia, str)
            self.assertIsInstance(valor, (int, float))
            self.assertGreater(valor, 0)

    def test_12_provincia_mayor_importaciones_existe_en_datos(self):
        """
        Prueba para provincia con mayor importaciones: verificar que la provincia existe
        """
        resultado = self.analizador.provincia_mayor_importaciones()
        if resultado:
            provincia, valor = resultado
            # Verificar que la provincia existe en el resumen de ventas
            self.assertIn(provincia, self.resumen_ventas)