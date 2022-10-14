#!/usr/bin/python3
from tallerMecanico import TallerMecanico
from repositorioTallerMecanico import RepositorioTallerMecanico
import tkinter
from tkinter import ttk
from tkinter import messagebox

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
        self.ventana_principal.title("Taller Mecanico")

        # Interfaz
        botonAgregarVehiculo = tkinter.Button(self.ventana_principal,text="Agregar vehiculo", 
                           command = self.agregar_vehiculo).grid(row=0, column=0)
        botonModificarVehiculoPatente=tkinter.Button(self.ventana_principal,text="Modificar Vehiculo",
                           command = self.modificar_vehiculo).grid(row=0, column=1)
        botonEliminarVehiculo=tkinter.Button(self.ventana_principal, text = "Eliminar Vehiculo",
                           command = self.eliminar_vehiculo).grid(row=0, column=2)

        tkinter.Label(self.ventana_principal,text="Buscar").grid(row=1,column=0)

        # Aca se esribe el texto
        self.cajaBuscar = tkinter.Entry(self.ventana_principal)
        self.cajaBuscar.grid(row=1, column=1)
        botonBuscar = tkinter.Button(self.ventana_principal, text = "Buscar por nombre o apellido",
                           command = self.buscar_vehiculo).grid(row=1, column=2)

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

        botonSalir = tkinter.Button(self.ventana_principal, text = "Salir",
                command = self.salir).grid(row=11,column=1)

        self.cajaBuscar.focus()


      
    def poblar_tabla(self, vehiculos = None):
        #Vaciamos el Treeview, si tuviera algún item:
        for i in self.treeview.get_children():
            self.treeview.delete(i)
        #Si no recibimos la lista de notas, le asignamos todas las notas:
        if not vehiculos:
            vehiculos = self.tallerMecanico.lista_vehiculos
        #Poblamos el treeview:
        for v in vehiculos:
            item = self.treeview.insert("", tkinter.END, text=v.patente,
                              values=(v.tipo, v.marca, v.modelo, v.nombre, v.apellido, v.dni, v.cant_puertas_traccion), iid=v.patente)
        
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

    def agregar_ok(self, event=None):
        vehiculo = self.tallerMecanico.agregar_vehiculo(self.tipo.get(), self.patente.get(),self.marca.get(), self.modelo.get(),self.nombre.get(), self.apellido.get(),self.dni.get(), self.cant_puertas_traccion.get())
        self.modalAgregar.destroy()
        item = self.treeview.insert("", tkinter.END, text=vehiculo.patente,
                                        values=(vehiculo.tipo, vehiculo.marca, vehiculo.modelo, vehiculo.nombre, vehiculo.apellido, vehiculo.dni, vehiculo.cant_puertas_traccion))
        #print(self.treeview.set(item))

    def modificar_vehiculo(self):
        if not self.treeview.selection():
            messagebox.showwarning("Sin selección",
                    "Seleccione primero el vehiculo a modificar")
            return False
        #id = int(self.treeview.selection()[0][1:])
        item = self.treeview.selection()        
        patente = self.treeview.item(item)['text']
        #id = self.treeview.item(item, option="text")

        #Para probar:
        print(patente)

        vehiculo = self.tallerMecanico.buscar_por_patente(patente)
        self.modalModificar = tkinter.Toplevel(self.ventana_principal)
        self.modalModificar.grab_set()
        tkinter.Label(self.modalModificar, text = "Tipo: ").pack()
        self.tipo = tkinter.Entry(self.modalModificar)
        self.tipo.insert(0,vehiculo.tipo)
        self.tipo.pack()
        self.tipo.focus()
        # tkinter.Label(self.modalModificar, text = "Patente: ").pack()
        # self.patente = tkinter.Entry(self.modalModificar)
        # self.patente.insert(0,vehiculo.patente)
        # self.patente.pack()
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
        #id = int(self.treeview.selection()[0][1:])
        #idtree = self.treeview.selection()[0]
        self.tallerMecanico.modificar_todo_gui(patente, self.tipo.get(), self.marca.get(), self.modelo.get(), self.nombre.get(), self.apellido.get(), self.dni.get(), self.cant_puertas_traccion.get())
       # self.treeview.set(self.treeview.selection()[0], column="patente",
              #            value = self.patente.get())
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

    def buscar_vehiculo(self):
        filtro = self.cajaBuscar.get()
        vehiculos = self.tallerMecanico.buscar_por_nombre_apellido(filtro)
        if vehiculos:
            self.poblar_tabla(vehiculos)
        else:
            messagebox.showwarning("Sin resultados",
                                "Ningun vehiculo coincide con la búsqueda")
    
    def salir(self):
        print(self.tallerMecanico.lista_vehiculos)
        self.repositorio.guardar_todo(self.tallerMecanico.lista_vehiculos)
        self.ventana_principal.destroy()

if __name__ == "__main__":
    gui = Gui()
    gui.ventana_principal.mainloop()