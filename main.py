from claseArreglo import Arreglo
from claseEmpleado import Empleado
from os import system
from datetime import datetime

def switch(argument):
    func = switcher.get(argument, lambda: print("Opción incorrecta"))
    func()

def opcion1():
    system('cls')
    dni= int(input("Ingrese el dni de un empleado: "))
    horasTrabajadas= int(input("Ingrese la cantidad de horas trabajadas: "))
    i = 0
    arregloEmpleados.setHorasTrabajadas(dni, horasTrabajadas)
    system('pause')
    system('cls')

def opcion2():
    system('cls')
    tarea= str(input("Ingrese una tarea: "))
    while tarea != "Carpinteria" and tarea != "Electricidad" and tarea != "Plomeria": 
        print("ERROR: Tarea inexistente.")
        tarea= str(input("Ingrese una tarea: "))
    print(f"El monto a pagar por la tarea '{tarea}' es de: {arregloEmpleados.montoPorTarea(tarea)}")
    system('pause')
    system('cls')

def opcion3():
    system('cls')
    arregloEmpleados.listar()
    system('pause')
    system('cls')

def opcion4():
    system('cls')
    arregloEmpleados.mostrar()
    system('pause')
    system('cls')

def opcion0():

    exit()

switcher = {
    0: opcion0,
    1: opcion1,
    2: opcion2,
    3: opcion3,
    4: opcion4
}

if __name__ == "__main__":
    system("cls")
    #Ingresa el tamaño del arreglo y creamos el mismo
    print("Antes de comenzar, debe ingresar una cantidad de empleado a cargar: 15")
    print("(Se ingresa automaticamente el numero 15 para testear)")
    cantidad = 15
    #cantidad = int(input("Antes de comenzar, debe de ingresar una cantidad de empleados a cargar:"))
    arregloEmpleados = Arreglo(cantidad)
    system("pause")
    system("cls")
    bandera = False
    while not bandera:
        print("0. Salir")
        print("1. Registrar horas")
        print("2. Total de tarea")
        print("3. Ayuda")
        print("4. Calcular sueldo")
        opcion= int(input("Ingrese una opción: "))
        switch(opcion)
        bandera = int(opcion)==0