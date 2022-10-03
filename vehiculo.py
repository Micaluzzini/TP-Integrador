#!/usr/bin/python3

from auto import Auto
from camioneta import Camioneta

class Vehiculo:
    def __init__(self, tipo, patente, modelo, marca, nombre, apellido, dni):
        self.tipo = tipo
        self.patente = patente
        self.modelo = modelo
        self.marca = marca
        elf.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        
     def mostrar_datos(self):
        texto += f"tipo: {self.tipo}\n"
        texto = f"Patente y modelo: {self.patente} {self.modelo}\n"
        texto += f"Marca: {self.marca}\n"
        texto = f"Nombre y apellido: {self.nombre} {self.apellido}\n"
        texto += f"DNI: {self.dni}\n"
        
        return texto

    def coincide(self, texto_a_buscar):
        if texto_a_buscar in self.patente:
            return True
        else:
            return False


        
        
        
        
  

    
    
    
