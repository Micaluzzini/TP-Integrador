#!/usr/bin/python3

from auto import Auto
from camioneta import Camioneta




class TallerMecanico:
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
    
    def eliminar_vehiculo(self,patente):
        '''Busca la patente dada y elimina el vehiculo asociado a esa patente'''
        patente = self.buscar_por_patente(patente)
        if patente:
            self.vehiculos.remove(patente)
            return True
        return False
       
    def mostrar_datos(self):
        texto = f"Patente y modelo: {self.patente} {self.modelo}\n"
        texto += f"Marca: {self.marca}\n"
        texto = f"Nombre y apellido: {self.nombre} {self.apellido}\n"
        texto += f"DNI: {self.dni}\n"
        
        return texto

    def coincide(self, patente_a_buscar):
        if patente_a_buscar in self.patente:
            return True
        else:
            return False
        
    def modificar_patente_vehiculo(self, patente):
        '''Busca la patente ingresada y la modifica por el nuevo texto ingresado'''
        nueva_patente = self.buscar_por_patente(patente)

        if nueva_patente:
            nueva_patente.patente = patente
            return True
        return False
