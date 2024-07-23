from clase_vehiculo import vehiculo

class autobus(vehiculo):
    __tipo_servicio:str
    __turno:str
    
    def __init__(self, marca, modelo, anio, capacidad, num, distancia, tarifa, tipo, turno):
        super().__init__(marca, modelo, anio, capacidad, num, distancia, tarifa)
        self.__tipo_servicio=tipo
        self.__turno=turno
        
    def calcular_tarifa(self):
        tarifa:float
        if self.__tipo_servicio=="turismo" and self.__turno=="noche":
            tarifa=super().dar_tarifa()*1.2
        else:
            tarifa=super().dar_tarifa()*1.05
        
        return tarifa
    
    def mostrar_datos(self, tarifa):
        modelo=super().dar_modelo()
        anio=super().dar_anio()
        capacidad=super().dar_capacidad()
        
        print(f"Modelo: {modelo}, año:{anio}, capacidad:{capacidad}, tarifa:{tarifa:.2f}")