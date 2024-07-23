import csv
from clase_ladrillo import ladrillo
import random
class gestor_lad:
    __gestor_ladrillos:list
    
    def __init__(self) :
        self.__gestor_ladrillos=[]
        
    def carga(self, ruta):
        with open(ruta, "r") as archi_lad:
            reader=csv.reader(archi_lad, delimiter=";")
            next(reader)
            for fila in reader:
                cant, id, mat, costo=fila
                un_ladrillo=ladrillo(cant, id, mat, costo)
                self.__gestor_ladrillos.append(un_ladrillo)
                
    def asignar_materiales(self, materiales):
        #asignacion aleatoria de materiales refractados
        indice_lad=list(range(len(self.__gestor_ladrillos)))
        indice_mat=list(range(materiales.dar_long()))
        
        for i in range(3):#asigna 3 materiales aleatoriamente
            lad_random=random.choice(indice_lad)
            mat_random=random.choice(indice_mat)
            self.__gestor_ladrillos[lad_random].agregar_mat(materiales.buscar_mat(mat_random))
            
    def validar(self, id):
        band=False
        i=0
        while band==False and i<len(self.__gestor_ladrillos):
            if self.__gestor_ladrillos[i].dar_id()==id:
                band=True
                self.__gestor_ladrillos[i].dar_caract()
            i+=1
        return band
    
    def costo_pedido(self):
        print("")
        for lad in self.__gestor_ladrillos:
            lad.costo_total()

    def tabla(self):
        print("\nN° identificador                  Material/es                  Costo\n")
        for lad in self.__gestor_ladrillos:
            lad.datos_tabla()