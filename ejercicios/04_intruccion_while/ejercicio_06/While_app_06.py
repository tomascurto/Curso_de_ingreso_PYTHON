import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar 5 números mediante prompt. 
Calcular la suma acumulada y el promedio de los números ingresados. 
Luego informar los resultados en las cajas de texto txt_suma_acumulada y txt_promedio

nombre: Tomas Leon
apellido: Curto Eivers

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
        
        self.txt_suma_acumulada = customtkinter.CTkEntry(master=self, placeholder_text="Suma acumulada")
        self.txt_suma_acumulada.grid(row=0, padx=20, pady=20)

        self.txt_promedio = customtkinter.CTkEntry(master=self, placeholder_text="Promedio")
        self.txt_promedio.grid(row=1, padx=20, pady=20)

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
#solicitar 5 números mediante prompt. 
        contador = 0
        suma = 0
        while contador <5:
            numero = int(prompt("EJ 06", "Ingrese un número"))
            suma += numero
            contador += 1
        promedio = suma / 5
        self.txt_promedio.delete(0, 100000000)
        self.txt_suma_acumulada.delete(0, 100000000)
        self.txt_suma_acumulada.insert(0, str(suma))
        self.txt_promedio.insert(0, str(promedio))



#Calcular la suma acumulada
#el promedio de los números ingresados. 
#informar los resultados en las cajas de texto txt_suma_acumulada y txt_promedio

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
