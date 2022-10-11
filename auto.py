#!/usr/bin/python3


class Auto:
      def __init__(self, patente, modelo, marca, nombre, apellido, dni, cant_puertas):
        self.patente = patente
        self.modelo = modelo
        self.marca = marca
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.cant_puertas = cant_puertas
        
      def mostrar_datos(self):
        texto = f"Patente y modelo: {self.patente} {self.modelo}\n"
        texto += f"Marca: {self.marca}\n"
        texto = f"Nombre y apellido: {self.nombre} {self.apellido}\n"
        texto += f"DNI: {self.dni}\n"
        texto += f"Cantidad de puertas: {self.cant_puertas}\n"
        
        return texto
        
    
    
