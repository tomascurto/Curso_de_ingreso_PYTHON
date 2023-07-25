'''
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por consola (print)

Nombre: Tomás León 
Apellido: Curto Eivers

'''
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
#De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
#nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
        nombre = 0
        edad_int = 0
        candidato_maximo = nombre
        candidato_minimo = nombre
        votos_maximos = -1
        votos_minimos = 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        edad_menos_votos = edad_int
        suma_edades = edad_int
        cantidad_de_candidatos = 1
        total_de_votos = 0
        promedio = 0
        while True:
            nombre = prompt("Nombre", "Escriba un nombre o presione Cancelar para efectuar los calculos")
            if nombre == None:
                break
            edad = prompt("Edad", "Ingrese edad")
            if edad.isdigit() == True:
                edad_int = int(edad)
            else:
                edad_int=0
            while edad_int < 25:
                edad = prompt ("Edad", "La edad debe ser un caracter numérico y mayor de 25")
                if edad.isdigit() == True:
                    edad_int = int(edad)
                else:
                    edad_int=0
            votos = prompt("Votos", "Ingrese cantidad de votos")
            if votos.isdigit() == True:
                votos_int = int(votos)
            else:
                votos_int= -1
            while votos_int < 0:
                votos = prompt ("Votos", "La cantidad de votos debe ser un caracter numérico y mayor a 0")
                if votos.isdigit() == True:
                    votos_int = int(votos)
                else:
                    votos_int= -1
            if votos_int > votos_maximos:
                candidato_maximo = nombre
                votos_maximos = votos_int
            elif votos_int < votos_minimos:
                candidato_minimo = nombre
                votos_minimos = votos_int
                edad_menos_votos = edad_int
            suma_edades += edad_int
            cantidad_de_candidatos += 1
            total_de_votos += votos_int            
#Informar: 
#a. nombre del candidato con más votos
        print("El candidato con más votos es " + candidato_maximo)
#b. nombre y edad del candidato con menos votos
        print("El candidato con menos votos es " + candidato_minimo)
        print("La edad del candidato con menos votos es de " + str(edad_menos_votos) + " años")
#c. el promedio de edades de los candidatos
        promedio = suma_edades / cantidad_de_candidatos
        print("El promedio de edades de candidatos es de " + str(promedio) + " años")
#d. total de votos emitidos.
        print("El total de votos emitidos es de " + str(total_de_votos))
#Todos los datos se ingresan por prompt y los resultados por consola (print)

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
