from tkinter import *
from tkinter import messagebox, StringVar, ttk

class CochesView:
    def borrarPantalla(self):
        for widget in self.ventana.winfo_children():
            widget.destroy()

    def barraMenu(self):
        #Menu de Opciones
        menuBar = Menu(self.ventana)
        self.ventana.config(menu=menuBar)
        
        
        menuPrincipal = Menu(menuBar, tearoff=False)
        menuBar.add_cascade(label="Principal" , menu=menuPrincipal)
        menuPrincipal.add_command(label="Menu Principal",command=self.main)
        menuPrincipal.add_command(label="Menu Acciones",command=self.menu_acciones)
        menuPrincipal.add_separator()
        menuPrincipal.add_command(label="Salir",command=self.ventana.quit)
        
        accionesMenu = Menu(menuBar , tearoff=False)
        menuBar.add_cascade(label="Acciones" , menu=accionesMenu)
        accionesMenu.add_command(label="Agregar",command=self.insertar_view)
        accionesMenu.add_command(label="Borrar",command=self.eliminar_view)
        accionesMenu.add_command(label="Modificar",command=self.modificar_view)
        accionesMenu.add_command(label="Mostrar",command=self.consultar_view)
        accionesMenu.add_command(label="Agregar",command=self.insertar_view)
        accionesMenu.add_separator()
        accionesMenu.add_command(label="Regresar",command=self.main)

    def menu_acciones(self):
        self.borrarPantalla()
        self.barraMenu()
        tipo="Coches"
        Label(self.ventana,text=f"\n...::: menu de {tipo} :::... \n").pack(pady=10)
        self.frame1=Frame(self.ventana)
        self.frame1.pack(pady=10)
        Button(self.frame1,text="Agregar",width=10,height=3,command=self.insertar_view).grid(row=0,column=0,pady=5,padx=5,sticky="e")
        Button(self.frame1,text="Borrar",width=10,height=3,command=self.eliminar_view).grid(row=0,column=1,pady=5,padx=5,sticky="e")
        Button(self.frame1,text="Modificar",width=10,height=3,command=self.modificar_view).grid(row=1,column=0,pady=5,padx=5,sticky="e")
        Button(self.frame1,text="Mostrar",width=10,height=3,command=self.consultar_view).grid(row=1,column=1,pady=5,padx=5,sticky="e")
        Button(self.frame1,text="Salir",width=10,height=3,command=self.main).grid(row=2,column=0,columnspan=2,pady=5,padx=5)

    def main (self):
        self.borrarPantalla()
        self.barraMenu()
        Label(self.ventana,text="\n...::: M E N U   P R I N C I P A L :::...").pack(pady=10)
        self.frame1=Frame(self.ventana)
        self.frame1.pack(pady=10)
        Button(self.frame1,text="1.- Coches",width=10,height=3,command=self.menu_acciones).grid(row=0,column=0,pady=5,padx=5,sticky="e")
        Button(self.frame1,text="2.- Salir",width=10,height=3,command=self.ventana.quit).grid(row=1,column=0,pady=5,padx=5,sticky="w")

    def insertar_view(self):
        self.borrarPantalla()
        self.barraMenu()
        Label(self.ventana,text="...Ingresar los datos de Coche").pack(pady=10)
        
        self.frame1=Frame(self.ventana)
        self.frame1.pack(pady=10)
        
        
        Label(self.frame1,text="Marca").grid(row=0,column=0,pady=5,padx=5,sticky="e")
        self._marca=Entry(self.frame1)
        self._marca.focus()
        self._marca.grid(row=0,column=1,pady=5,padx=5,sticky="w")
        
        Label(self.frame1,text="Color").grid(row=1,column=0,pady=5,padx=5,sticky="e")
        self._color=Entry(self.frame1)
        self._color.grid(row=1,column=1,pady=5,padx=5,sticky="w")
        
        Label(self.frame1,text="Modelo").grid(row=2,column=0,pady=5,padx=5,sticky="e")
        self._modelo=Entry(self.frame1)
        self._modelo.grid(row=2,column=1,pady=5,padx=5,sticky="w")
        
        Label(self.frame1,text="Velocidad").grid(row=3,column=0,pady=5,padx=5,sticky="e")
        self._velocidad=Entry(self.frame1)
        self._velocidad.grid(row=3,column=1,pady=5,padx=5,sticky="w")
        
        Label(self.frame1,text="Potencia").grid(row=4,column=0,pady=5,padx=5,sticky="e")
        self._potencia=Entry(self.frame1)
        self._potencia.grid(row=4,column=1,pady=5,padx=5,sticky="w")
        
        Label(self.frame1,text="Asientos").grid(row=5,column=0,pady=5,padx=5,sticky="e")
        self._asientos=Entry(self.frame1)
        self._asientos.grid(row=5,column=1,pady=5,padx=5,sticky="w")
        
        Button(self.frame1,text="Guardar",command=lambda:(self.insertar_controller(),self.insertar_view())).grid(row=6,column=0,pady=10,padx=5,sticky="e")
        Button(self.frame1,text="Regresar",command=self.menu_acciones).grid(row=6,column=1,pady=10,padx=5,sticky="e")

    def eliminar_view(self):
        self.borrarPantalla()
        self.barraMenu()
        self.frame1=Frame(self.ventana)
        self.frame1.pack(pady=10)
        Label(self.frame1,text="...Ingresar el ID del Coche a eliminar").grid(row=0,column=0,columnspan=2,pady=10)
        self.frame1=Frame(self.ventana)
        self.frame1.pack(pady=10)
            
        Label(self.frame1,text="ID").grid(row=0,column=0,pady=5,padx=5,sticky="e")
        self.id=Entry(self.frame1)
        self.id.grid(row=0,column=1,pady=5,padx=5,sticky="w")
        
        self.btn_buscar=Button(self.frame1,text="Buscar",command=lambda:self.buscar_controller("eliminar"))
        self.btn_buscar.grid(row=1,column=0,pady=10,padx=5,sticky="e")
            
            
        self.btn_eliminar=Button(self.frame1,text="Eliminar",state="disabled",command=lambda:(self.eliminar_controller(),self.eliminar_view()))
        self.btn_eliminar.grid(row=1,column=1,pady=10,padx=5,sticky="e")
        Button(self.frame1,text="Regresar",command=self.menu_acciones).grid(row=2,column=0,columnspan=2,pady=10,padx=5,sticky="s")  

    def modificar_view(self):
            self.borrarPantalla()
            self.barraMenu()
            Label(self.ventana,text="...Ingresar el ID del Coche a modificar").pack(pady=10)
            
            self.frame1=Frame(self.ventana)
            self.frame1.pack(pady=10)
                 
                    
            Label(self.frame1,text="ID").grid(row=0,column=0,pady=5,padx=5,sticky="e")
            self.id=Entry(self.frame1)
            self.id.focus()
            self.id.grid(row=0,column=1,pady=5,padx=5,sticky="w")
            
            self.btn_buscar=Button(self.frame1,text="Buscar",command=lambda:self.buscar_controller("modificar"))
            self.btn_buscar.grid(row=1,column=0,pady=10,columnspan=2,padx=5)
            
            # Variables asociadas a los campos
            self.var_marca=StringVar()
            self.var_color=StringVar()
            self.var_modelo=StringVar()
            self.var_velocidad=StringVar()
            self.var_potencia=StringVar()
            self.var_asientos=StringVar()
            
            self.frame2=Frame(self.ventana)
            self.frame2.pack(pady=10)

            Label(self.frame2,text="Nueva Marca").grid(row=0,column=0,pady=5,padx=5,sticky="e")
            self._marca=Entry(self.frame2,textvariable=self.var_marca)
            self._marca.grid(row=0,column=1,pady=5,padx=5,sticky="w")
                    
            Label(self.frame2,text="Nuevo Color").grid(row=1,column=0,pady=5,padx=5,sticky="e")
            self._color=Entry(self.frame2,textvariable=self.var_color)
            self._color.grid(row=1,column=1,pady=5,padx=5,sticky="w")
                    
            Label(self.frame2,text="Nuevo Modelo").grid(row=2,column=0,pady=5,padx=5,sticky="e")
            self._modelo=Entry(self.frame2,textvariable=self.var_modelo)
            self._modelo.grid(row=2,column=1,pady=5,padx=5,sticky="w")
                    
            Label(self.frame2,text="Nuevo Velocidad").grid(row=3,column=0,pady=5,padx=5,sticky="e")
            self._velocidad=Entry(self.frame2,textvariable=self.var_velocidad)
            self._velocidad.grid(row=3,column=1,pady=5,padx=5,sticky="w")
                    
            Label(self.frame2,text="Nueva Potencia").grid(row=4,column=0,pady=5,padx=5,sticky="e")
            self._potencia=Entry(self.frame2,textvariable=self.var_potencia)
            self._potencia.grid(row=4,column=1,pady=5,padx=5,sticky="w")
                    
            Label(self.frame2,text="Nuevos Asientos").grid(row=5,column=0,pady=5,padx=5,sticky="e")
            self._asientos=Entry(self.frame2,textvariable=self.var_asientos)
            self._asientos.grid(row=5,column=1,pady=5,padx=5,sticky="w")
                    
            self.btn_modificar=Button(self.ventana,text="Guardar",state="disabled",command=lambda:(self.modificar_controller(),self.modificar_view()))
            self.btn_modificar.pack(pady=10)
            
            Button(self.ventana,text="Regresar",command=self.menu_acciones).pack(pady=10)

    def consultar_view(self):
        self.borrarPantalla()
        self.barraMenu()
        Label(self.ventana,text="::: Consultar los coches :::").pack(pady=10)
        
        # Tabla
        self.tree =ttk.Treeview(self.ventana, columns=("ID", "Marca", "Color", "Modelo","Velocidad","Potencia","Asientos"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Marca", text="Marca")
        self.tree.heading("Color", text="Color")
        self.tree.heading("Modelo", text="Modelo")
        self.tree.heading("Velocidad", text="Velocidad")
        self.tree.heading("Potencia", text="Potencia")
        self.tree.heading("Asientos", text="Asientos")
        self.tree.pack(fill="both", expand=False)
        
        #Colocar los datos en la tabla
        self.mostrar_coches()
        
        Button(self.ventana,text="Regresar",command=self.menu_acciones).pack(pady=5)
        
        #filas=""
        #filas=self.consultar_controller(filas)
        #Label(self.ventana,text=f"{'No.':<20}{'ID':<20}{'Marca':<20}{'Color':<20}{'Modelo':<20}{'Velocidad':<20}{'Potencia':<20}{'Asientos':<20}").pack(pady=5)
        #Label(self.ventana,text=f"-"*100).pack(pady=5)
        #Label(self.ventana,text=f"{filas}").pack(pady=5)
        #Label(self.ventana,text=f"-"*100).pack(pady=5)
        
        
    def cambiar_estado_btn(self,estado,tipo_accion):
        if estado:
          if tipo_accion=="eliminar":
            self.btn_eliminar.config(state="normal")
          elif tipo_accion=="modificar":
            self.btn_modificar.config(state="normal")
            
        else:
            if tipo_accion=="eliminar":
                self.btn_eliminar.config(state="disabled")
            elif tipo_accion=="modificar":
                self.btn_modificar.config(state="disabled")

    def confirmar_eliminacion(self,tipo):
        resp=messagebox.askokcancel(title="...¡Atencion!...",message=f"...¿Deseas {tipo} este registro?...")
        if resp:
            return True
        else:
            return False

    def respuesta_sql(self,respuesta):
        if respuesta:
            messagebox.showinfo(title="... Exitoso ...",message="... ¡Accion Realizada con Exito!")
        else:
            messagebox.showerror(title="...¡ Verifique por favo !...",message="...¡Esta Accion no pudo realizarse en este momento!...")

