from clase_servicios import servicio

class embalaje(servicio):
    __precio_unidad:float
    __peso_unidad:float
    __cant_unidades:int
    
    def __init__(self, empresa, contratante, direc, fecha, precio_unidad, peso_unidad, cant):
        super().__init__(empresa, contratante, direc, fecha)
        self.__precio_unidad=precio_unidad
        self.__peso_unidad=peso_unidad
        self.__cant_unidades=cant
        
    def costo(self):
        total=(self.__precio_unidad*self.__cant_unidades)*1.1
        return total    
    
    def dar_peso_unidad(self):
        return self.__peso_unidad