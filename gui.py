#!/usr/bin/python3
from tallerMecanico import TallerMecanico
from repositorioTallerMecanico import RepositorioTallerMecanico
import tkinter
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk


class Gui():
    '''Crear la pantalla inicial, mostrando todos los vehiculos y botones'''
    def __init__(self):
        self.iniciar_tallerMecanico()
        self.iniciar_gui()

    def iniciar_tallerMecanico(self):
        self.repositorio = RepositorioTallerMecanico()
        taller = self.repositorio.obtener_todo()
        self.tallerMecanico = TallerMecanico(taller)

    def iniciar_gui(self):
        self.ventana_principal = tkinter.Tk()
        self.ventana_principal.title("Taller Mecanico 'Clinica del Automotor'")

        # Interfaz
        botonAgregarVehiculo = tkinter.Button(self.ventana_principal,text="Agregar vehiculo", bg="green",
                           command = self.agregar_vehiculo).grid(row=0, column=0)
        botonModificarVehiculoPatente=tkinter.Button(self.ventana_principal,text="Modificar Vehiculo", cursor="pencil",
                           command = self.modificar_vehiculo).grid(row=0, column=1)
        botonEliminarVehiculo=tkinter.Button(self.ventana_principal, text = "Eliminar Vehiculo", bg="#ff0000",
                           command = self.eliminar_vehiculo).grid(row=1, column=0)
        botonContarVehiculosIngresados = tkinter.Button(self.ventana_principal,text="Contar vehiculos ingresados",
                           command = self.contar_vehiculo).grid(row=1, column=1)
    

        tkinter.Label(self.ventana_principal,text="Buscar vehiculo por nombre y apellido").grid(row=2,column=0)
        tkinter.Label(self.ventana_principal,text="Buscar vehiculo por patente").grid(row=3,column=0)

        # Aca se esribe el texto para buscar por nombre y apellido
        self.cajaBuscar = tkinter.Entry(self.ventana_principal)
        self.cajaBuscar.grid(row=2, column=1)
        botonBuscar = tkinter.Button(self.ventana_principal, text = "Buscar",
                           command = self.buscar_vehiculo).grid(row=2, column=3)

        # Aca se esribe el texto para buscar por patente
        self.cajaBuscarPatente = tkinter.Entry(self.ventana_principal)
        self.cajaBuscarPatente.grid(row=3, column=1)
        botonBuscar = tkinter.Button(self.ventana_principal, text = "Buscar",
                           command = self.buscar_patente).grid(row=3, column=3)

        # Hay un TreeView que va mostrar las siguientes columnas               
        self.treeview = ttk.Treeview(self.ventana_principal)
        self.treeview = ttk.Treeview(self.ventana_principal, 
                                     columns=("tipo", "marca", "modelo","nombre", "apellido","dni", "cant_puertas_traccion"))
        self.treeview.heading("#0", text="Patente")
        self.treeview.column("#0", minwidth=0, width="50")
        self.treeview.heading("tipo", text="Tipo")
        self.treeview.heading("marca", text="Marca")
        self.treeview.heading("modelo", text="Modelo")
        self.treeview.heading("nombre", text="Nombre")
        self.treeview.heading("apellido", text="Apellido")
        self.treeview.heading("dni", text="DNI")
        self.treeview.heading("cant_puertas_traccion", text="Cant_Puertas_Traccion")
        self.treeview.grid(row=10, columnspan=6)

        # Aca pone los vehiculos en pantalla
        self.poblar_tabla()

        botonSalir = tkinter.Button(self.ventana_principal, text = "Salir", relief="solid",
                command = self.salir).grid(row=11,column=1)

        self.cajaBuscar.focus()


      
    def poblar_tabla(self, vehiculos = None):
        #Vacia el treeview
        for i in self.treeview.get_children():
            self.treeview.delete(i)
        #Si no se recibe la lista de los vehiculos, a 'vehiculos' se le asignan todos los vehiculos:
        if not vehiculos:
            vehiculos = self.tallerMecanico.lista_vehiculos
        #Se llena el treeview:
        for v in vehiculos:
            item = self.treeview.insert("", tkinter.END, text=v.patente,
                              values=(v.tipo, v.marca, v.modelo, v.nombre, v.apellido, v.dni, v.cant_puertas_traccion), iid=v.patente)
     
     #Se agrega un nuevo vehiculo con sus atributos   
    def agregar_vehiculo(self):
        self.modalAgregar = tkinter.Toplevel(self.ventana_principal)
        #top.transient(parent)
        self.modalAgregar.grab_set()
        tkinter.Label(self.modalAgregar, text = "Tipo: ").grid()
        self.tipo = tkinter.Entry(self.modalAgregar)
        self.tipo.grid(row=0,column=1,columnspan=2)
        self.tipo.focus()
        tkinter.Label(self.modalAgregar, text = "Patente: ").grid(row=1)
        self.patente = tkinter.Entry(self.modalAgregar)
        self.patente.grid(row=1, column=1, columnspan=2)
        tkinter.Label(self.modalAgregar, text = "Marca: ").grid(row=2)
        self.marca = tkinter.Entry(self.modalAgregar)
        self.marca.grid(row=2,column=1,columnspan=8)
        tkinter.Label(self.modalAgregar, text = "Modelo: ").grid(row=3)
        self.modelo = tkinter.Entry(self.modalAgregar)
        self.modelo.grid(row=3, column=1, columnspan=2)
        tkinter.Label(self.modalAgregar, text = "Nombre: ").grid(row=4)
        self.nombre = tkinter.Entry(self.modalAgregar)
        self.nombre.grid(row=4,column=1,columnspan=2)
        tkinter.Label(self.modalAgregar, text = "Apellido: ").grid(row=5)
        self.apellido = tkinter.Entry(self.modalAgregar)
        self.apellido.grid(row=5, column=1, columnspan=2)
        tkinter.Label(self.modalAgregar, text = "DNI: ").grid(row=6)
        self.dni = tkinter.Entry(self.modalAgregar)
        self.dni.grid(row=6,column=1,columnspan=2)
        tkinter.Label(self.modalAgregar, text = "Cant_Puertas_Traccion: ").grid(row=7)
        self.cant_puertas_traccion = tkinter.Entry(self.modalAgregar)
        self.cant_puertas_traccion.grid(row=7, column=1, columnspan=2)


        botonOK = tkinter.Button(self.modalAgregar, text="Guardar",
                command=self.agregar_ok)
        self.modalAgregar.bind("<Return>", self.agregar_ok)
        botonOK.grid(row=8)
        botonCancelar = tkinter.Button(self.modalAgregar, text = "Cancelar",
                command = self.modalAgregar.destroy)
        botonCancelar.grid(row=8,column=2)
        
    #Cuenta la cantidad de vehiculos que ingresaron al taller distinguidos si son Autos o Camioneta
    def contar_vehiculo(self):
        self.modalAgregar = tkinter.Toplevel(self.ventana_principal)
        self.modalAgregar.grab_set()
        tkinter.Label(self.modalAgregar, text = "Ingrese tipo de vehiculo (Auto o Camioneta) [A/C]: ",).grid()
        botonSeleccion = self.ModalAgregar=tk.Radiobutton(self.modalAgregar,text="Auto", variable=self.modalAgregar, value=1)
        self.tipo = tkinter.Entry(self.modalAgregar)
        self.tipo.grid(row=0,column=1,columnspan=2)
        self.tipo.focus()
        botonOK = tkinter.Button(self.modalAgregar, text="Contar",
                command=self.contar_ok)
        self.modalAgregar.bind("<Return>",  self.contar_ok)
        botonOK.grid(row=8)
        botonCancelar = tkinter.Button(self.modalAgregar, text = "Cancelar",
                command = self.modalAgregar.destroy)
        botonCancelar.grid(row=8,column=2)
        botonResultado = tkinter.Button(self.modalAgregar, text = self.contar_ok,
                        command=self.contar_ok)
        
    #Funcion llamada por contar_vehiculo 
    def contar_ok(self):
        resultado = self.tallerMecanico.contar_veh(self.tipo.get())
        tkinter.Label(self.modalAgregar, text = resultado).grid()
        
        #print (resultado)
        
    #Agregar un nuevo vehiculo
    def agregar_ok(self, event=None):
        vehiculo = self.tallerMecanico.agregar_vehiculo(self.tipo.get(), self.patente.get(),self.marca.get(), self.modelo.get(),self.nombre.get(), self.apellido.get(),self.dni.get(), self.cant_puertas_traccion.get())
        self.modalAgregar.destroy()
        item = self.treeview.insert("", tkinter.END, text=vehiculo.patente,
                                        values=(vehiculo.tipo, vehiculo.marca, vehiculo.modelo, vehiculo.nombre, vehiculo.apellido, vehiculo.dni, vehiculo.cant_puertas_traccion))
        print(self.treeview.set(item))

    #Boton de Modificar Vehiculo
    def modificar_vehiculo(self):
        if not self.treeview.selection():
            messagebox.showwarning("Sin selección",
                    "Seleccione primero el vehiculo a modificar")
            return False
        item = self.treeview.selection()        
        patente = self.treeview.item(item)['text']

        #En consola, al clickear en 'Modificar vehiculo' lo busca por el atributo patente
        vehiculo = self.tallerMecanico.buscar_por_patente(patente)
        
        
        #El siguiente listado muestra la pantalla que se abre al clickear "Modificar vehiculo"
        self.modalModificar = tkinter.Toplevel(self.ventana_principal)
        self.modalModificar.grab_set()
        tkinter.Label(self.modalModificar, text = "Tipo: ").pack()
        self.tipo = tkinter.Entry(self.modalModificar)
        self.tipo.insert(0,vehiculo.tipo)
        self.tipo.pack()
        self.tipo.focus()
        tkinter.Label(self.modalModificar, text = "Marca: ").pack()
        self.marca = tkinter.Entry(self.modalModificar)
        self.marca.insert(0,vehiculo.marca)
        self.marca.pack()
        tkinter.Label(self.modalModificar, text = "Modelo: ").pack()
        self.modelo = tkinter.Entry(self.modalModificar)
        self.modelo.insert(0,vehiculo.modelo)
        self.modelo.pack()
        tkinter.Label(self.modalModificar, text = "Nombre: ").pack()
        self.nombre = tkinter.Entry(self.modalModificar)
        self.nombre.insert(0,vehiculo.nombre)
        self.nombre.pack()
        tkinter.Label(self.modalModificar, text = "Apellido: ").pack()
        self.apellido = tkinter.Entry(self.modalModificar)
        self.apellido.insert(0,vehiculo.apellido)
        self.apellido.pack()
        tkinter.Label(self.modalModificar, text = "DNI: ").pack()
        self.dni = tkinter.Entry(self.modalModificar)
        self.dni.insert(0,vehiculo.dni)
        self.dni.pack()
        tkinter.Label(self.modalModificar, text = "Cant_Puertas_Traccion : ").pack()
        self.cant_puertas_traccion = tkinter.Entry(self.modalModificar)
        self.cant_puertas_traccion.insert(0,vehiculo.cant_puertas_traccion)
        self.cant_puertas_traccion.pack()

        botonOK = tkinter.Button(self.modalModificar, text="Guardar",
                command=self.modificar_ok)
        self.modalModificar.bind("<Return>", self.modificar_ok)
        botonOK.pack()
        botonCancelar = tkinter.Button(self.modalModificar, text = "Cancelar",
                                       command = self.modalModificar.destroy)
        botonCancelar.pack()

    def modificar_ok(self, event=None):
        item = self.treeview.selection()        
        patente = self.treeview.item(item)['text']
        print("Modificado el vehiculo ", patente)
        self.tallerMecanico.modificar_todo_gui(patente, self.tipo.get(), self.marca.get(), self.modelo.get(), self.nombre.get(), self.apellido.get(), self.dni.get(), self.cant_puertas_traccion.get())
        self.treeview.set(self.treeview.selection()[0], column="tipo",
                          value = self.tipo.get())
        self.treeview.set(self.treeview.selection()[0], column="marca",
                          value = self.marca.get())
        self.treeview.set(self.treeview.selection()[0], column="modelo",
                          value = self.modelo.get())
        self.treeview.set(self.treeview.selection()[0], column="nombre",
                          value = self.nombre.get())
        self.treeview.set(self.treeview.selection()[0], column="apellido",
                          value = self.apellido.get())
        self.treeview.set(self.treeview.selection()[0], column="dni",
                          value = self.dni.get())
        self.treeview.set(self.treeview.selection()[0], column="cant_puertas_traccion",
                          value = self.cant_puertas_traccion.get())
        self.modalModificar.destroy()
   
    def eliminar_vehiculo(self):
        if not self.treeview.selection():
            messagebox.showwarning("Sin selección",
                    "Seleccione primero el vehiculo a eliminar")
            return False
        else:
            resp = messagebox.askokcancel("Confirmar",
                    "¿Está seguro de eliminar el vehiculo?")
            if resp:
                patente = self.treeview.selection()[0]
                self.treeview.delete(self.treeview.selection()[0])
                self.tallerMecanico.eliminar_vehiculo(patente)
            else:
                return False
    #Busca vehicuo por nombre o apellido ingresado parcial
    def buscar_vehiculo(self):
        filtro = self.cajaBuscar.get()
        vehiculos = self.tallerMecanico.buscar_por_nombre_apellido(filtro)
        if vehiculos:
            self.poblar_tabla(vehiculos)
        else:
            messagebox.showwarning("Sin resultados",
                                "Ningun vehiculo coincide con la búsqueda")

    #Busca por patente completa
    def buscar_patente(self):
        busqueda = self.cajaBuscarPatente.get()
        veh = self.tallerMecanico.buscar_por_patente(busqueda)
        if veh:
            self.poblar_tabla([veh])
        else:
            messagebox.showwarning("Sin resultados",
                                "Ninguna patente coincide con la búsqueda")

    
    def salir(self):
        print(self.tallerMecanico.lista_vehiculos)
        self.repositorio.guardar_todo(self.tallerMecanico.lista_vehiculos)
        self.ventana_principal.destroy()

if __name__ == "__main__":
    gui = Gui()
    gui.ventana_principal.mainloop()