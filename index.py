from tkinter import *
import math
import datetime

#dimensiones de la ventana
ventana = Tk()
ancho = 600
alto = 300
ventana.geometry(str(ancho)+'x'+str(alto))
ventana.title('Examen Final')

#titulo de la ventana
bienvenido = Label(text="Bienvenido",font=("Arial Narrow",25))
bienvenido.grid(row=1, column=1, columnspan=6)

#etiqueta para el nombre
nombre = Label(text="Nombre",font=("Arial Narrow",10))
nombre.grid(row=2, column=1, columnspan=2)
#caja de texto
Nom = Entry(ventana)
Nom.grid(row=2, column=3, columnspan=3, sticky= W + E)

#etiqueta para el apellido
apellido = Label(text="Apellido",font=("Arial Narrow", 10))
apellido.grid(row=3, column=1, columnspan=2)
#caja de texto
Ape = Entry(ventana)
Ape.grid(row=3, column=3, columnspan=3, sticky= W + E)

#etiqueta para el día
Dia = Label(text="Día",font=("Arial Narrow", 10))
Dia.grid(row=4, column=1, columnspan=2)
#caja de texto
Day = Entry(ventana)
Day.grid(row=4, column=3, columnspan=3, sticky= W + E)

#etiqueta para el mes
Mes = Label(text="Mes",font=("Arial Narrow", 10))
Mes.grid(row=5, column=1, columnspan=2)
#caja de texto
Month = Entry(ventana)
Month.grid(row=5, column=3, columnspan=3, sticky= W + E)

#etiqueta para el año
Año = Label(text="Año",font=("Arial Narrow", 10))
Año.grid(row=6, column=1, columnspan=2)
#caja de texto
Year = Entry(ventana)
Year.grid(row=6, column=3, columnspan=3, sticky= W + E)

#funciones:
#función que muestra la fecha ingresada en codigo binario 
def fechaabinario():
    dd=int(Day.get())
    mm=int(Month.get())
    y=int(Year.get())
    bdd=format(dd, '0b' )
    bmm=format(mm, '0b')
    by=format(y, '0b')

    Resultado['text'] = 'Su fecha es: {}/{}/{} y en binario es:{}/{}/{}'.format(dd,mm,y,bdd,bmm,by)

#función que muetra los días que ha vivido desde que nació hasta el día actual 
def diasvividos():
    da = int(Day.get())
    mse = int(Month.get())
    an = int(Year.get())
    nac = datetime.datetime(an, mse, da)
    fec = datetime.datetime.now()
    resto = fec - nac
    viv = resto.days
    Resultado['text'] = '{}/{}/{} y ha vivido {} dias'.format(da,mse,an,viv)

#función que muetra si el número de letras de su nombre y apellido es par o impar 
def paroimpar():
    Name = f"{Nom.get()}"
    SurName = f"{Ape.get()}"
    NumName = len(Name)
    NumSurName = len(SurName)

    if NumName % 2 == 0:
        NB = f"Su nombre {Name} es número par  "
    else:
        NB = f"Su nombre {Name} es número impar  "
    if NumSurName % 2 == 0:
        PLL = f"su apellido {SurName} es número par ."
    else:
        PLL = f"su apellido {SurName} es número Impar ."
    answer2 = f"{NB} y  {PLL} "

    Resultado.configure(text = answer2)

#función que mustra cuántas vocales y cuantas consonantes tiene su nombre y su apellido 
def vocalesyconsonantes():
        Namme=str(Nom.get())
        SurNamee=str(Ape.get())
        sumvoc = 0
        for vc in Namme:
            if vc == 'a' or vc =='A' or vc =='e' or vc =='E' or vc =='i' or vc =='I' or vc =='o' or vc =="O" or vc =="u" or vc=="U":
                sumvoc += 1
        for vc in SurNamee:
            if vc == 'a' or vc =='A' or vc =='e' or vc =='E' or vc =='i' or vc =='I' or vc =='o' or vc =="O" or vc =="u" or vc=="U":
                sumvoc += 1
        c1=len(Namme)
        c12=len(SurNamee)
        consta=c1+c12-sumvoc

        Resultado['text'] = 'Su nombre y apellido tiene: {} vocales y {} consonantes'.format(sumvoc,consta)
     

#función que muestre su nombre y apellido al revés 
def nombreyapellidoalreves():
    nareves = Nom.get()+" "+Ape.get()
    nareves = nareves[::-1]
    Resultado["text"] = Nom.get() + " " + Ape.get() + " al revés es: " + nareves

#botones de las funciones
Funcion1 = Button(ventana, text = "Función 1", command=fechaabinario, font=("Arial Narrow", 12), width=10)
Funcion1.grid(row=7, column=1)

Funcion2 = Button(ventana, text = "Función 2", command=diasvividos ,font=("Arial Narrow", 12), width=10)
Funcion2.grid(row=7, column=2)

Funcion3 = Button(ventana, text = "Función 3",command= paroimpar,font=("Arial Narrow", 12), width=10)
Funcion3.grid(row=7, column=3)

Funcion4 = Button(ventana, text = "Función 4", command=vocalesyconsonantes, font=("Arial Narrow", 12),width=10)
Funcion4.grid(row=7, column=4)

Funcion5 = Button(ventana, text = "Función 5",command=nombreyapellidoalreves,font=("Arial Narrow", 12), width=10)
Funcion5.grid(row=7, column=5)

#etiqueta que muestra el resultado
Resultado = Label(ventana, text="Aca se verá el resultado de las funciones", font=("Arial Narrow", 12))
Resultado.grid(row=8, column=1, columnspan=6)

ventana.mainloop()