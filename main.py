from TDA_Cola.cola import Cola
import os, sys, time

cola = Cola()

def cls():
    os.system("cls")

def menu():
    cls()
    while True:
        print("""****** Menu Principal ******
        
        1. Ingresar Orden
        2. Entregar Orden
        3. Mostrar Orden
        4. Mostrar Datos del Estudiante
        5. Salir""")

        opc = input("Ingrese opción a realizar:")

        if opc == "1":
            cls()
            print("*** Bienvenido a Pizza Family ***")
            x = input("Ingrese el ingrediente de su piza: ")
            cola.push(x)
            input("Pizza agregada a la orden...")
            menu()
            break
        if opc == "2":
            cls()
            print("*** Entregar Orden ***\n")
            cola.firstOrder()
            confirm = input("Confirmar orden Si/No: ")

            if confirm.lower().strip() == "si":
                cola.pop()
                menu()
            else:
                menu()
            break
        if opc == "3":
            cls()
            print("*** Ordenes de Pizza agregados al sistema ***\n")
            cola.show()
            input("Presione cualquier tecla para continuar...")
            menu()
            break
        if opc == "4":
            cls()      
            print("\n           Datos del estudiante            \n")     
            print("**********************************************")
            print("****                IPC 2                 ****")
            print("****              Sección D               ****")
            print("****                                      ****")
            print("****            Ciencias y sistemas       ****")
            print("****      Brayan Andrés Cholotio Tum      ****")
            print("****              201807066               ****")
            print("**********************************************\n")

            input("Presione cualquier tecla para continuar...")
            menu()
            break
        if opc == "5":
            cls()
            print("Saliendo del sistema...")
            time.sleep(0.5)
            os.system("exit")
            break
        else:
            print("\nOpcion inorrecta...")
            time.sleep(0.5)
            cls()
            menu()
            break

menu()