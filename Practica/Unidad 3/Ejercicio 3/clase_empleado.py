class empleado:
    __nya:str
    __id:int
    __puesto:str
    __matriculas:list
    
    def __init__(self, nya, id, puesto):
        self.__nya=nya
        self.__id=int(id)
        self.__puesto=puesto
        self.__matriculas=[]
        
    def __str__(self):
        return self.__nya
    
    def dar_nya(self):
        return self.__nya
    def dar_id(self):
        return self.__id
    
    def matricular(self, matricula):
        self.__matriculas.append(matricula)
        
    def datos_prog(self):
        print(f"\n{self.__nya} esta matriculado a los siguientes programas:")
        for matri in self.__matriculas:
            matri.mostrar_prog()
    
    def verif_matriculacion(self):
        if self.__matriculas==[]:
            return self.__nya