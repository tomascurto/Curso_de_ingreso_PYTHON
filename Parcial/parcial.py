import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre: Tomás León
Apellido: Curto Eivers
DNI: 41738563

Una distribuidora de bebidas llena 10 comiones con sus productos y necesita guardar ciertos datos de cada una:

-Nombre del conductor
-Cantidad de litros de agua transportada($300 el litro)
-Cantidad de litros de gaseosa transportada ($600 el litro)
-Cantidad de litros de cerveza transportada ($800 el litro)
-Cantidad de litros de vino transportada ($1000 el litro)

Obligatorio: Informar el promedio de litros totales por camion.

Por  terminación de DNI: 
deberá realizar dos informes,
para determinar que informe hacer, tenga en cuenta lo siguiente:
    
    1- Tome el último número de su DNI Personal (Ej 4) y realiza ese informe (Ej, Realizar informe 4)

    2- Tome el último número de su DNI Personal (Ej 4), y restarle al número 9 (Ej 9-4 = 5). 
    Realiza el informe correspondiente al número obtenido.

EL RESTO DE LOS INFORMES LOS PUEDE IGNORAR. 

0)Debemos mostrar que tipo de bebida se transportó en mayor cantidad (cerveza, agua, gaseosa o vino).
1)Debemos mostrar el total de facturación del agua y la gaseosa vendida que estará dado por cada litro de gaseosa $600 y cada litro de agua a $300.
2)Debemos mostrar el total de facturación de la cerveza y el vino vendido que estará dado por cada litro de cerveza $800 y cada litro de vino a $1000.
3)Si la empresa supera la facturación de 350000 pesos deberá pagar un 8% de ingresos brutos. Informar si lo paga y de ser así el monto del impuesto.
4)Si la empresa supera la facturación de 700000 pesos deberá pagar un 15% de impuesto a las ganancias. Informar si lo paga y de ser así el monto del impuesto.
5)Debemos mostrar que tipo de bebida se transportó en menor cantidad (cerveza, agua, gaseosa o vino).
6)Informar el porcentaje de agua transportada y de gaseosa transportada en relación al total de litros transportados.
7)Informar el porcentaje de cerveza transportada y de vino transportado en relación al total de litros transportados.
8)Informar el primer ingreso (camion) que transporte mas de 100 litros.
9)Informar el primer ingreso (camion) que transporte menos de 50 litros.

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("Simulacro Parcial")

        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar", command=self.btn_cargar_on_click)
        self.btn_cargar.grid(row=3, padx=20, pady=20, columnspan=2, sticky="nsew")
       
        self.btn_informar= customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=5, padx=20, pady=20, columnspan=2, sticky="nsew")        


        self.lista_nombre = []
        self.lista_litros_agua = []
        self.lista_litros_gaseosa = []
        self.lista_litros_cerveza = []
        self.lista_litros_vino = []



    def btn_cargar_on_click(self):
        for i in range(0, 10, 1):
            #nombre del conductor
            nombre = prompt("Nombre", "Ingrese el nombre del conductor.") 
            while nombre == None or nombre.isalpha() != True:
                nombre = prompt("Nombre", "Ingrese el nombre del conductor, solo se aceptan caracteres alfabéticos.")
            #-Cantidad de litros de agua transportada($300 el litro)
            litros_agua = prompt("Litros de agua", "Ingrese con caracteres numéricos los litros de agua que transporta el camión.")
            while litros_agua == None or litros_agua.isdigit() != True:
                alert("Error", "Debe ingresarse un número positivo con caracteres numéricos.")
                litros_agua = prompt("Agua", "Ingrese con caracteres numéricos los litros de agua que transporta el camión.")
            litros_agua = int(litros_agua)
            #-Cantidad de litros de gaseosa transportada ($600 el litro)
            litros_gaseosa = prompt("Litros de gaseosa", "Ingrese con caracteres numéricos los litros de gaseosa que transporta el camión.")
            while litros_gaseosa == None or litros_gaseosa.isdigit() != True:
                alert("Error", "Debe ingresarse un número positivo con caracteres numéricos.")
                litros_gaseosa = prompt("Gaseosa", "Ingrese con caracteres numéricos los litros de gaseosa que transporta el camión.")
            litros_gaseosa = int(litros_gaseosa)
            #-Cantidad de litros de cerveza transportada ($800 el litro)
            litros_cerveza = prompt("Litros de cerveza", "Ingrese con caracteres numéricos los litros de cerveza que transporta el camión.")
            while litros_cerveza == None or litros_cerveza.isdigit() != True:
                alert("Error", "Debe ingresarse un número positivo con caracteres numéricos.")
                litros_cerveza = prompt("Cerveza", "Ingrese con caracteres numéricos los litros de cerveza que transporta el camión.")
            litros_cerveza = int(litros_cerveza)
            #-Cantidad de litros de vino transportada ($1000 el litro) 
            litros_vino = prompt("Litros de vino", "Ingrese con caracteres numéricos los litros de vino que transporta el camión.")
            while litros_vino == None or litros_vino.isdigit() != True:
                alert("Error", "Debe ingresarse un número positivo con caracteres numéricos.")
                litros_vino = prompt("Vino", "Ingrese con caracteres numéricos los litros de vino que transporta el camión.")
            litros_vino = int(litros_vino)
            #carga a listas
            self.lista_nombre.append(nombre)
            self.lista_litros_agua.append(litros_agua)
            self.lista_litros_gaseosa.append(litros_gaseosa)
            self.lista_litros_cerveza.append(litros_cerveza)
            self.lista_litros_vino.append(litros_vino)


