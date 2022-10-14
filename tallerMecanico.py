#!/usr/bin/python3

from auto import Auto
from camioneta import Camioneta
import datetime

class TallerMecanico:
    '''Representa una colección de vehículos que se pueden editar, eliminar, buscar'''
    
    def __init__(self, lista_vehiculos = []):
        '''Inicializa el Taller Mecanico con una lista de vehículos'''
        self.lista_vehiculos = lista_vehiculos
        
# AGREGAR VEHICULO    
        '''Agrega un vehiculo que puede ser Auto o Camioneta. Se agrega a la coleccion
    de lista de vehiculos'''
    def agregar_vehiculo(self, tipo, patente, modelo, marca, nombre, apellido, dni, cant_puertas_tipo_traccion):
        if (tipo) == 'A' or 'a':
            v = Auto(tipo, patente, modelo, marca, nombre, apellido, dni, cant_puertas_tipo_traccion)
        elif (tipo) == 'C' or 'c':
            v = Camioneta(tipo, patente, modelo, marca, nombre, apellido, dni, cant_puertas_tipo_traccion)
        else:
            return None

        self.lista_vehiculos.append(v)

        '''Se le agrega este return para que el gui lo lea'''
        return v

# BUSCAR POR PATENTE
    def buscar_por_patente(self, patente_para_buscar):
        '''Un método que reciba una patente y retorne el vehiculo que tiene
        esa patente, o None si no hay ninguno.'''
        for un_vehiculo in self.lista_vehiculos:
            if un_vehiculo.patente == patente_para_buscar:
                return un_vehiculo
            
        return None

# BUSCAR POR NOMBRE Y APELLIDO
    def buscar_por_nombre_apellido(self, texto_a_buscar):
        '''Un método que reciba un texto, y retorna una lista de personas cuyo
        nombre y/o apellido coincida (total o parcialmente) con ese texto.'''
        vehiculos_coincidentes = []
        for un_vehiculo in self.lista_vehiculos:
            if un_vehiculo.coincide(texto_a_buscar):
                vehiculos_coincidentes.append(un_vehiculo)
        return vehiculos_coincidentes

# ELIMINAR VEHICULO POR PATENTE  
    def eliminar_vehiculo(self, patente):
        '''Busca la patente dada y elimina el vehiculo asociado a esa patente'''
        vehiculo = self.buscar_por_patente(patente)
        if vehiculo:
            self.lista_vehiculos.remove(vehiculo)
            print("\nEl vehiculo se elimino correctamente")
            return True
        else:
            print("\nNo se encontro vehiculo con esa patente")
            return False
       
# MODIFICAR PATENTE        
    def modificar_patente_vehiculo(self, patente, texto_patente):
        '''Busca la patente ingresada y la modifica por el nuevo texto ingresado'''
        nueva_patente = self.buscar_por_patente(patente)

        if nueva_patente:
            nueva_patente.patente = texto_patente
            print("\nLa patente se modifico correctamente")
            return True
        else:
            print("\nNo se encontro vehiculo con esa patente")
            return False

# MOSTRAR TODOS LOS VEHICULOS
    def mostrar_vehiculos(self):
        for un_vehiculo in self.lista_vehiculos:
            print(un_vehiculo.mostrar_datos())

# CONTAR POR TIPO: SERA UN REPORTE
    def contar_veh(self, tipo):
        lista_vehiculos_tipo = []
        if tipo == 'A':
            lista_vehiculos_tipo = [v for v in self.lista_vehiculos if v.tipo == 'A']
            
        elif tipo == 'C':
            lista_vehiculos_tipo = [v for v in self.lista_vehiculos if v.tipo == 'C']

        return len(lista_vehiculos_tipo)

# Modificar todo el vehiculo para el GUI       
    def modificar_todo_gui(self, patente, tipo, modelo, marca, nombre, apellido, dni, cant_puertas_traccion):
        '''Busca la patente ingresada y la modifica por el nuevo texto ingresado'''
        nueva_patente = self.buscar_por_patente(patente)

        if nueva_patente:
            nueva_patente.tipo = tipo
            # nueva_patente.patente = patente_nueva
            nueva_patente.modelo = modelo
            nueva_patente.marca = marca
            nueva_patente.nombre = nombre
            nueva_patente.apellido = apellido
            nueva_patente.dni = dni
            nueva_patente.cant_puertas_traccion = cant_puertas_traccion
            print("\nEl vehiculo se modifico correctamente")
            return True
        else:
            print("\nNo se encontro vehiculo con esa patente")
            return False