from models import coches_models as coches
from tkinter import messagebox

class CochesController:
    def insertar_controller(self):
        coche1=coches.CochesModel(self._marca.get(),self._color.get(),self._modelo.get(),self._velocidad.get(),self._potencia.get(),self._asientos.get())
        respuesta=coche1.insertar()
        self.respuesta_sql(respuesta)
        del coche1

    def eliminar_controller(self):
            id=self.id.get()
            resp=self.confirmar_eliminacion("eliminar")
            if resp:
                respuesta=coches.CochesModel.eliminar(id)
            else:
                respuesta=False
            self.respuesta_sql(respuesta)

    def consultar_controller(self,filas):
        registros= coches.CochesModel.consultar()
        if len(registros)>0:
            num_coches=1
            for fila in registros:
                filas=filas+f"\n{num_coches:<20}{fila[0]:<20}{fila[1]:<20}{fila[2]:<20}{fila[3]:<20}{fila[4]:<20}{fila[5]:<20}{fila[6]:<20}"
                num_coches+=1
        else:
                print("\n\n\t ¡No existen datos que mostrarpor el momento ...!")
                
        return filas

    def modificar_controller(self):
        id=self.id.get()
        coche1=coches.CochesModel(self._marca.get(),self._color.get(),self._modelo.get(),self._velocidad.get(),self._potencia.get(),self._asientos.get())
        respuesta=coche1.actualizar(id)
        self.respuesta_sql(respuesta)
        del coche1

    def buscar_controller(self,tipo_accion):
        id=self.id.get()
        coche1=coches.CochesModel.buscar(id)
        if len(coche1)>0:
            messagebox.showinfo(title="...¡ Registro Encontrado !...",message=f"...¡El registro fue encontrado con exisato, puedes {tipo_accion}!...")
            self.cambiar_estado_btn(True,tipo_accion)
            if tipo_accion=="modificar":
                self.var_marca.set(coche1[0][1])
                self.var_color.set(coche1[0][2])
                self.var_modelo.set(coche1[0][3])
                self.var_velocidad.set(coche1[0][4])
                self.var_potencia.set(coche1[0][5])
                self.var_asientos.set(coche1[0][6])
            
        else:
            messagebox.showerror(title="...¡ verifique por favor !...",message=f"...¡El registro no fue encontrado, no es posible {tipo_accion}!...")
            self.cambiar_estado_btn(False,tipo_accion)      

    def mostrar_coches(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for row in coches.CochesModel.consultar():
            self.tree.insert("", "end", values=row)

