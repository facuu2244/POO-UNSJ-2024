class matricula:
    __fecha:str
    __empleado:object
    __programa:object
    
    def __init__(self, fecha, emp, prog):
        self.__fecha=fecha
        self.__empleado=emp
        self.__programa=prog
        
    def dar_empl(self):
        return self.__empleado
    def dar_prog(self):
        return self.__programa
    
    def mostrar_prog(self):
        print(self.__programa)
    def mostrar_empl(self):
        print(self.__empleado)