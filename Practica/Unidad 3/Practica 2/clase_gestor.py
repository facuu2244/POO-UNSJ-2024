import csv
from clase_autobus import autobus
from clase_van import van

class g_vehiculos():
    __vehiculos:list
    
    def __init__(self):
        self.__vehiculos=[]
        
    def cargar(self, ruta):
        with open(ruta, "r") as archivo:
            reader=csv.reader(archivo, delimiter=";")
            next(reader)
            
            for fila in reader:
                if fila[0]=="A":
                    marca, modelo, anio, capacidad, num, distancia, tarifa, tipo, turno=fila[1], fila[2], fila[3], fila[4], fila[5], fila[6], fila[7], fila[8], fila[9]
                    
                    un_autobus=autobus(marca, modelo, anio, capacidad, num, distancia, tarifa, tipo, turno)
                    self.__vehiculos.append(un_autobus)
                    
                else: 
                    marca, modelo, anio, capacidad, num, distancia, tarifa, carroseria=fila[1], fila[2], fila[3], fila[4], fila[5], fila[6], fila[7], fila[8]
                    
                    una_van=van(marca, modelo, anio, capacidad, num, distancia, tarifa, carroseria)
                    self.__vehiculos.append(una_van)
                    
    def agregar(self):
        vehiculo=input("Tipo de vehiculo que se quiere agregar: ")
        if vehiculo.lower()=="Autobus":
            marca=input("Marca: ")
            modelo=input("Modelo: ")
            anio=int(input("Año de fabricacion: "))
            capacidad=input("Capacidad de pasajeros: ")
            num=input("Numero de plazas: ")
            distancia=input("Distancia recorrida: ")
            tarifa=input("Tarifa  base: ")
            tipo=input("Tipo de servicio: ")
            turno=input("Marca: ")

            un_autobus=autobus(marca, modelo, anio, capacidad, num, distancia, tarifa, tipo, turno)
            self.__vehiculos.append(un_autobus)
            print("\nVehiculo agregado")
            
        elif vehiculo.lower()=="van":
            marca=input("Marca: ")
            modelo=input("Modelo: ")
            anio=input("Año de fabricacion: ")
            capacidad=input("Capacidad de pasajeros: ")
            num=input("Numero de plazas: ")
            distancia=input("Distancia recorrida: ")
            tarifa=input("Tarifa  base: ")
            carroseria=input("Tipo de carroseria: ")

            una_van=van(marca, modelo, anio, capacidad, num, distancia, tarifa, carroseria)
            self.__vehiculos.append(una_van)
            print("\nVehiculo agregado")

        else:
            print("Tipo de vehiculo incorrecto")
            
    def consultar(self):
        try:
            indice=int(input("Posicion de la lista que se quiere consultar: "))
            assert indice>0 and indice<=len(self.__vehiculos)
            
            if isinstance(self.__vehiculos[indice-1], autobus):
                print(f"\nEl objeto en la posicion {indice} es un autobus")
                
            else:
                print(f"\nEl objeto en la posicion {indice} es una van")
            
        except AssertionError:
            print("\nIndice fuera de rango de la lista")
            
        except ValueError:
            print("\nTipo de dato incorrecto, se esperaba un entero")
            
            
    def contar(self):
        cont_auto=0
        cont_van=0
        
        for vehiculo in self.__vehiculos:
            if isinstance(vehiculo, autobus):
                cont_auto+=1
            else:
                cont_van+=1
                
        print(f"\nHay un total de {cont_auto} autobuses y {cont_van} vanes")
        
    def mostrar(self):
        
        for vehiculo in self.__vehiculos:
            tarifa=vehiculo.calcular_tarifa()
            vehiculo.mostrar_datos(tarifa)