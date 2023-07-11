import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
Enunciado:
Al presionar el botón ‘Informar’ mostrar mediante alert los siguientes mensajes 
en función del mes seleccionado:
    Si estamos en invierno: ‘¡Abrígate que hace frío!’
    Si aún no llegó el invierno: ‘Falta para el invierno..’
    Si ya pasó el invierno: ‘¡Ya pasamos frío, ahora calor!’
	
Aclaracion: tomamos a Julio y Agosto como los meses de invierno

nombre: Tomas Leon
apellido: Curto Eivers

'''
# Enero, Febrero, Marzo, Abril, Mayo, Junio - ¡Falta para el invierno..!
# Julio, Agosto - ¡Abrígate que hace frío!
# Septiembre, Octubre, Noviembre, Diciembre - ¡Ya pasamos frío, ahora calor!


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.label_meses = customtkinter.CTkLabel(master=self, text="Meses")
        self.label_meses.grid(row=0, column=0, padx=20, pady=10)
        meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
        self.combobox_mes = customtkinter.CTkComboBox(master=self, values=meses)
        self.combobox_mes.grid(row=1, column=0, padx=20, pady=(10, 10))
        
        self.btn_informar = customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_informar_on_click(self):
        # Enero, Febrero, Marzo, Abril, Mayo, Junio - ¡Falta para el invierno..!
        # Julio, Agosto - ¡Abrígate que hace frío!
        # Septiembre, Octubre, Noviembre, Diciembre - ¡Ya pasamos frío, ahora calor!
        mes = self.combobox_mes.get()
        if mes == "Julio" or mes == "Agosto":
            mensaje = "¡Abrígate que hace frío!"
        elif mes == "Septiembre" or mes == "Octubre" or mes == "Noviembre" or mes == "Diciembre":
            mensaje = "¡Ya pasamos frío, ahora calor!"
        else:
            mensaje = "¡Falta para el invierno..!"
        alert ("EJ 02", mensaje)
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()