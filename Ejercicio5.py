class alumno:
    inasistmax=21
    cantclases=56
    __nombre=''
    __anio=''
    __division=''
    __cantinasist=''

    def __init__(self,nom,anio,divi,inas):
        self.__nombre=nom
        self.__anio=anio
        self.__division=divi
        self.__cantinasist=inas
