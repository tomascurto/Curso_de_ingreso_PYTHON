import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
Enunciado:
Al presionar el botón ‘Pedir clave’, solicitar al usuario que ingrese una contraseña mediante prompt. 
Comprobar que la contraseña ingresada sea ‘utn750’. En caso de no coincidir, volverla a solicitar hasta que coincidan

nombre: Tomas Leon
apellido: Curto Eivers
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_pedir_clave = customtkinter.CTkButton(master=self, text="Ingresar", command=self.btn_pedir_clave_on_click)
        self.btn_pedir_clave.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_pedir_clave_on_click(self):
        clave = prompt("EJ 03", "Ingrse la clave")
        while clave != "utn750":
            alert ("EJ 03", "Intente nuevamente")
            clave = prompt("EJ 03", "Ingrse la clave")
        alert ("EJ 03", "Clave ingresada correctamente")
    
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()