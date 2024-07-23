import unittest
from clase_publicacion import publicacion
from clase_cd import cd
from gestor_publicaciones import gestor_publis

class test(unittest.TestCase):
    def test_cd(self, gestor):
        try:
            self.assertEqual(gestor[5].dar_titulo(), "Los Pilares de la Tierra")
            print("Encontre")
        except AssertionError:
            print("no encontre")