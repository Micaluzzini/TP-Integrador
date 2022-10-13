#!/usr/bin/python3
from tallerMecanico import TallerMecanico
from repositorioTallerMecanico import RepositorioTallerMecanico
import tkinter
from tkinter import ttk
from tkinter import messagebox

class Gui():
    '''Crear la pantalla inicial, mostrando todas las notas y botones'''
    def __init__(self):
        self.iniciar_tallerMecanico()
        self.iniciar_gui()

    def iniciar_tallerMecanico(self):
        self.repositorio = RepositorioTallerMecanico()
        taller = self.repositorio.obtener_todo()
        self.tallerMecanico = TallerMecanico(taller)

    def iniciar_gui(self):
        self.ventana_principal = tkinter.Tk()
        self.ventana_principal.title("Taller Mecanico")
        botonAgregarVehiculo=tkinter.Button(self.ventana_principal,text="Agregar vehiculo", 
                           command = self.agregar).grid(row=0, column=0)
        botonBuscarPorPatente=tkinter.Button(self.ventana_principal,text="Buscar por patente",
                           command = self.buscar_por_patente).grid(row=0, column=1)
      
    
    def salir(self):
        self.repositorio.guardar_todo(self.tallerMecanico.taller)
        self.ventana_principal.destroy()

if __name__ == "__main__":
    gui = Gui()
    gui.ventana_principal.mainloop()
