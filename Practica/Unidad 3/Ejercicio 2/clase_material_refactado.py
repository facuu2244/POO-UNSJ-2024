class material_refac:
    __material:int
    __caract:str
    __cant_utilizada:float
    __cost_adic:float
    
    def __init__(self, mat, caract, cant, costo):
        self.__material=int(mat)
        self.__caract=caract
        self.__cant_utilizada=cant
        self.__cost_adic=float(costo)
        
        
    def dar_mat(self):
        return self.__material
    def dar_cost(self):
        return self.__cost_adic
    def dar_caract(self):
        return self.__caract