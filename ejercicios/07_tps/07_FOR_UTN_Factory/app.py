'''
UTN Software Factory está en la búsqueda de programadores para incorporar a su equipo de 
trabajo. En las próximas semanas se realizará un exhaustivo proceso de selección. Para ello se 
ingresarán los siguientes datos de los 10 postulantes para luego establecer distintas métricas 
necesarias para tomar decisiones a la hora de la selección:

Nombre
Edad (mayor de edad)
Género (F-M-NB)
Tecnología (PYTHON - JS - ASP.NET)
Puesto (Jr - Ssr - Sr)

Informar por pantalla:
a. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS 
cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.
b. Nombre del postulante Jr con menor edad.
c. Promedio de edades por género.
d. Tecnologia con mas postulantes (solo hay una).
e. Porcentaje de postulantes de cada genero.

Todos los datos se ingresan por prompt y los resultados se muestran por consola (print)

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
        cantidad_a = 0
        minima_edad = 99999999999
        minima_edad_mensaje = "No hubo postulantes para el puesto Jr"
        contador_M = 0
        sumatoria_edades_M = 0
        contador_H = 0
        sumatoria_edades_H = 0
        contador_NB = 0
        sumatoria_edades_NB = 0
        contador_PY = 0
        contador_JS = 0
        contador_ASP = 0
    #10 postulantes
        for i in range(0,10,1):
    #Nombre
            nombre = prompt("Nombre", "Ingrese nombre del postulante")
    #Edad (mayor de edad)
            while True:
                edad = prompt ("Edad","Ingrese la edad mayor a 0 con caracteres numéricos")
                if edad.isdigit() == True:
                    edad_int = int(edad)
                    if edad_int >= 0:
                        break
    #Género (F-M-NB)
            while True:
                genero = prompt("Genero", "Ingrese su género, ¨F¨ para femenino, ¨M¨ para masculino o ¨NB¨ para no binario")
                if genero == "F" or genero == "M" or genero == "NB":
                    break
    #Tecnología (PYTHON - JS - ASP.NET)
            while True:
                tecnologia = prompt("Tecnología", "Ingrese la tecnología en la que se especializa entre ¨PYTHON¨, ¨JS¨ o ¨ASP.NET¨")
                if tecnologia == "PYTHON" or tecnologia == "JS" or tecnologia == "ASP.NET":
                    break
    #Puesto (Jr - Ssr - Sr)
            while True:
                puesto = prompt("Puesto", "Ingrese el puesto querido entre ¨Jr¨, ¨Ssr¨ o ¨Sr¨")
                if puesto == "Jr" or puesto == "Ssr" or puesto == "Sr":
                    break
    #Informar por pantalla:
    #a. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS 
    #   cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.
            if genero == "NB" and (tecnologia == "ASP.NET" or tecnologia == "JS") and edad_int <= 40 and edad_int >= 25:
                cantidad_a += 1
    #b. Nombre del postulante Jr con menor edad.
            if edad_int <  minima_edad and puesto == "Jr":
                minima_edad = edad_int
                minima_edad_mensaje = nombre +" es el postulante a Jr con menor edad"
    #c. Promedio de edades por género.
            if genero == "M":
                contador_M += 1
                sumatoria_edades_M += edad_int
            elif genero == "H":
                contador_H += 1
                sumatoria_edades_H += edad_int
            else:
                contador_NB += 1
                sumatoria_edades_NB += edad_int
    #d. Tecnologia con mas postulantes (solo hay una).
            if tecnologia == "PYTHON":
                contador_PY+=1
            elif tecnologia == "JS":
                contador_JS+=1
            else:
                contador_ASP+=1
    #e. Porcentaje de postulantes de cada genero.
    #Todos los datos se ingresan por prompt y los resultados se muestran por consola (print)
        if contador_M != 0:
            promedio_M=sumatoria_edades_M/contador_M
        else:
            promedio_M = 0
        if contador_H != 0:
            promedio_H=sumatoria_edades_H/contador_H
        else:
            promedio_H = 0
        if contador_NB != 0:
            promedio_NB=sumatoria_edades_NB/contador_NB
        else:
            promedio_NB = 0
        mensaje_promedios="El promedio de edades de mujeres fue de "+str(promedio_M)+" años, el de hombres fue de "+str(promedio_H)+" años, y el de no binarios fue de " + str(promedio_NB)+ " años"
        if contador_PY >= contador_JS:
            if contador_PY >= contador_ASP:
                tecnologia_popular = "PYTHON"
        elif contador_JS >= contador_ASP:
            tecnologia_popular = "JS"
        else:
            tecnologia_popular = "ASP.NET"
        #el porcentaje de x sabiendo q son 10 en total es el (contador/10)*100 lo cual es igual a contador* 10
        porcentaje_M = contador_M*10
        porcentaje_H = contador_H*10
        porcentaje_NB = contador_NB*10
        mensaje_porcentajes = "El porcentaje de mujeres postuladas fue de " + str(porcentaje_M) + "%, el de hombres fue de " + str(porcentaje_H) + "%, y el de no binarios fue de "+ str(porcentaje_NB)+ "%"
        print("Hay "+ str(cantidad_a)+ " postulantes no binarios que programan en ASP.NET o JS cuya edad este entre 25 y 40 postulados para Ssr")
        print(minima_edad_mensaje)
        print(mensaje_promedios)
        print("La tecnología con mas postulantes es "+tecnologia_popular)
        print(mensaje_porcentajes)




if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
