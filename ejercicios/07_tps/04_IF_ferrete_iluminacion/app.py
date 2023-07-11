import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Todas las lámparas están  al mismo precio de $800 pesos final.
		A.	Si compra 6 o más  lamparitas bajo consumo tiene un descuento del 50%. 
		B.	Si compra 5  lamparitas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40 % y si es de otra marca el descuento es del 30%.
		C.	Si compra 4  lamparitas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se hace un descuento del 25 % y si es de otra marca el descuento es del 20%.
		D.	Si compra 3  lamparitas bajo consumo marca "ArgentinaLuz"  el descuento es del 15%, si es  “FelipeLamparas” se hace un descuento del 10 % y si es de otra marca un 5%.
		E.	Si el importe final con descuento suma más de $4000  se obtien un descuento adicional de 5%.

nombre: Tomas Leon
apellido: Curto Eivers
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__() 

        # configure window
        self.title("UTN Fra")

        self.label1 = customtkinter.CTkLabel(master=self, text="Marca")
        self.label1.grid(row=0, column=0, padx=10, pady=10)
        
        self.combobox_marca = customtkinter.CTkComboBox(master=self, values=["ArgentinaLuz", "FelipeLamparas","JeLuz","HazIluminacion","Osram"])
        self.combobox_marca.grid(row=0, column=1, padx=10, pady=10)

        self.label2 = customtkinter.CTkLabel(master=self, text="Cantidad")
        self.label2.grid(row=1, column=0, padx=10, pady=10)

        self.combobox_cantidad = customtkinter.CTkComboBox(master=self, values= ["1", "2","3","4","5","6","7","8","9","10","11","12"])
        self.combobox_cantidad.grid(row=1, column=1, padx=10, pady=10)
                
        self.btn_calcular = customtkinter.CTkButton(master=self, text="Calcular", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_calcular_on_click(self):
        marca = self.combobox_marca.get()
        cantidad = int(self.combobox_cantidad.get())
        precio_unitario = 800
        precio_base = precio_unitario * cantidad
        if cantidad >= 6:
            porcentaje = 50
            descuento = precio_base * (porcentaje/100)
        elif cantidad == 5:
            if marca == "ArgentinaLuz":
                porcentaje = 40
                descuento = precio_base * (porcentaje/100)
            else:
                porcentaje = 30
                descuento = precio_base * (porcentaje/100)
        elif cantidad == 4:
            if marca == "ArgentinaLuz" or marca == "FelipeLamparas":
                porcentaje = 25
                descuento = precio_base * (porcentaje/100)
            else:
                porcentaje = 20
                descuento = precio_base * (porcentaje/100)
        elif cantidad == 3:
            if marca == "ArgentinaLuz":
                porcentaje = 15
                descuento = precio_base * (porcentaje/100)
            elif marca == "FelipeLamparas":
                porcentaje = 10
                descuento = precio_base * (porcentaje/100)
            else:
                porcentaje = 5
                descuento = precio_base * (porcentaje/100)
        else:
            descuento = 0
        precio_descontado = precio_base - descuento
        precio_descontado_str = str(precio_descontado)
        precio_base_str = str(precio_base)
        descuento_str = str(descuento)
        if cantidad >=3:
            porcentaje_str = str(porcentaje)
            if precio_descontado >= 4000:
                segundo_descuento = precio_descontado * (5/100)
                precio_final = precio_descontado - segundo_descuento
                precio_final_str = str(precio_final)
                mensaje = "Al precio base de $" + precio_base_str + " se le aplica un " + porcentaje_str + "% de descuento, y al sobrepasar los $4000 se le aplica otro 5% de descuento quedando el precio final de $" + precio_final_str
            elif precio_descontado < 4000:
                mensaje = "Al precio base de $" + precio_base_str + " se le aplica un " + porcentaje_str + "% de descuento, quedando el precio final de $" + precio_descontado_str
        else:
            mensaje = "El precio final es de $" + precio_descontado_str
        alert("TP 04", mensaje)    

        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()