import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    La suma acumulada de los negativos
    La suma acumulada de los positivos
    Cantidad de números positivos ingresados
    Cantidad de números negativos ingresados
    Cantidad de ceros
    Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

nombre: Tomas Leon
apellido: Curto Eivers

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
    #La suma acumulada de los negativos
    #La suma acumulada de los positivos
    #Cantidad de números positivos ingresados
    #Cantidad de números negativos ingresados
    #Cantidad de ceros
    #Diferencia entre la cantidad de los números positivos ingresados y los negativos        
        acumulador_positivos = 0
        acumulador_negativos = 0
        contador_positivos = 0
        contador_negativos = 0
        contador_ceros = 0
        numero = int(prompt("EJ 10", "Ingrese un número"))
        while numero != None:
            if numero > 0:
                contador_positivos += 1
                acumulador_positivos += numero
            elif numero == 0:
                contador_ceros += 1
            else:
                contador_negativos += 1
                acumulador_negativos += numero          
            numero = prompt("EJ 10", "Ingrese otro número o ejecute los calculos presionando ¨cancelar¨")
            if numero != None:
                numero = int(numero)
        if contador_positivos > contador_negativos:
            diferencia = contador_positivos - contador_negativos
            diferencia_mensaje = ". Se ingresaron " + str(diferencia) + " numeros positivos mas de lo que se ingresaron negativos"
        if contador_negativos == contador_positivos:
            diferencia_mensaje = ". Se ingresaron la misma cantidad de números negativos que positivos"
        else:
            diferencia = contador_negativos - contador_positivos 
            diferencia_mensaje = ". Se ingresaron " + str(diferencia) + " numeros negativos mas de lo que se ingresaron positivos"
        alert("EJ 10", "La suma acumulada de los números negativos ingresados es " + str(acumulador_negativos) + ". La suma acumulada de los números positivos ingresados es " + str(acumulador_positivos) + ". La cantidad de números negativos ingresados es de " + str(contador_negativos) + ". La cantidad de números positivos ingresados es de " + str(contador_positivos) + ". La cantidad de ceros ingresados es de " + str(contador_ceros) + diferencia_mensaje)

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
