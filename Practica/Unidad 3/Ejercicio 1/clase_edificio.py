from clase_departamento import departamento

class edificio: 
    __id:int
    __nombre:str
    __direccion:str
    __empr_constructora:str
    __cant_pisos:int
    __cant_dept:int
    __departamentos:list
    
    def __init__(self, id,nom,direc,empr,pisos,deptos):
        self.__id=id
        self.__nombre=nom
        self.__direccion=direc
        self.__empr_constructora=empr
        self.__cant_pisos=pisos
        self.__cant_dept=deptos
        self.__departamentos=[]
        
        
    def __del__(self):
        print("Eliminando edificio....")
        for dep in self.__departamentos:
            del dep
            
    def agregar_depto(self, id,nya,piso,dept,habi,banos,sup):
        un_departamento=departamento(id,nya,piso,dept,habi,banos,sup)
        self.__departamentos.append(un_departamento)
        
    def dar_nombre(self):
        return self.__nombre
    
    def mostrar_deptos(self):
        for depto in self.__departamentos:
            depto.mostrar_propi()
            
    def calc_sup(self):
        acum=0
        for depto in self.__departamentos:
            acum+=depto.dar_sup()
        
        return acum
    
    def buscar_propi(self, propi):
        band=False
        i=0
        sup=None
        while band==False and i<len(self.__departamentos):
            if propi==self.__departamentos[i].dar_propi():
                band=True
                sup=self.__departamentos[i].dar_sup()
                print(f"La superficie cubierta del departamento de {propi}, es: {sup}")
            i+=1
        return sup
    
    def filtar_deptos(self,piso):
        cont_depto=0
        for depto in self.__departamentos:
            if depto.dar_piso()==piso and depto.dar_habi()==3 and depto.dar_banos()>1:
                cont_depto+=1
                print(depto)
        
        return cont_depto