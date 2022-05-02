from tkinter import *

root = Tk()
root.title("Calculadora")

miFrame = Frame(root)
miFrame.pack()

operacion = ""

reset_pantalla = False

resultado = 0

#-----------------------Pantalla--------------------------
numeroEnPantalla = StringVar()

pantalla = Entry(miFrame, textvariable = numeroEnPantalla)
pantalla.grid(row = 1, column = 1, padx = 10, pady = 10, columnspan = 4)
pantalla.config(bg = "black", fg = "#03f943", justify = "right")

#----------------------Pulsaciones teclado----------------------------
def numeroPulsado(num):
    global operacion
    global reset_pantalla

    if reset_pantalla != False:
        numeroEnPantalla.set(num)
        reset_pantalla = False
    else:
        numeroEnPantalla.set(numeroEnPantalla.get() + num)

#----------------------Funcion suma------------------------------------
def suma(num):
    global operacion
    global resultado
    global reset_pantalla

    resultado += int(num)
    operacion = "suma"
    reset_pantalla = True
    numeroEnPantalla.set(resultado)

#----------------------Funcion resta------------------------------------
num1 = 0
contador_resta = 0

def resta(num):
    global operacion
    global resultado
    global num1
    global contador_resta
    global reset_pantalla

    if contador_resta == 0:
        num1 = int(num)
        resultado = num1
    else:
        if contador_resta == 1:
            resultado = num1-int(num)
        else:
            resultado = int(resultado)-int(num)	

        numeroEnPantalla.set(resultado)
        resultado = numeroEnPantalla.get()
    
    contador_resta += 1
    operacion = "resta"
    reset_pantalla = True

#---------------------Funcion multiplicacion-----------------------------
contador_multi = 0

def multiplicar(num):
    global operacion
    global resultado
    global num1
    global contador_multi
    global reset_pantalla

    if contador_multi == 0:
        num1 = int(num)
        resultado = num1
    else:
        if contador_multi == 1:
            resultado = num1 * int(num)
        else:
            resultado = int(resultado) * int(num)

        numeroEnPantalla.set(resultado)
        resultado = numeroEnPantalla.get()

    contador_multi += 1
    operacion = "multiplicacion"
    reset_pantalla = True

#---------------------Funcion division-----------------------------------
contador_div = 0

def dividir(num):
    global operacion
    global resultado
    global num1
    global contador_div
    global reset_pantalla

    if contador_div == 0:
        num1 = float(num)
        resultado = num1
    else:
        if contador_div == 1:
            resultado = num1 / float(num)
        else:
            resultado = float(resultado) / float(num)
        
        numeroEnPantalla.set(resultado)
        resultado = numeroEnPantalla.get()

    contador_div += 1
    operacion = "division"
    reset_pantalla = True

#---------------------Funcion resultado_total---------------------------
def resultado_total():
    global resultado
    global operacion
    global contador_resta
    global contador_multi
    global contador_div

    if operacion == "suma":
        numeroEnPantalla.set(resultado + int(numeroEnPantalla.get()))
        resultado = 0
    
    elif operacion == "resta":
        numeroEnPantalla.set(int(resultado) - int(numeroEnPantalla.get()))
        resultado = 0
        contador_resta = 0

    elif operacion == "multiplicacion":
        numeroEnPantalla.set(int(resultado) * int(numeroEnPantalla.get()))
        resultado = 0
        contador_multi = 0

    elif operacion == "division":
        numeroEnPantalla.set(float(resultado) / float(numeroEnPantalla.get()))
        resultado = 0
        contador_div = 0

#----------------------Fila 1------------------------------------------
boton7 = Button(miFrame, text = "7", width = 3, command = lambda: numeroPulsado("7"))
boton7.grid(row = 2, column = 1)
boton8 = Button(miFrame, text = "8", width = 3, command = lambda: numeroPulsado("8"))
boton8.grid(row = 2, column = 2)
boton9 = Button(miFrame, text = "9", width = 3, command = lambda: numeroPulsado("9"))
boton9.grid(row = 2, column = 3)
botonDiv = Button(miFrame, text = "/", width = 3, command = lambda: dividir(numeroEnPantalla.get()))
botonDiv.grid(row = 2, column = 4)

#----------Fila 2-----------------
boton4 = Button(miFrame, text = "4", width = 3, command = lambda: numeroPulsado("4"))
boton4.grid(row = 3, column = 1)
boton5 = Button(miFrame, text = "5", width = 3, command = lambda: numeroPulsado("5"))
boton5.grid(row = 3, column = 2)
boton6 = Button(miFrame, text = "6", width = 3, command = lambda: numeroPulsado("6"))
boton6.grid(row = 3, column = 3)
botonMult = Button(miFrame, text = "x", width = 3, command = lambda: multiplicar(numeroEnPantalla.get()))
botonMult.grid(row = 3, column = 4)

#----------Fila 3-----------------
boton1 = Button(miFrame, text = "1", width = 3, command = lambda: numeroPulsado("1"))
boton1.grid(row = 4, column = 1)
boton2 = Button(miFrame, text = "2", width = 3, command = lambda: numeroPulsado("2"))
boton2.grid(row = 4, column = 2)
boton3 = Button(miFrame, text = "3", width = 3, command = lambda: numeroPulsado("3"))
boton3.grid(row = 4, column = 3)
botonRest = Button(miFrame, text = "-", width = 3, command = lambda: resta(numeroEnPantalla.get()))
botonRest.grid(row = 4, column = 4)

#----------Fila 4-----------------
botonComa = Button(miFrame, text = ",", width = 3, command = lambda: numeroPulsado(","))
botonComa.grid(row = 5, column = 1)
boton0 = Button(miFrame, text = "0", width = 3, command = lambda: numeroPulsado("0"))
boton0.grid(row = 5, column = 2)
botonIgual = Button(miFrame, text = "=", width = 3, command = lambda: resultado_total())
botonIgual.grid(row = 5, column = 3)
botonSuma = Button(miFrame, text = "+", width = 3, command = lambda: suma(numeroEnPantalla.get()))
botonSuma.grid(row = 5, column = 4)



root.mainloop()
