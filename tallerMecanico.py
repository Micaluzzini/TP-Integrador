#!/usr/bin/python3

class TallerMecanico:
    
    def coincide(self, texto_a_buscar):
        if texto_a_buscar in self.patente or texto_a_buscar in self.dni:
            return True
        else:
            return False
    


    def mostrar_datos(self):
        texto += f"Patente: {self.patente}\n"
        texto += f"Modelo: {self.modelo}\n"
        texto += f"Marca: {self.marca}\n"
        texto = f"Nombre y apellido: {self.nombre} {self.apellido}\n"
        texto += f"DNI: {self.dni}\n"
        return texto
    
    
    