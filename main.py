import os, sys

def cls():
    os.system("cls")

def menu():
    cls()
    while True:
        print("""****** Menu Principal ******
        
        1. Ingresar Orden
        2. Entregar Orden
        3. Mostrar Orden
        4. Mostrar Datos deel Estudiante
        5. Salir""")

        opc = input("Ingrese opción a realizar:")
        input()
        break

menu()