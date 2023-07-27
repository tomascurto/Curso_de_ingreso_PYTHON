import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
A) El profesor OAK de pueblo paleta quiere que construyas un modelo prototipico de pokedex con 
 algunos pokemones de prueba.

Para ello deberas programar el boton "Cargar Pokedex" para poder cargar 10 pokemones.
Los datos que deberas pedir para los pokemones son:
    * El nombre del pokemon
    * El tipo de su elemento (Agua, Tierra, Psiquico, Fuego, Electrico)
    * La cantidad de poder (validar que sea mayor a 50 y menor a 200)
    
-- SOLO SE CARGARAN LOS VALORES SI Y SOLO SI SON CORRECTOS --

B) Al presionar el boton mostrar, se debera mostrar el pokemon (nombre, tipo y poder) de tipo fuego o agua con mas poder

Para determinar que informe hacer, tenga en cuenta lo siguiente:
    
    1- Tome el ultimo numero de su DNI Personal (Ej 4) y realiza ese informe (Ej, Realizar informe 4)

    2- Tome el ultimo numero de su DNI Personal (Ej 4), y restarselo al numero 9 (Ej 9-4 = 5). 
    Realiza el informe correspondiente al numero obtenido.
    
EL RESTO DE LOS INFORMES LOS PUEDE IGNORAR. 

*******Tener en cuenta que pueden no haber ingresos o egresos**********
C) Al presionar el boton Informar 
    # 0) - Cantidad de pokemones de tipo Fuego
    # 1) - Cantidad de pokemones de tipo Electrico
    # 2) - Nombre, tipo y Poder del pokemon con el poder mas alto
    # 3) - Nombre, tipo y Poder del pokemon con el poder mas bajo
    # 4) - Cantidad de pokemones, con mas de 100 de poder.
    # 5) - Cantidad de pokemones, con menos de 100 de poder
    # 6) - tipo de los pokemones del tipo que mas pokemones posea 
    # 7) - tipo de los pokemones del tipo que menos pokemones posea 
    # 8) - el promedio de poder de todos los ingresados
    # 9) - el promedio de poder de todos los poquemones de Electrico 

