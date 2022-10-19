#!/usr/bin/python3

from tallerMecanico import TallerMecanico
import sys
from camioneta import Camioneta
from auto import Auto


#Es el menu que se ejecuta en consola sin necesidad de gui con tkinter
class Menu:
    def __init__(self):
        self.tallerMecanico = TallerMecanico()
    def ejecutar_menu(self):
        while True:
            self.elegir_opcion()

    def elegir_opcion(self):
        print ('''
1- Agregar un vehiculo, ya sea un auto o una camioneta.
2- Buscar un vehiculo por su patente.
3- Buscar un vehiculo por su dueño con nombre y/o apellido.
4- Mostrar un listado de todos los autos ingresados al taller.
5- Modificar la patente de algún vehículo.
6- Eliminar algún vehículo.
7- Mostrar cantidad de autos o camionetas.
8- Salir del programa.''')
        opcion = int(input("\nElija la opción: "))

        if opcion == 1:
            self.agregar()
        elif opcion == 2:
            self.buscar_por_patente()
        elif opcion == 3:
            self.buscar_por_nombre_apellido()
        elif opcion == 4:
            self.lista_completa()
        elif opcion == 5:
            self.modificar_patente_vehiculo()
        elif opcion == 6:
            self.eliminar_vehiculo()
        elif opcion == 7:
            self.contar_vehiculos()
        elif opcion == 8:
            self.salir()

# AGREGAR VEHICULO          
    def agregar(self):
        while True:
            tipo = input("\nIngrese tipo de vehiculo (Auto o Camioneta) [A/C]: ")
            if tipo in [ 'a', 'A', 'c', 'C']:
                tipo = tipo.upper()
                break
            else:
                print("Error: ingrese 'A' o 'C'")

        patente = input("Ingrese la patente del vehiculo: ")
        modelo = input("Ingrese el modelo del vehiculo: ")
        marca = input("Ingrese la marca del vehiculo: ")
        nombre = input("Ingrese el nombre del propietartio del vehiculo: ")
        apellido = input("Ingrese el apellido de propietario del vehiculo: ")
        dni = input("Ingrese el DNI del propietario del vehiculo: ")

        if tipo == 'A':
            cant_puertas_tipo_traccion = int(input("Ingrese la cantidad de puertas del auto: "))
            
        elif tipo == 'C':
            cant_puertas_tipo_traccion = int(input("Ingrese '2' si la tracción de la camioneta es 2x2 o '4' si es 4x4: "))
              
        # Esta asignacion es porque agregar_vehiculo retorna un objeto, pero aca no sirve para nada
        v = self.tallerMecanico.agregar_vehiculo(tipo, patente, modelo, marca, nombre, apellido, dni, cant_puertas_tipo_traccion)

# BUSCA POR PATENTE         
    def buscar_por_patente(self):
        patente_a_buscar = input("\nIngrese la patente a buscar: ")
        patente = self.tallerMecanico.buscar_por_patente(patente_a_buscar)
        if patente:
            # Mostramos los datos del vehiculo con esa patente:
            print("\n")
            print(patente.mostrar_datos())
        else:
            print("\nNo se encontró un vehiculo con esa patente")    
        

# NOMBRE O APELLIDO   
    def buscar_por_nombre_apellido(self):
        texto_a_buscar = input("\nIngrese parte del nombre o apellido a buscar del dueño del vehiculo: ")
        dueños_vehiculo = self.tallerMecanico.buscar_por_nombre_apellido(texto_a_buscar)
        if dueños_vehiculo:
            # Mostramos los datos del vehiculo:
            for v in dueños_vehiculo:
                print("\n")
                print(v.mostrar_datos())
        else:
            print("\nNo se encontró ningún vehiculo relacionado a ese nombre y/o apellido")

# LISTA COMPLETA
    def lista_completa(self):
        print("\nLista de todos los vehiculos ingresados: ")
        self.tallerMecanico.mostrar_vehiculos()
            
# MODIFICAR PATENTE            
    def modificar_patente_vehiculo(self):
        '''Solicita la patente del vehiculo y la nueva patente a modificar. Busca la patente con el ID de patente ingresado, y actualiza con la nueva patente.'''
        patente = input("\nIngrese la patente del vehiculo a modificar: ")
        texto_patente = input("\nIngrese la nueva patente correctamente: ")
        
        if texto_patente:
            self.tallerMecanico.modificar_patente_vehiculo(patente, texto_patente)

# ELIMINAR POR PATENTE           
    def eliminar_vehiculo(self):
        '''Solicita la patente del vehiculo y luego lo elimina'''
        patente = input("\nIngrese la patente del vehiculo a eliminar: ")

        if patente:
            self.tallerMecanico.eliminar_vehiculo(patente)

# CONTAR POR TIPO         
    def contar_vehiculos(self):
        '''Solicita tipo de vehiculo a contar'''
        while True:
            tipo = input("\nIngrese tipo de vehiculo (Auto o Camioneta) [A/C]: ")
            if tipo in [ 'a', 'A', 'c', 'C']:
                tipo = tipo.upper()
                cant = self.tallerMecanico.contar_veh(tipo)
                if cant == 0:
                    print("\nNo se encontraron vehiculos de ese tipo")
                else:
                    print(f"Cantidad de vehiculos de ese tipo: {cant}\n")
                break
            else:
                print("Error: ingrese 'A' o 'C'")
                
            
# EXIT
    def salir(self):
        '''Muestra un mensaje y sale del sistema'''
        print("Gracias por utilizar el sistema.")
        sys.exit(0)


if __name__ == "__main__":
    Menu().ejecutar_menu()
