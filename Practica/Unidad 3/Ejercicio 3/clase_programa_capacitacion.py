class programa:
    __nom:str
    __cod:str
    __duracion:int
    __matriculas:list
    
    def __init__(self, nom, cod, duracion):
        self.__nom=nom
        self.__cod=cod
        self.__duracion=duracion
        self.__matriculas=[]
        
    def __str__(self):
        return f"{self.__nom}, duracion: {self.__duracion}hs"
        
    def dar_nom(self):
        return self.__nom
    
    def matricular(self, matricula):
        self.__matriculas.append(matricula)
        
    def empleados(self):
        print(f"\nEmpleado/s matriculados al programa {self.__nom}: ")
        for matri in self.__matriculas:
            matri.mostrar_empl()