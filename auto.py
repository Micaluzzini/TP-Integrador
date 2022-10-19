#!/usr/bin/python3
import datetime

class Auto:
      def __init__(self, tipo, patente, modelo, marca, nombre, apellido, dni, cant_puertas_traccion):
        self.tipo = tipo
        self.patente = patente
        self.modelo = modelo
        self.marca = marca
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.cant_puertas_traccion = cant_puertas_traccion
        self.fecha_creacion = datetime.date.today()
        
      def mostrar_datos(self):
        texto = f"Tipo: {self.tipo}\n"
        texto += f"Patente y modelo: {self.patente} {self.modelo}\n"
        texto += f"Marca: {self.marca}\n"
        texto += f"Nombre y apellido: {self.nombre} {self.apellido}\n"
        texto += f"DNI: {self.dni}\n"
        texto += f"Cantidad de puertas: {self.cant_puertas_traccion}\n"
        
        return texto
      
      def coincide(self, texto_a_buscar):
        if texto_a_buscar.upper() in self.nombre.upper() or texto_a_buscar.upper() in self.apellido.upper():
            return True
        else:
            return False