Nombre: Tomás León
Apellido: Curto Eivers
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("Simulacro Parcial")

        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar Pokedex", command=self.btn_cargar_on_click)
        self.btn_cargar.grid(row=3, padx=20, pady=20, columnspan=2, sticky="nsew")
       
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=4, padx=20, pady=20, columnspan=2, sticky="nsew")

        self.btn_informar= customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=5, padx=20, pady=20, columnspan=2, sticky="nsew")        

        self.lista_nombre = []
        self.lista_tipo = []
        self.lista_poder = []




    def btn_cargar_on_click(self):
        self.lista_nombre.clear()
        self.lista_tipo.clear()
        self.lista_poder.clear()
        #cargar 10 pokemones
        for i in range(0,10,1):
            #nombre del pokemon
            nombre = prompt("Nombre", "Ingrese el nombre del Pokemon.") 
            while nombre == None or nombre.isalpha() != True:
                nombre = prompt("Nombre", "Ingrese el nombre del Pokemon, solo se aceptan caracteres alfabéticos.")
            #El tipo de su elemento (Agua, Tierra, Psiquico, Fuego, Electrico)
            tipo = prompt("Tipo", "Ingrese el tipo de Pokemon dentro de las siguientes opciones: Agua, Tierra, Psiquico, Fuego, Electrico.")
            while tipo == None or tipo.isalpha() != True or (tipo != "Agua" and tipo != "Tierra" and tipo != "Psiquico" and tipo != "Fuego" and tipo != "Electrico"):
                alert("Error", "Se debe ingresar una de las opciones dadas en caracteres alfabéticos y solo la primer letra en mayusculas.")
                tipo = prompt("Tipo", "Ingrese el tipo de pokemon dentro de las siguientes opciones: Agua, Tierra, Psiquico, Fuego, Electrico.")
            #La cantidad de poder (validar que sea mayor a 50 y menor a 200)
            poder = prompt("Poder", "Ingrese con caracteres numéricos el poder del Pokemon (Debe ser un número entre 50 y 200).")
            while poder == None or poder.isdigit() != True or int(poder) < 50 or int(poder) > 200:
                alert("Error", "Debe ingresarse con caracteres numéricos entre 50 y 200.")
                poder = prompt("Poder", "Ingrese con caracteres numéricos el poder del Pokemon (Debe ser un número entre 50 y 200).")
            poder = int(poder)
            #Carga a listas:
            self.lista_nombre.append(nombre)
            self.lista_tipo.append(tipo)
            self.lista_poder.append(poder)

    def btn_mostrar_on_click(self):
        #B mostrar el pokemon (nombre, tipo y poder) de tipo fuego o agua con mas poder
        poder_maximo_fuego_agua = 0 #establecí cero ya que si se ingresa el primer pokemon de tipo fuego o ague su poder será si o si mayor a 50 superando esta variable
        for i in range(0,10,1):
            if self.lista_tipo[i] == "Agua" or self.lista_tipo[i] == "Fuego":
                if poder_maximo_fuego_agua < self.lista_poder[i]:
                    poder_maximo_fuego_agua = self.lista_poder[i]
                    numero_pokemon_maximo_fuego_agua =  i
        if poder_maximo_fuego_agua == 0:
            mensaje_maximo_fuego_agua = "No se ingreso ningun Pokemon de tipo Fuego o Agua."
        else:
            mensaje_maximo_fuego_agua = self.lista_nombre[numero_pokemon_maximo_fuego_agua] + " es el Pokemon tipo " + self.lista_tipo[numero_pokemon_maximo_fuego_agua] + " con mas poder entre todos los tipo Agua y Fuego cargados, con un poder de " + str(self.lista_poder[numero_pokemon_maximo_fuego_agua]) + "."
        alert("Máximo entre Fuego y Agua", mensaje_maximo_fuego_agua)


    def btn_informar_on_click(self):
        #C Nro DNI termina en 3
        # 3) - Nombre, tipo y Poder del pokemon con el poder mas bajo
        poder_minimo = 500
        for i in range(0,10,1):
            if poder_minimo > self.lista_poder[i]:
                poder_minimo = self.lista_poder[i]
                numero_pokemon_poder_minimo = i
        # 6) - tipo de los pokemones del tipo que mas pokemones posea
        self.lista_contadores_de_tipos = [0, 0, 0, 0, 0]
        for i in range(0,10,1):
            match self.lista_tipo[i]:
                case "Agua": 
                    self.lista_contadores_de_tipos[0] += 1
                case "Tierra":
                    self.lista_contadores_de_tipos[1] += 1
                case "Psiquico":
                    self.lista_contadores_de_tipos[2] += 1
                case "Fuego":
                    self.lista_contadores_de_tipos[3] += 1
                case _:
                    self.lista_contadores_de_tipos[4] += 1
        cantidad_maximo_tipo = 0
        for i in range(0,5,1):
            if cantidad_maximo_tipo < self.lista_contadores_de_tipos[i]:
                cantidad_maximo_tipo =  self.lista_contadores_de_tipos[i]
                indice_maximo_tipo = i
        match indice_maximo_tipo:
            case 0:
                mensaje_maximo_tipo = " El tipo con mayor cantidad de Pokemones ingresado es Agua."
            case 1:
                mensaje_maximo_tipo = " El tipo con mayor cantidad de Pokemones ingresado es Tierra."
            case 2:
                mensaje_maximo_tipo = " El tipo con mayor cantidad de Pokemones ingresado es Psiquico."
            case 3:
                mensaje_maximo_tipo = " El tipo con mayor cantidad de Pokemones ingresado es Fuego."
            case _:
                mensaje_maximo_tipo = " El tipo con mayor cantidad de Pokemones ingresado es Electrico."
        mensaje = "El Pokemon con el poder mas bajo es " + self.lista_nombre[numero_pokemon_poder_minimo] + " de tipo " + self.lista_tipo[numero_pokemon_poder_minimo] + " con un poder de " + str(self.lista_poder[numero_pokemon_poder_minimo]) + "." + mensaje_maximo_tipo
        # alertas
        alert("Resultado", mensaje)
        




if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
