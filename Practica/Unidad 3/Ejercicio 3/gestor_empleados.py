from clase_empleado import empleado
import csv

class gestor_empl:
    __empleados:list
    
    def __init__(self):
        self.__empleados=[]
        
    def cargar(self, ruta):
        with open (ruta, "r") as archivo:
            reader=csv.reader(archivo, delimiter=";")
            next(reader)
            
            for fila in reader:
                nya, id, puesto=fila
                un_empleado=empleado(nya, id, puesto)
                self.__empleados.append(un_empleado)
        
    def dar_cantidad(self):
        return len(self.__empleados)
    
    def dar_empl(self, i):
        return self.__empleados[i]
    
    
    def buscar(self, id):
        band=False
        i=0
        while band==False and i<len(self.__empleados):
            if self.__empleados[i].dar_id()==id:
                band=True
            else:
                i+=1
        
        return band, i
    
    def mostar_prog(self, i):
        self.__empleados[i].datos_prog()
        
    def empl_nomatri(self):
        nomatriculados=[]
        for empl in self.__empleados:
            nom=empl.verif_matriculacion()
            if nom!=None:
                nomatriculados.append(nom)
                
        if nomatriculados!=[]:
            
            print(f"\nEmpleados no matriculados en ningun programa: {nomatriculados}")
            
        else:
            print("Todos los empleados fueron matriculados en al menos un programa")