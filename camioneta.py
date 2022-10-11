#!/usr/bin/python3


class Camioneta:
      def __init__(self, patente, modelo, marca, nombre, apellido, dni, tipo_traccion):
        self.patente = patente
        self.modelo = modelo
        self.marca = marca
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.tipo_traccion = tipo_traccion
        
        
      def mostrar_datos(self):
        texto = f"Patente y modelo: {self.patente} {self.modelo}\n"
        texto += f"Marca: {self.marca}\n"
        texto = f"Nombre y apellido: {self.nombre} {self.apellido}\n"
        texto += f"DNI: {self.dni}\n"
        texto += f"tipo_traccion: {self.tipo_traccion}\n"
        
        return texto  
      
      def coincide(self, patente_a_buscar):
        if patente_a_buscar in self.patente:
            return True
        else:
            return False
    
