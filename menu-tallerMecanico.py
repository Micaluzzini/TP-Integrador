#!/usr/bin/python3

from tallerMecanico import TallerMecanico
from vehiculo import Vehiculo
from auto import Auto
from camioneta import Camioneta
import sys


class Menu:
    def __init__(self):
        self.vehiculo = Vehiculo()

    def ejecutar(self):
        while True:
            self.elegir_opcion()

    def elegir_opcion(self):
        print ('''
1- Agregar un vehiculo, ya sea un auto o una camioneta.
2- Buscar un vehiculo por su patente.
3- Buscar un vehiculo por su dueño con nombre y/o apellido.
4- Mostrar un listado de todos los autos ingresados al taller.
5- Salir del programa.''')
        opcion = int(input("Elija la opción: "))

        if opcion == 1:
            self.agregar_()
        elif opcion == 2:
            self.buscar_por_patente()
        elif opcion == 3:
            self.buscar_por_nombre_apellido()
        elif opcion == 4:
            self.lista_completa()
        elif opcion == 6:
            self.salir()
            
    def agregar_vehiculo(self):
        while True:
            tipo = input("Ingrese tipo de vehiculo (Auto o Camioneta) [A/C]")
            if tipo in [ 'a', 'A', 'c', 'C']:
                break
            else:
                print("Error: ingrese 'a' o 'c'")
        patente = input("Ingrese la patente del vehiculo: ")
        modelo = input("Ingrese el modelo del vehiculo: ")
        marca = input("Ingrese la marca del vehiculo: ")
        nombre = int(input("Ingrese el nombre del propietartio del vehiculo: "))
        apellido = input("Ingrese el apellido de propietario del vehiculo: ")
        dni = input("Ingrese el DNI del propietario del vehiculo: ")
        
        if tipo == 'a' or tipo == 'A':
            cant_puertas = int(input("Ingrese la cantidad de puertas del auto: "))
            
        elif tipo == 'c' or tipo == 'C':
            tipo_traccion = int(input("Ingrese '2' si la tracción de la camioneta es 2x2 o '4' si es 4x4"))
              

        self.vehiculo.agregar_vehiculo(patente, modelo, marca, nombre, apellido, dni)
        
    def buscar_por_nombre_apellido(self):
        texto_a_buscar = input("Ingrese parte del nombre o apellido a buscar del dueño del vehiculo")
        dueños_vehiculo = self.vehiculo.buscar_por_nombre_apellido(texto_a_buscar)
        if dueños_vehiculo:
            # Mostramos los datos del vehiculo:
            for v in dueños_vehiculo:
                print(v.mostrar_datos())
        else:
            print("No se encontró ningún vehiculo relacionado a ese nombre y/o apellido")


    def salir(self):
        '''Muestra un mensaje y sale del sistema'''
        print("Gracias por utilizar el sistema.")
        sys.exit(0)


if __name__ == "__main__":
    Menu().ejecutar()
