class alumno:
    inasistmax=21
    cantclases=56
    __nombre=''
    __anio=''
    __division=''
    __cantinasist=''

    def __init__(self,nom='',anio='',divi='',inas=''):
        self.__nombre=nom
        self.__anio=anio
        self.__division=divi
        self.__cantinasist=inas

    def retornaanio(self):
        return self.__anio

    def retornacant(self):
        return self.__cantinasist
    

    def retornanom(self):
        return self.__nombre

    def retornacantclases(self):
        return self.cantclases

    def retornadivi(self):
        return self.__division
    @classmethod
    def cambio(cls,nueva):
        cls.inasistmax=nueva