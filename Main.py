
from lista import Lista
from Ejercicio5 import alumno
def op0():

    print("Salir")

def op1():
    a=int(input("Ingrese el año: "))
    d=str(input("Ingrese la division: ").upper())
    l.inasistencias(a,d)
    
def op2():
    a=int(input("Ingrese la nueva cantidad de inasistencias permitidas: "))
    alumno.cambio(a)

    

switcher={
    0:op0,
    1:op1,
    2:op2
    }
def switch(op):
    func = switcher.get(op, lambda: print("Opción incorrecta"))
    func()

if __name__ == '__main__':
    l=Lista()
    l.crearlista()
    al=alumno()
    bandera=False
    while not bandera:
        print("---Menu---\n")
        print("1.Muestra segun alumno\n")
        print("2.Modificar inasistencias maximas\n")
        op=int(input("SELECCIONE UNA OPCION. 0 para salir\n"))
        switch(op)
        bandera = int(op)==0



