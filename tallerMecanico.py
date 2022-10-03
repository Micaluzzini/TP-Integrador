#!/usr/bin/python3

from auto import Auto
from camioneta import Camioneta


class Vehiculo:
    def __init__(self):
        self.lista_vehiculos = []
        
        
    def agregar_vehiculo(self, tipo, patente, modelo, marca, nombre, apellido, dni):
        if (tipo) == 'A' or 'a':
            v = Auto(patente, modelo, marca, nombre, apellido, dni)
        elif (tipo) == 'C' or 'C':
            v = Camioneta(patente, modelo, marca, nombre, apellido, dni)
        else:
            return None

        self.lista_vehiculos.append(v)

    def buscar_por_patente(self, patente_para_buscar):
        '''Un método que reciba una patente y retorne el vehiculo que tiene
        esa patente, o None si no hay ninguno.'''
        for un_vehiculo in self.lista_vehiculos:
            if un_vehiculo.dni == patente_para_buscar:
                return un_vehiculo
        return None

    def buscar_por_nombre_apellido(self, texto_a_buscar):
        '''Un método que reciba un texto, y retorne una lista de empleados cuyo
        nombre y/o apellido coincida (total o parcialmente) con ese texto.'''
        vehiculos_coincidentes = []
        for un_vehiculo in self.lista_vehiculos:
            if un_vehiculo.coincide(texto_a_buscar):
                vehiculos_coincidentes.append(un_vehiculo)
        return vehiculos_coincidentes