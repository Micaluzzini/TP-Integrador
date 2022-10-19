#! /usr/bin/python3

from tallerMecanico import TallerMecanico
from camioneta import Camioneta
from auto import Auto
import datetime

class RepositorioTallerMecanico:
    def __init__(self, archivo = "taller.txt"):
        self.archivo = archivo

    def obtener_todo(self):
        taller = []
        with open(self.archivo, 'r') as fp:
            for tallerMecanico_como_texto in fp:
                t = self.texto_a_taller(tallerMecanico_como_texto)
                taller.append(t)
        return taller

    def guardar_todo(self, taller):
        with open(self.archivo, 'w') as fp:
            for tall in taller:
                taller_como_texto = self.taller_a_texto(tall)
                fp.write(taller_como_texto)
            print("Guardado en "+ self.archivo)

    def taller_a_texto(self, taller):
        fc = taller.fecha_creacion
        fecha_en_texto = str(fc.year) + '-' + str(fc.month) + '-' + str(fc.day)
        return taller.tipo + ',' + taller.patente + ',' + taller.modelo + ',' + taller.marca + ',' + taller.nombre + ',' + taller.apellido + ',' + taller.dni + ',' + taller.cant_puertas_traccion + ',' + fecha_en_texto + "\n"

    def texto_a_taller(self, texto):
        texto = texto[:-1]  # Sacamos el \n final
        tallerMecanico_como_lista = texto.split(',')
        if tallerMecanico_como_lista[0] == 'A':
            t = Auto(tallerMecanico_como_lista[0], tallerMecanico_como_lista[1],tallerMecanico_como_lista[2], tallerMecanico_como_lista[3],tallerMecanico_como_lista[4], tallerMecanico_como_lista[5],tallerMecanico_como_lista[6], tallerMecanico_como_lista[7])
        elif tallerMecanico_como_lista[0] == 'C':
            t = Camioneta(tallerMecanico_como_lista[0], tallerMecanico_como_lista[1],tallerMecanico_como_lista[2], tallerMecanico_como_lista[3],tallerMecanico_como_lista[4], tallerMecanico_como_lista[5],tallerMecanico_como_lista[6], tallerMecanico_como_lista[7])
        fecha = tallerMecanico_como_lista[8].split('-')
        t.fecha_creacion = datetime.date(int(fecha[0]),int(fecha[1]),int(fecha[2]))
        return t