#-Nombre del conductor
#-Cantidad de litros de agua transportada($300 el litro)
#-Cantidad de litros de gaseosa transportada ($600 el litro)
#-Cantidad de litros de cerveza transportada ($800 el litro)
#-Cantidad de litros de vino transportada ($1000 el litro)   
       
# Informar el promedio de litros totales por camion.
#3)Si la empresa supera la facturación de 350000 pesos deberá pagar un 8% de ingresos brutos. Informar si lo paga y de ser así el monto del impuesto.
#6)Informar el porcentaje de agua transportada y de gaseosa transportada en relación al total de litros transportados.            

    def btn_informar_on_click(self):
        # Informar el promedio de litros totales por camion.
        acumulador_litros_totales = 0
        # Suma todos los litros de todos los camiones.
        for i in range(0, 10, 1):
            acumulador_litros_totales += self.lista_litros_agua[i] + self.lista_litros_gaseosa[i] + self.lista_litros_cerveza[i] + self.lista_litros_vino[i] 
        # Al tener el total de litros totales para todos los camiones, para obtener el promedio se divide entre los 10 camiones.
        promedio = acumulador_litros_totales / 10
        # Para el mensaje se necesita como string.
        promedio = str(promedio)
        mensaje_promedio = "El promedio de litros totales por camión es de " + promedio + " litros."
        # Informar
        alert("Informar", mensaje_promedio)

        #3)Si la empresa supera la facturación de 350000 pesos deberá pagar un 8% de ingresos brutos. Informar si lo paga y de ser así el monto del impuesto.
        facturacion = 0
        for i in range(0, 10, 1):
            facturacion += self.lista_litros_agua[i] * 300 + self.lista_litros_gaseosa[i] * 600 + self.lista_litros_cerveza[i] * 800 + self.lista_litros_vino[i] *1000
        if facturacion < 350000:
            facturacion = str(facturacion)
            mensaje_impuesto = "La facturación es de " + facturacion + " y no supera los $350000, por lo tanto no se pagan ingresos brutos."
        else:
            impuesto = facturacion * 0.08
            facturacion = str(facturacion)
            impuesto = str(impuesto)
            mensaje_impuesto = "La facturación es de " + facturacion + " y supera los $350000, por lo tanto se pagan " + impuesto + " de ingresos brutos."
        alert("Informar", mensaje_impuesto)

        #6)Informar el porcentaje de agua transportada y de gaseosa transportada en relación al total de litros transportados.
        acumulador_litros_agua_totales = 0
        acumulador_litros_gaseosa_totales = 0
        # Suma todos los litros de todos los camiones.
        for i in range(0, 10, 1):
            acumulador_litros_agua_totales += self.lista_litros_agua[i]
            acumulador_litros_gaseosa_totales += self.lista_litros_gaseosa[i]
        # Al tener el total de litros totales para todos los camiones, comparo.
        porcentaje_agua = (acumulador_litros_agua_totales / acumulador_litros_totales) * 100
        porcentaje_gaseosa = (acumulador_litros_gaseosa_totales / acumulador_litros_totales) * 100
        # Para el mensaje se necesita como string.
        porcentaje_agua = str(porcentaje_agua)
        porcentaje_gaseosa = str(porcentaje_gaseosa)
        mensaje_porcentajes = "El prorcentaje total de litros de agua es de " + porcentaje_agua + "% y el de litros de gaseosa es de " + porcentaje_gaseosa + "%."
        alert("Informar", mensaje_porcentajes)


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()