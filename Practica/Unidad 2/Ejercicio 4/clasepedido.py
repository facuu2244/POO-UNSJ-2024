class pedido:
    __pate_Moto=""
    __id_pedido=""
    __comidas=""
    __tiempo_est=int
    __tiempo_real=0
    __precio=float
    
    def __init__(self, pate, id, comidas, tiempo_est, precio):
        self.__pate_Moto=pate
        self.__id_pedido=id
        self.__comidas=comidas
        self.__tiempo_est=tiempo_est
        self.__precio=precio
        
    def __str__(self):
        return f"{self.__pate_Moto},{self.__id_pedido},{self.__tiempo_real}"
    
    def dar_patente(self):
        return self.__pate_Moto
    
    def dar_id(self):
        return self.__id_pedido
    
    def cambiar_tiempreal(self, xtr):
        self.__tiempo_real=xtr
        
    def dar_tiempreal(self):
        return self.__tiempo_real
        
        
class gestor_pedidos:
    __gestor=list
    
    def __init__(self):
        self.__gestor=[]

    def cargar(self,un_pedido):
        self.__gestor.append(un_pedido)
    
    def actu_tiempr(self):
        pate=input("Patente de la moto: ")
        id=input("Id del pedido: ")
        xtr=int(input("Tiempo real de entrega(en minutos): "))
        
        #Buscar el pedido con el id ingresado
        band=False
        i=0
        while band==False and i<len(self.__gestor):
            if id==self.__gestor[i].dar_id():
                self.__gestor[i].cambiar_tiempreal(xtr)
                band=True
                print(self.__gestor[i])
            i+=1

        if band ==False:
            print("Pedido no encontrado")
    
    def calc_promedio(self, pate):
        acum=0
        i=0
        for pedido in self.__gestor:
            if pate==pedido.dar_patente():
                acum+=pedido.dar_tiempreal()
                i+=1
        return (acum/i)