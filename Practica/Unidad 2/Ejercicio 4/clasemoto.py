class moto:
    __patente=""
    __marca=""
    __nya=""
    __km=int
    
    def __init__(self, patente, marca, nya, km):
        self.__patente=patente
        self.__marca=marca
        self.__nya=nya
        self.__km=km
    # def mostrar(self):
    #     return(self.__marca)
    def dar_patente(self):
        return self.__patente
    def dar_nya(self):
        return self.__nya
    
class gestor_motos:
    __gestor=list
    
    def __init__(self):
        self.__gestor=[]
    # def __str__(self):
    #     return(self.__gestor[2].mostrar())
    def cargar(self, una_moto):
        self.__gestor.append(una_moto)
    
    def validar_patente(self, patente_verif):
        band=False
        for moto in self.__gestor:
            patente=moto.dar_patente()
            if patente==patente_verif:
                band=True
                return(band)
        
        if band==False:
            return(band)
        
    def validar_conduct(self):
        '''Leer por una patente de una moto, mostrar los datos del conductor y el tiempo promedio 
        real de entrega de los pedidos que hizo.'''
        pate=input("Ingrese patente: ")
        ban=False
        i=0
        while ban==False and i<len(self.__gestor):
            if pate==self.__gestor[i].dar_patente():
                ban=True 
                print(self.__gestor[i].dar_nya())
                return self.__gestor[i].dar_patente()
            i+=1
        