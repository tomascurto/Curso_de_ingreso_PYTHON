import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el
usuario quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    a. La suma acumulada de los negativos
    b. La suma acumulada de los positivos
    c. Cantidad de números positivos ingresados
    d. Cantidad de números negativos ingresados
    e. Cantidad de ceros
    f. El minimo de los negativos
    g. El maximo de los positivos
    h. El promedio de los negativos

Informar los resultados mediante alert()

'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_cargar = customtkinter.CTkButton(
            master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_cargar.grid(row=2, padx=20, pady=20,
                             columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar Estadísticas", command=self.btn_mostrar_estadisticas_on_click)
        self.btn_mostrar.grid(row=3, padx=20, pady=20,
                              columnspan=2, sticky="nsew")

        self.lista = []

    def btn_comenzar_ingreso_on_click(self):
        #Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el
        #usuario quiera hasta que presione el botón Cancelar (en el prompt). 
        while True:
            numero = prompt("Número", "Ingrese un número o presione ¨Cancelar¨ para guardar los datos ingresados.")
            if numero == None:
                break
            numero = int(numero)
            self.lista.append(numero)


    def btn_mostrar_estadisticas_on_click(self):
        acumulador_negativo = 0
        acumulador_positivo = 0
        contador_positivo = 0
        contador_negativo = 0
        contador_ceros = 0
        minimo = self.lista[0]
        maximo = self.lista[0]
        for i in range(0, len(self.lista), 1):
        #a. La suma acumulada de los negativos
        #b. La suma acumulada de los positivos
        #c. Cantidad de números positivos ingresados
        #d. Cantidad de números negativos ingresados
        #e. Cantidad de ceros
        #f. El minimo de los negativos
        #g. El maximo de los positivos
        #h. El promedio de los negativos
            if self.lista[i] < 0:
                acumulador_negativo += self.lista[i]
                contador_negativo += 1
            elif self.lista[i] > 0:
                acumulador_positivo += self.lista[i]
                contador_positivo +=1
            else:
                contador_ceros += 1
            if self.lista[i] < minimo:
                minimo = self.lista[i]
            elif self.lista[i] > maximo:
                maximo = self.lista[i]
        promedio = acumulador_negativo / contador_negativo
        acumulador_negativo = "La suma acumulada de negativos es " + str(acumulador_negativo)
        acumulador_positivo = ". La suma acumulada de los positivos es "+ str(acumulador_positivo)
        contador_positivo = ". La cantidad de números positivos ingresados es " + str(contador_positivo)
        contador_negativo = ". La cantidad de números negativos ingresados es " + str(contador_negativo)
        contador_ceros = ". La cantidad de ceros ingresados es " + str(contador_ceros)
        minimo = ". El minimo es " + str(minimo)
        maximo = ". El maximo es " + str(maximo)
        promedio = ". El promedio de los negativos es " + str(promedio) +"."
        alert("Estadisticas", acumulador_negativo+acumulador_positivo+contador_positivo+contador_negativo+contador_ceros+minimo+maximo+promedio)



if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
