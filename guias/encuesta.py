import tkinter as tk
##------------------raiz ------------------
raiz = tk.Tk()
raiz.title("Cuestionario")
#raiz.geometry("350x400")
## ------------------labels------------------
nombre = tk.Label(raiz, text = "Nombre:")
edad = tk.Label(raiz, text = "Edad:")
ocupacion = tk.Label(raiz, text = "Ocupacion:")
proyecto = tk.Label(raiz, text = "Proyecto:")
genero = tk.Label(raiz, text = "Genero:")
## ------------------Hubicacion labels------------------
nombre.grid(row = 0, column = 0, sticky= "nw", pady = 5) # El argumento stycky identa segun los puntos cardinales (N,S,E,W,NW,SW...)
edad.grid(row = 1, column = 0, sticky= "nw", pady = 5) # pady y padx separan los labels o textos con respecto a pixeles
ocupacion.grid(row = 2, column = 0, sticky= "nw", pady = 5)
genero.grid(row = 6, column = 0, sticky = "nw", pady = 5)
proyecto.grid(row = 8, column = 0, sticky= "nw", pady = 5)
## ------------------Denominacion de entradas------------------
n = tk.StringVar() # Denominamos que lo que se va a ingresar es una cadena de caracteres
e = tk.StringVar()
o = tk.IntVar()
o2 = tk.IntVar()
o3 = tk.IntVar()
o4 = tk.IntVar()
mas = tk.IntVar()
## ------------------Cuadros de texto------------------------
name = tk.Entry(raiz, textvariable = n) # Introducimos a la variable de texto en el Entry
age = tk.Entry(raiz, textvariable = e)
ocupation = tk.Checkbutton(raiz, text = "Estudiante", variable = o)
ocupation2 = tk.Checkbutton(raiz, text = "Profesor", variable = o2,)
ocupation3 = tk.Checkbutton(raiz, text = "Trabajador", variable = o3)
ocupation4 = tk.Checkbutton(raiz, text = "Ninguna", variable = o4)
proyect = tk.Text(raiz, width=20, height=3, ) # Como conseguir el texto ingresado en un Text
scroll = tk.Scrollbar(raiz, command=proyect.yview) # Se crea el scrollbar, se integra al texto y con yview se hubica para moverse de arriba a abajo
## ------------------Hubicacion cuadros de texto------------------
name.grid(row = 0, column = 1, pady = 5)
age.grid(row = 1, column = 1, pady = 5)
ocupation.grid(row = 2, column = 1, pady = 5, sticky = "nw")
ocupation2.grid(row = 3, column = 1, pady = 5, sticky = "nw")
ocupation3.grid(row = 4, column = 1, pady = 5, sticky = "nw")
ocupation4.grid(row = 5, column = 1, pady = 5, sticky = "nw")
proyect.grid(row = 8, column = 1, pady = 5)
scroll.grid(row = 8, column = 2, sticky="nsew") # Hubica el scroll
proyect.config(yscrollcommand = scroll.set) # Se adapta el scroll a la posicion del texto
## ------------------ Comandos para el boton ------------------
def imprimir(): # Definimos la funcion que imprime el contenido de el Entry
    print("Nombre: ", n.get()) # usamos el get() para "obtener" la variable de texto
    print("Edad: ", e.get())
    oc = "Ocupacion/es: "
    l = []
    if o.get() == 1:
        l += ["Estudiante"]
    if o2.get() == 1:
        l += ["Profesor"]
    if o3.get() == 1:
        l += ["Trabajador"]
    if o4.get() == 1:
        l += ["Ninguna"]
    if "Ninguna" in l:
        print(oc + "Ninguna.")
    else:
        if len(l) != 1:
            oc += ", ".join(e for e in l[:len(l)-1])
            oc += " y " + l[len(l) - 1] + "."
        else:
            oc += l[0] + "."
        print(oc)
    choise = ""
    if mas.get() == 1:
        choise += "Masculino"
    else:
        choise += "Femenino"
    print("Genero: ", choise)
    print("Proyecto: ", proyect.get("1.0" , "end"))


## -----------------------Boton------------------------------------
envio = tk.Button(raiz, text = "Imprimir", command = imprimir)
envio.grid(row = 9, column = 1)
## --------------------- Radiobuttons --------------------------
tk.Radiobutton(raiz, text = "Masculino", variable = mas, value = 1).grid(row = 6, column = 1, sticky = "nw")
# Los radiobuttons sirven para crear opciones de  respuesta unica
# Para ello necesitamos que las variables de cada uno de los radiobuttons sea la misma
tk.Radiobutton(raiz, text = "Femenino", variable = mas, value = 2).grid(row = 7, column = 1, sticky = "nw")

raiz.mainloop()
