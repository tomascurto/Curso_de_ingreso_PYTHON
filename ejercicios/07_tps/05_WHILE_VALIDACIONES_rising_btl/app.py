import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Rising BTL. Empresa dedicada a la toma de datos para realizar estadísticas y censos nos pide realizar una carga de datos validada e ingresada 
por ventanas emergentes solamente (para evitar hacking y cargas maliciosas) y luego asignarla a cuadros de textos. 

Los datos requeridos son los siguientes:
    Apellido
    Edad, entre 18 y 90 años inclusive.
    Estado civil, ["Soltero/a", "Casado/a", "Divorciado/a", "Viudo/a"]
    Número de legajo, numérico de 4 cifras, sin ceros a la izquierda.

    Apellido: Curto Eivers,
    Nombre: Tomás León
'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.label0 = customtkinter.CTkLabel(master=self, text="Apellido")
        self.label0.grid(row=0, column=0, padx=20, pady=10)
        self.txt_apellido = customtkinter.CTkEntry(master=self)
        self.txt_apellido.grid(row=0, column=1)

        self.label1 = customtkinter.CTkLabel(master=self, text="Edad")
        self.label1.grid(row=1, column=0, padx=20, pady=10)
        self.txt_edad = customtkinter.CTkEntry(master=self)
        self.txt_edad.grid(row=1, column=1)

        self.label2 = customtkinter.CTkLabel(master=self, text="Estado")
        self.label2.grid(row=2, column=0, padx=20, pady=10)
        self.combobox_tipo = customtkinter.CTkComboBox(
            master=self, values=["Soltero/a", "Casado/a", "Divorciado/a", "Viudo/a"])
        self.combobox_tipo.grid(row=2, column=1, padx=20, pady=10)

        self.label3 = customtkinter.CTkLabel(master=self, text="Legajo")
        self.label3.grid(row=3, column=0, padx=20, pady=10)
        self.txt_legajo = customtkinter.CTkEntry(master=self)
        self.txt_legajo.grid(row=3, column=1)

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        #ventanas emergentes solamente
        #Apellido
        apellido = prompt("Apellido", "Ingrese apellido")
        while apellido.isalpha() == False:
            apellido = prompt("Apellido", "Apellido solo acepta caracteres alfabéticos, intentelo de nuevo")
        #Edad, entre 18 y 90 años inclusive.
        edad = prompt("Edad", "Ingrese edad")
        if edad.isdigit() == True:
            edad_int = int(edad)
        else:
            edad_int=0
        while edad_int < 18 or edad_int > 90:
            edad = prompt ("Edad", "La edad debe ser un caracter numérico entre 18 y 90")
            if edad.isdigit() == True:
                edad_int = int(edad)
            else:
                edad_int=0 #use 0 debido a que siempre va a ser menor que 18, y elimina la posibilidad de error al comparar 18 y 90 con cualquier entrada que no se
        #Estado civil, ["Soltero/a", "Casado/a", "Divorciado/a", "Viudo/a"]
        estado_civil = prompt("Legajo", "Ingrese estado civil")
        while estado_civil != "Soltero/a" and estado_civil != "Casado/a" and estado_civil != "Divorciado/a" and estado_civil != "Viudo/a":
            estado_civil = prompt("Estado civil", "La respuesta debe ser escrita de la siguiente manera y entre estas opciones: ¨Soltero/a¨, ¨Casado/a¨, ¨Divorciado/a¨, ¨Viudo/a¨")
        #Número de legajo, numérico de 4 cifras, sin ceros a la izquierda.
        legajo = prompt("Legajo", "Ingrese el legajo")
        if legajo.isdigit() == True:
            legajo_int = int(legajo)
        else:
            legajo_int = 10000 # cuando compare 10000 siempre va a tener más de 4 digitos y no lo va a aceptar
        while len(legajo) != 4 or legajo.isdigit() == False :
            legajo = prompt("Legajo", "el legajo debe ser un caracter numérico de 4 digitos sin ceros a la izquierda")
        #asignarla a cuadros de textos
        self.txt_apellido.delete(0, 10000000)
        self.txt_apellido.insert(0, apellido)
        self.txt_edad.delete(0, 10000000)
        self.txt_edad.insert(0, edad)
        self.combobox_tipo.set(estado_civil)
        self.txt_legajo.delete(0, 10000000)
        self.txt_legajo.insert(0, legajo)

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
