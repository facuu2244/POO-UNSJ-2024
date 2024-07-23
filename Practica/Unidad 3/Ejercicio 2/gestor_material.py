import csv
from clase_material_refactado import material_refac

class gestor_mat:
    __gestor_materiales:list
    
    def __init__(self) :
        self.__gestor_materiales=[]
    
    def carga(self, ruta):
        with open(ruta, "r") as archi_mat:
            reader=csv.reader(archi_mat, delimiter=";")
            next(reader)
            for fila in reader:
                mat, caract, cant, costo=fila
                un_material=material_refac(mat, caract, cant, costo)
                self.__gestor_materiales.append(un_material)
                
    def dar_long(self):
        return len(self.__gestor_materiales)
    def buscar_mat(self, mat_random):
        return self.__gestor_materiales[mat_random]