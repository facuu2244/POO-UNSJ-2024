from clase_material_refactado import material_refac

class ladrillo:
    __alto=7
    __largo=25
    __ancho=15
    __cantidad:int
    __id:int
    __kg_material_uti:float
    __costo:float
    __materiales:list
    
    def __init__(self, cant, id, kg, costo):
        self.__cantidad=int(cant)
        self.__id=int(id)
        self.__kg_material_uti=float(kg)
        self.__costo=float(costo)
        self.__materiales=[]
        
    def agregar_mat(self, material):
        if material not in self.__materiales:
            self.__materiales.append(material)
            self.__costo+=material.dar_cost()
        else:
            print("El ladrillo ya posee ese material ")
            
    def dar_id(self):
        return self.__id
    
    def dar_caract(self):
        print(f"\nCaracteristicas del ladrillo {self.__id}:\nCosto: {self.__costo}")
        print("Caracteristicas de materiales: ")
        if self.__materiales==[]:
                print("Es un ladrillo comun, sin materiales refractados")
        else: 
            for mate in self.__materiales:
                print(mate.dar_caract())
                
    def costo_total(self):
        total= self.__cantidad*self.__costo
        print(f"Costo total del pedido del ladrillo {self.__id}: ${total}")
        
    def datos_tabla(self):
        if self.__materiales==[]:
            materiales="Comun"
            print(f"        {self.__id}                           {materiales}                      {self.__costo}")
        else: 
            for mat in self.__materiales:
                materiales=[]
                materiales.append(mat.dar_mat())#Guarda los materiales del ladrillo en una lista ya que puede que tenga mas de uno
            print(f"        {self.__id}                         Comun + {materiales}                  {self.__costo}")
