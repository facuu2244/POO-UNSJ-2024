import unittest
from clase_servicios import servicio
from clase_embalaje import embalaje
from clase_transporte import transporte

class test(unittest.TestCase):
    def test_item1(self, comienzo):
        try:
            assert comienzo!=None
            print("\nCargado correctamente")
            
        except AssertionError:
            print("\nNo se cargo")