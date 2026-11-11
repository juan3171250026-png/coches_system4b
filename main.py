from coches.coches import Coches
from tkinter import Tk, Label, Entry, Button
from tkinter import messagebox

class App():
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("App")
        self.ventana.geometry("600x600")
        self.ventana.resizable(0, 0)

    def borrarPantalla(self):
        for widget in self.ventana.winfo_children():
            widget.destroy()

    def esperarTecla(self):
        input("... ! Oprima cualquier tecla para continuar ¡ ...")

    def terminarSistema(self):
        input("... ::: ! Gracias por usar nuestro sistema ¡ ::: ...")

    def opcionInvalida(self):
        input("... Opcion invalida oprima cualquier tecla para continuar...")

    def main(self):
        self.borrarPantalla()

        Label(self.ventana, text="::: Menu Principal :::").pack(pady=20)

        Button(
            self.ventana,
            text="1.- Coches",
            command=self.menu_coches
        ).pack(pady=10)

        Button(
            self.ventana,
            text="2.- Salir",
            command=self.ventana.quit
        ).pack(pady=10)

    def menu_acciones(self, tipo):
        self.borrarPantalla()

        Label(self.ventana, text=f"::: Menu de {tipo} :::").pack(pady=10)

        Button(
            self.ventana,
            text="1.- Agregar",
            command=self.insertar_coches_view
        ).pack(pady=10)

        Button(
            self.ventana,
            text="2.- Borrar",
            command=self.eliminar_coches_view
        ).pack(pady=10)

        Button(
            self.ventana,
            text="3.- Modificar",
            command=self.modificar_coches_view
        ).pack(pady=10)

        Button(
            self.ventana,
            text="4.- Mostrar",
            command=self.mostrar_coches_view
        ).pack(pady=10)

        Button(
            self.ventana,
            text="5.- Regresar",
            command=self.main
        ).pack(pady=10)

    def menu_coches(self):
        self.menu_acciones("Coches")

    # Vista insertar
    def insertar_coches_view(self):
        self.borrarPantalla()

        Label(self.ventana, text="... Ingresar datos del coche ...").pack(pady=10)

        Label(self.ventana, text="Marca: ").pack(pady=5)
        self.marca = Entry(self.ventana)
        self.marca.pack(pady=5)

        Label(self.ventana, text="Color: ").pack(pady=5)
        self.color = Entry(self.ventana)
        self.color.pack(pady=5)

        Label(self.ventana, text="Modelo: ").pack(pady=5)
        self.modelo = Entry(self.ventana)
        self.modelo.pack(pady=5)

        Label(self.ventana, text="Velocidad: ").pack(pady=5)
        self.velocidad = Entry(self.ventana)
        self.velocidad.pack(pady=5)

        Label(self.ventana, text="Potencia: ").pack(pady=5)
        self.potencia = Entry(self.ventana)
        self.potencia.pack(pady=5)

        Label(self.ventana, text="Asientos: ").pack(pady=5)
        self.asientos = Entry(self.ventana)
        self.asientos.pack(pady=5)

        Button(
            self.ventana,
            text="Agregar",
            command=lambda:
            {
                self.insertar_coches_controller(),
                self.insertar_coches_view()
            }
        ).pack(pady=10)

        Button(
            self.ventana,
            text="5.- Regresar",
            command=self.menu_coches
        ).pack(pady=10)

    # Vista eliminar
    def eliminar_coches_view(self):
        self.borrarPantalla()

        Label(
            self.ventana,
            text="... Ingresar el ID del coche a eliminar ..."
        ).pack(pady=10)

        Label(self.ventana, text="ID: ").pack(pady=5)
        self.id = Entry(self.ventana)
        self.id.pack(pady=5)

        Button(
            self.ventana,
            text="Eliminar",
            command=lambda:
            {
                self.eliminar_coches_controller(),
                self.eliminar_coches_view()
            }
        ).pack(pady=10)

        Button(
            self.ventana,
            text="5.- Regresar",
            command=self.menu_coches
        ).pack(pady=10)

    # Vista modificar
    def modificar_coches_view(self):
        self.borrarPantalla()

        Label(
            self.ventana,
            text="... Ingresar datos del coche a modificar ..."
        ).pack(pady=10)

        Label(self.ventana, text="ID: ").pack(pady=5)
        self.id = Entry(self.ventana)
        self.id.pack(pady=5)

        Label(self.ventana, text="Marca: ").pack(pady=5)
        self.marca = Entry(self.ventana)
        self.marca.pack(pady=5)

        Label(self.ventana, text="Color: ").pack(pady=5)
        self.color = Entry(self.ventana)
        self.color.pack(pady=5)

        Label(self.ventana, text="Modelo: ").pack(pady=5)
        self.modelo = Entry(self.ventana)
        self.modelo.pack(pady=5)

        Label(self.ventana, text="Velocidad: ").pack(pady=5)
        self.velocidad = Entry(self.ventana)
        self.velocidad.pack(pady=5)

        Label(self.ventana, text="Potencia: ").pack(pady=5)
        self.potencia = Entry(self.ventana)
        self.potencia.pack(pady=5)

        Label(self.ventana, text="Asientos: ").pack(pady=5)
        self.asientos = Entry(self.ventana)
        self.asientos.pack(pady=5)

        Button(
            self.ventana,
            text="Modificar",
            command=lambda:
            {
                self.modificar_coches_controller(),
                self.modificar_coches_view()
            }
        ).pack(pady=10)

        Button(
            self.ventana,
            text="5.- Regresar",
            command=self.menu_coches
        ).pack(pady=10)

    # Vista mostrar
    def mostrar_coches_view(self):
        self.borrarPantalla()

        Label(
            self.ventana,
            text="::: Lista de Coches :::"
        ).pack(pady=10)

        self.mostrar_coches_controller()

        Button(
            self.ventana,
            text="5.- Regresar",
            command=self.menu_coches
        ).pack(pady=10)

    # Controlador insertar
    def insertar_coches_controller(self):
        coches1 = Coches(
            self.marca.get(),
            self.color.get(),
            self.modelo.get(),
            self.velocidad.get(),
            self.potencia.get(),
            self.asientos.get()
        )

        respuesta = coches1.insertar()
        self.respuesta_sql(respuesta)
        del coches1

    # Controlador eliminar
    def eliminar_coches_controller(self):
        respuesta = Coches.eliminar(self.id.get())
        self.respuesta_sql(respuesta)

    # Controlador modificar
    def modificar_coches_controller(self):
        coches1 = Coches(
            self.marca.get(),
            self.color.get(),
            self.modelo.get(),
            self.velocidad.get(),
            self.potencia.get(),
            self.asientos.get()
        )

        respuesta = coches1.actualizar(self.id.get())
        self.respuesta_sql(respuesta)
        del coches1

    # Controlador mostrar
    def mostrar_coches_controller(self):
        respuesta = Coches.consultar()

        if respuesta:
            for coche in respuesta:
                Label(
                    self.ventana,
                    text=str(coche)
                ).pack(pady=5)
        else:
            messagebox.showinfo(
                title=":: Informacion ::",
                message="No hay coches registrados"
            )

    # Respuesta SQL
    def respuesta_sql(self, respuesta):
        if respuesta:
            messagebox.showinfo(
                title=":: Exitoso ::",
                message="Accion realizada con exito"
            )
        else:
            messagebox.showerror(
                title=":: Error ::",
                message="No se pudo realizar la accion"
            )


if __name__ == "__main__":
    ventana = Tk()
    app = App(ventana)
    ventana.geometry("600x600")
    app.main()
    ventana.mainloop()
