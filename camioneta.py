#!/usr/bin/python3

from vehiculo import Vehiculo

class Camioneta(Vehiculo):
      def __init__(self, patente, modelo, marca, nombre, apellido, dni, tipo_traccion):
        self.patente = patente
        self.modelo = modelo
        self.marca = marca
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
