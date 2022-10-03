#!/usr/bin/python3

from vehiculo import Vehiculo

class Auto(Vehiculo):
      def __init__(self, patente, modelo, marca, nombre, apellido, dni, cant_puertas):
        self.patente = patente
        self.modelo = modelo
        self.marca = marca
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.cant_puertas = cant_puertas
        
    
    
