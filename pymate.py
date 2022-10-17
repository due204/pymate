#!/bin/python3

from tkinter import Tk
from tkinter import Button
from tkinter import Label
from tkinter.ttk import Combobox
from os import system


class Mimate():
    def __init__(self, parent):
        # Vista principal
        self.parent = parent
        self.parent.title("Py Mate")
        vent_x = self.parent.winfo_screenwidth() // 2 - 200 // 2
        vent_y = self.parent.winfo_screenheight() // 2 - 150 // 2
        tam_y_pos = "300x" + "200+" + str(vent_x) + "+" + str(vent_y)
        self.parent.geometry(tam_y_pos)  # Ancho, largo y posicion
        self.parent.resizable(False, False)
        self.parent.bind("<KeyPress-Escape>", self.salir)
        
        self.vista()

    def vista(self):
        #Vista y posicionamiento de los widget
        #Labes
        self.label_home = Label(root, text="Icono de home")
        self.label_home.place(x=10, y=10)
        self.label_lugares = Label(root, text="Icono de lugares")
        self.label_lugares.place(x=10, y=40)
        self.label_red = Label(root, text="Icono de red")
        self.label_red.place(x=10, y=70)
        self.label_papelera = Label(root, text="Icono de papelera")
        self.label_papelera.place(x=10, y=100)
        self.label_volumenes = Label(root, text="Icono de volumenes")
        self.label_volumenes.place(x=10, y=130)

        #Comboboxs
        self.spin_home = Combobox(root, width=7, values=("Ver", "No ver"), state="readonly")
        self.spin_home.current(1)
        self.spin_home.place(x=200, y=10)
        self.spin_lugares = Combobox(root, width=7, values=("Ver", "No ver"), state="readonly")
        self.spin_lugares.current(1)
        self.spin_lugares.place(x=200, y=40)
        self.spin_red = Combobox(root, width=7, values=("Ver", "No ver"), state="readonly")
        self.spin_red.current(1)
        self.spin_red.place(x=200, y=70)
        self.spin_papelera = Combobox(root, width=7, values=("Ver", "No ver"), state="readonly")
        self.spin_papelera.current(1)
        self.spin_papelera.place(x=200, y=100)
        self.spin_volumenes = Combobox(root, width=7, values=("Ver", "No ver"), state="readonly")
        self.spin_volumenes.current(0)
        self.spin_volumenes.place(x=200, y=130)

        #Boton
        self.boton = Button(root, text="Guardar", command=self.guardar)
        self.boton.place(x=200, y=160)

    def guardar(self):
        #Obteniendo los datos
        self.home = self.validar(self.spin_home.get())
        system("gsettings set org.mate.caja.desktop home-icon-visible %s" %self.home)
        self.lugares = self.validar(self.spin_lugares.get())
        system("gsettings set org.mate.caja.desktop computer-icon-visible %s" %self.lugares)
        self.red = self.validar(self.spin_red.get())
        system("gsettings set org.mate.caja.desktop network-icon-visible %s" %self.red)
        self.papelera = self.validar(self.spin_papelera.get())
        system("gsettings set org.mate.caja.desktop trash-icon-visible %s" %self.papelera)
        self.volumenes = self.validar(self.spin_volumenes.get())
        system("gsettings set org.mate.caja.desktop volumes-visible %s" %self.volumenes)
        self.salir()

    def validar(self, dato):
        #Valida los datos
        if dato == "Ver":
            return "true"
        else:
            return "false"

    def salir(self, *args):
        self.parent.destroy()
        self.parent.quit()
        print("Saliendo del programa")


if __name__ == "__main__":
    root = Tk()
    Mimate(root)
    root.mainloop()