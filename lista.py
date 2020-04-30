from Ejercicio5 import alumno
import csv
class Lista:
    __Lista=[]
    def __init__(self):
        self.__Lista=[]
    def crearlista(self):
        archivo=open("alumnos.csv")
        reader=csv.reader(archivo,delimiter=',')
        for fila in reader:
            alu=alumno(fila[0],fila[1],fila[2],fila[3])
            self.__Lista.append(alu)
        return self.__Lista

    def inasistencias(self,a,d):
        print("Alumno:         Porcentaje:\n")
        for fila in range(len(self.__Lista)):
            l=int(self.__Lista[fila].retornaanio())
            h=int(self.__Lista[fila].retornacant())
            k=alumno.inasistmax
            m=str(self.__Lista[fila].retornadivi())
            
            if a==l and d==m and k<h: 
                porcentaje=0.0
                porcentaje=float(int(h*100)/int(self.__Lista[fila].retornacantclases()))
                print("{}{:.2f}%".format(self.__Lista[fila].retornanom().ljust(20," "),porcentaje))
    

            