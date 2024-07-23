from clase_servicios import servicio

class transporte(servicio):
    __precio_hora:float
    __peso_carga:float
    __direc_destino:str
    
    def __init__(self, empresa, contratante, direc, fecha, precio_hora, peso, direc_destino):
        super().__init__(empresa, contratante, direc, fecha)
        self.__precio_hora=precio_hora
        self.__peso_carga=peso
        self.__direc_destino=direc_destino
        
        
    def costo(self):
        total=(self.__precio_hora)*1.1
        return total
    
    def __lt__(self, otro):
        return self.costo()<otro.costo()
    
    def mostrar(self):
        contratante=super().dar_contratante()
        total=self.costo()
        print(f"{contratante}                     {total:.2f}")