from clase_libro import publicacion

class cd(publicacion):
    __tiempo_rep:int
    __nom_narra:str
        
    def __init__(self, titulo, cate, precio,tiempo, nom):
        super().__init__(titulo, cate, precio)
        self.__tiempo_rep=tiempo
        self.__nom_narra=nom
    
    def mostrar_publi(self):
        imp_venta=super().dar_precio_base()*1.1
        print(f"{super().dar_titulo()}, {super().dar_categoria()}, {imp_venta:.2f}")