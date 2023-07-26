import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Al presionar el botón 'PROMEDIO' se analizará el vector lista_datos a efectos de calcular 
el promedio el cual deberá ser informado utilizando Dialog Alert.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_calcular = customtkinter.CTkButton(master=self, text="PROMEDIO", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.lista_datos = [1,80,5,0,15,-5,1,79]


    def btn_calcular_on_click(self):
        sumatoria = 0
        contador = 0
        for i in range(0, 8, 1):
            sumatoria += self.lista_datos[i]
            contador += 1
        promedio=sumatoria/contador
        promedio = str(promedio)
        alert("EJ 06", "El promedio es de "+str(promedio))
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()