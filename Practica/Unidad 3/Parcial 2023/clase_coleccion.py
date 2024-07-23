from clase_nodo import nodo
from clase_embalaje import embalaje
from clase_transporte import transporte
from testing import test

class coleccion:
    __comienzo:nodo
    
    def __init__(self):
        self.__comienzo=None
    
    def cargar(self, servicio):
        try:
            if servicio.lower()=="transporte":
                empresa=input("Nombre de la empresa: ")
                contratante=input("Nombre del contratante: ") 
                direc=input("Direccion del contratante: ")
                fecha=input("Fecha del servicio: ")
                precio_hora=float(input("Precio por hora del servicio: ")) 
                peso=float(input("Peso de la carga: ")) 
                direc_destino=input("Direccion de destino: ")
                
                un_transporte=transporte(empresa, contratante, direc, fecha, precio_hora, peso, direc_destino)
                un_nodo=nodo(un_transporte)
                un_nodo.set_siguiente(self.__comienzo)
                self.__comienzo=un_nodo
                
                print("\nServicio transporte agregado\n")
                
            else:
                empresa=input("Nombre de la empresa: ")
                contratante=input("Nombre del contratante: ") 
                direc=input("Direccion del contratante: ")
                fecha=input("Fecha del servicio: ")
                precio_unidad=float(input("Precio por unidad a embalar: ")) 
                peso_unidad=float(input("Peso de la unidad: ")) 
                cant=int(input("Numero de unidades a embalar: "))
                
                un_embalaje=embalaje(empresa, contratante, direc, fecha, precio_unidad, peso_unidad, cant)
                un_nodo=nodo(un_embalaje)
                un_nodo.set_siguiente(self.__comienzo)
                self.__comienzo=un_nodo
        
                print("\nServicio embalaje agregado\n")
        
        except ValueError:
            print("El tipo de dato ingresado fue incorrecto")
    
        #Test para verificar que la carga funciono
        prueba=test()
        prueba.test_item1(self.__comienzo)
        
        
    def mostrar_transportes(self):
        aux=self.__comienzo
        listado=[]#Guardo en una lista todos los transportes para luego ordenarlos
        print("Servicios de transportes realizados: \n")
        print("Contratante              Costo total")
        while aux!=None:#Cargo la lsita
            if isinstance(aux.dar_servicio(), transporte):
                listado.append(aux.dar_servicio())
                
            aux=aux.dar_siguiente()
        
        listado.sort()
        
        for servicio in listado:#Muestro la lista ordenada
            servicio.mostrar()    
            
    def embalajes(self):
        aux=self.__comienzo
        cont_embalajes=0
        while aux!=None:
            servicio=aux.dar_servicio()
            if isinstance(servicio, embalaje) and servicio.dar_peso_unidad()>50:
                    cont_embalajes+=1
                    
            aux=aux.dar_siguiente()
                    
        print(f"Hay un total de {cont_embalajes} servicios de embalaje cuyo peso por unidad supera los 50kg")
        
        
    def mas_contrataciones(self):
        cont_transportes=0
        cont_embalajes=0
        fecha=input("Fecha de prestacion de servicio: ")
        
        aux=self.__comienzo
        while aux!=None:
            servicio=aux.dar_servicio()
            if servicio.dar_fecha()==fecha:#Verifica que la fecha del servicio sea igual a la ingresada
                if isinstance(servicio, transporte):#Si lo es, verifica si es un transporte o embalaje
                    cont_transportes+=1
                else:
                    cont_embalajes+=1
                    
            aux=aux.dar_siguiente()
        
        if cont_transportes>cont_embalajes:
            print(f"Los servicios de transporte fueron los mas prestados en esa fecha, con un total de {cont_transportes}")
        elif cont_embalajes>cont_transportes:
            print(f"Los servicios de embalaje fueron los mas prestados en esa fecha, con un total de {cont_embalajes}")
        else:
            print("Se realizaron la misma cantidad de transportes que de embalajes")