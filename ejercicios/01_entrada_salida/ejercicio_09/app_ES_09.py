import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Tomas Leon
apellido: Curto Eivers
---
Ejercicio: entrada_salida_09
---
Enunciado:
Al presionar el botón  'Calcular', se deberán obtener los valores contenidos en las cajas de texto (txtSueldo y txtIncremento), 
transformarlos en números y mostrar el importe de sueldo actualizado con el incremento porcentual utilizando el Dialog Alert.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Sueldo")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_sueldo = customtkinter.CTkEntry(master=self)
        self.txt_sueldo.grid(row=0, column=1)
        
        self.label2 = customtkinter.CTkLabel(master=self, text="% de Incremento")
        self.label2.grid(row=1, column=0, padx=20, pady=10)
        
        self.txt_incremento = customtkinter.CTkEntry(master=self)
        self.txt_incremento.grid(row=1, column=1)
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        sueldo = int(self.txt_sueldo.get())
        incremento = int(self.txt_incremento.get())
        aumento = sueldo * (incremento/100)
        sueldo_final = sueldo + aumento
        sueldo_texto = str(sueldo)
        incremento_texto = str(incremento)
        sueldo_final_texto = str(sueldo_final)
        alert("EJ 09", "El sueldo actualizado calculado con un sueldo inicial de "+sueldo_texto+" y un incremento del "+incremento_texto+"% resulta en "+sueldo_final_texto)

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()