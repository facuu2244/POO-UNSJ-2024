from clase_publicacion import publicacion

class libro(publicacion):
    __nombre_autor:str
    __fecha_edicion:int
    __cantpaginas:int
    
    def __init__(self, titulo, cate, precio,nom, fecha, cant):
        super().__init__(titulo, cate, precio)
        self.__nombre_autor=nom
        self.__fecha_edicion=int(fecha)
        self.__cantpaginas=cant
    
    def dar_fecha(self):
        return self.__fecha_edicion
    
    def mostrar_publi(self):
        porc_descuento=super().dar_fecha()-self.__fecha_edicion
        imp_venta=(porc_descuento*super().dar_precio_base())/100
        print(f"{super().dar_titulo()}, {super().dar_categoria()}, {imp_venta:.2f}")