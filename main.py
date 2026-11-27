from tkinter import Tk
from views.coches_views import CochesView
from controllers.coches_controller import CochesController

class App(CochesView, CochesController):
    def __init__(self,ventana):
        self.ventana=ventana
        self.ventana.title("Gestion de coches")
        self.ventana.geometry("800x600")
        self.ventana.resizable(0,0)
        self.main()


if __name__=="__main__":
    ventana=Tk()
    app=App(ventana)
    ventana.mainloop()
    
    

