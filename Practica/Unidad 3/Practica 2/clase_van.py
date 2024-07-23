from clase_vehiculo import vehiculo

class van(vehiculo):
    __tipo_carroseria:str
    
    def __init__(self, marca, modelo, anio, capacidad, num, distancia, tarifa, carroseria):
        super().__init__(marca, modelo, anio, capacidad, num, distancia, tarifa)
        self.__tipo_carroseria=carroseria
        
    def calcular_tarifa(self):
        tarifa:float
        if self.__tipo_carroseria=="minivan":
            descuento=super().dar_tarifa()*0.1
            tarifa=super().dar_tarifa()-descuento
        else:
            tarifa=super().dar_tarifa()*1.025
        
        return tarifa
    
    def mostrar_datos(self, tarifa):
        modelo=super().dar_modelo()
        anio=super().dar_anio()
        capacidad=super().dar_capacidad()
        
        print(f"Modelo: {modelo}, año:{anio}, capacidad:{capacidad}, tarifa:{tarifa:.2f}")