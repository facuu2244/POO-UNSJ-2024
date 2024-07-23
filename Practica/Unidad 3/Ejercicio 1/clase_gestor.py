from clase_edificio import edificio
from clase_edificio import departamento
import csv

class gestor:
    __gestor:list
    
    def __init__(self) -> None:
        self.__gestor=[]
        
    def cargar(self, ruta):
        with open(ruta, "r") as archi:
            reader=csv.reader(archi, delimiter=";")
            i=-1
            for fila in reader:
                if len(fila)==6:
                    i+=1
                    id,nom,direc,empr,pisos,deptos=fila
                    un_edificio=edificio(int(id),nom,direc,empr,int(pisos),int(deptos))
                    self.__gestor.append(un_edificio)
                else: 
                    _,id,nya,piso,dept,habi,banos,sup=fila
                    self.__gestor[i].agregar_depto(int(id),nya,int(piso),int(dept),int(habi),int(banos),float(sup))
                    
    def validar(self, edif):
        band=False
        i=0
        while band==False and i<len(self.__gestor):
            if edif==self.__gestor[i].dar_nombre():
                band=True
            i+=1
            
        return band, i-1 
    
    def mostrar_deptos(self, i):
        self.__gestor[i].mostrar_deptos()
        
    def mostrar_sup(self, i):
        print(f"La superficie cubierta por el edificio es: {self.__gestor[i].calc_sup()} metros cuadrados")
        
    def tam_depto(self):
        propi=input("Nombre del propietario>> ")
        for edif in self.__gestor:
            sup=edif.buscar_propi(propi)
            if sup !=None:
                total=edif.calc_sup()
                porcentaje=(sup*100)/total
                print(f"Lo que representa el {porcentaje:.2f}% de la superficie total del edificio")
        if sup==None:
            print("Propietario no encontrado")
            
    def buscar_deptos(self):
        piso=int(input("Ingrese numero de piso >> "))
        if piso>3 or piso<1:
            print("Piso invalido")
        
        else:
            cont=0
            for edif in self.__gestor:
                print(f"\nLos siguientes departamentos tienen 3 dormitorios y mas de un baño en el edificio {edif.dar_nombre()}:")
                cont+=edif.filtar_deptos(piso)
            
            print(f"\nEn total: {cont} departamentos cumplen estos requisitos")
            
    def eliminar(self):
        for edi in self.__gestor:
            del edi