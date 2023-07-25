import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Al presionar el botón Mostrar pedir valores por prompt hasta que el usuario ingrese el valor 9 (se deberá utilizar 'BREAK').

Nombre: Tomás León 
Apellido: Curto Eivers
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        for i in range (0,99999,1):
            numero = prompt("EJ 04", "Ingrese un número")
            if numero.isdigit() != True:
                numero = 0
            if int(numero) == 9:
                break
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()