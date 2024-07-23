import json
from clase_jugador import jugador

class gestor:
    __jugadores:list
    
    def __init__(self):
        self.__jugadores=[]
        
    def cargar(self):
        with open("pysimonpuntajes.json", "r") as archivo:
            lector=json.load(archivo)
            for jugadores in lector:
                nombre = jugadores["nombre"]
                puntos = jugadores["puntos"]
                fecha = jugadores["fecha"]
                hora = jugadores["hora"]
                un_jugador=jugador(nombre, puntos, fecha, hora)
                self.__jugadores.append(un_jugador)
                
    def ordenar(self):
        self.__jugadores.sort(reverse=True)
            
    def listar(self):
        lista=[]
        for jugador in self.__jugadores:
            lista.append(jugador.listar())
            
        return lista