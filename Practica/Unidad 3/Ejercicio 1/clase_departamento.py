class departamento: 
    __id:int
    __nya_propi:str
    __num_piso:int
    __num_dept:int
    __cant_habi:int
    __cant_banos:int
    __sup:float
    
    def __init__(self, id,nya,piso,dept,habi,banos,sup):
        self.__id=id
        self.__nya_propi=nya
        self.__num_piso=piso
        self.__num_dept=dept
        self.__cant_habi=habi
        self.__cant_banos=banos
        self.__sup=sup
        
    def __del__(self):
        print("Eliminando departamento....")
        
    def __str__(self) -> str:
        return f"Numero de departamento: {self.__num_dept}  Propietario: {self.__nya_propi}  Superficie: {self.__sup}"
    
    def mostrar_propi(self):
        print(f"Departamento: {self.__id}    Propietario: {self.__nya_propi}")
        
    def dar_sup(self):
        return float(self.__sup)
    def dar_propi(self):
        return self.__nya_propi
    def dar_piso(self):
        return int(self.__num_piso)
    def dar_habi(self):
        return int(self.__cant_habi)
    def dar_banos(self):
        return int(self.__cant_banos)
