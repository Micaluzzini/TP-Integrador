#!/usr/bin/python3

from auto import Auto
from camioneta import Camioneta
import datetime



class TallerMecanico:
    def __init__(self, lista_vehiculos = []):
        self.taller = lista_vehiculos
        
        
    def agregar_vehiculo(self, tipo, patente, modelo, marca, nombre, apellido, dni):
        if (tipo) == 'A' or 'a':
            v = Auto(tipo, patente, modelo, marca, nombre, apellido, dni)
        elif (tipo) == 'C' or 'C':
            v = Camioneta(tipo, patente, modelo, marca, nombre, apellido, dni)
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
        '''Un método que reciba un texto, y retorna una lista de personas cuyo
        nombre y/o apellido coincida (total o parcialmente) con ese texto.'''
        vehiculos_coincidentes = []
        for un_vehiculo in self.lista_vehiculos:
            if un_vehiculo.coincide(texto_a_buscar):
                vehiculos_coincidentes.append(un_vehiculo)
        return vehiculos_coincidentes
    
    def eliminar_vehiculo(self,patente):
        '''Busca la patente dada y elimina el vehiculo asociado a esa patente'''
        patente = self.buscar_por_patente(patente)
        if patente:
            self.vehiculos.remove(patente)
            return True
        return False
       
    
        
    def modificar_patente_vehiculo(self, patente):
        '''Busca la patente ingresada y la modifica por el nuevo texto ingresado'''
        nueva_patente = self.buscar_por_patente(patente)

        if nueva_patente:
            nueva_patente.patente = patente
            return True
        return False
