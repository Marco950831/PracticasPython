
import tkinter as tk
from tkinter import *
from tkinter import ttk

def getValue():
    print(panels.get())

def value1():
    value1 = panels.get()
    return var1.set(value1)



def linealOperations():
    value2 = panels.get()
    calculo1 = int(value2)-1
    calculo2= int(calculo1*2)
    return var2.set(calculo2)

def linealOperations():
    clemfin = 4
    return var3.set(clemfin)
    
def linealSWin():
    linealSystemWin = Toplevel(root)
    linealSystemWin.title("Sitema lineal")
    linealSystemWin.geometry("750x300")
    lbLineal = Label(linealSystemWin, text="Número de paneles:")
    lbLineal.grid(row=1, column=0, padx=10, pady=10)
    lbLineal2 = Label(linealSystemWin, text="Lista de Materiales:")
    lbLineal2.grid(row=2, column=0, padx=10, pady=10)
    lbLineal3=Label(linealSystemWin, text= "Numero de clemas finales:")
    lbLineal3.grid(row=3, column=0, padx=10, pady=10)
  
        
    ##Creating TextBox for Input Data
    ## DeployedList = Entry(linealSystemWin)
    ##DeployedList.grid(row=1, column=1, padx=10, pady=10)
    panelsOut = Label(linealSystemWin,bg="#FDFEFE",textvariable=var1,padx=3,pady=3,width=10)
    panelsOut.grid(row=1, column=1)
    ListOut = Label(linealSystemWin, bg="#FDFEFE", textvariable=var2, padx=3, pady=3, width=10)
    ListOut.grid(row=2, column=1)
    ClemasOut = Label(linealSystemWin, bg="#FDFEFE", textvariable=var3, padx=3, pady=3, width=10)
    ClemasOut.grid(row=3, column=1)
      ##Creating List
    my_Materials=["Clemas medias:","Clemas finales:", "Perfiles:","Climbers:", "TitlUP:", "L-Foot:"]
    txt_output= Text(root, height=5, width=30)
    txt_output.pack(pady=30)
    for item in my_Materials:
        txt_output.insert(END, item + "\n")
    linealSystemWin.mainloop()

def squareSWin():
    squareSystemWin = Toplevel(root)
    squareSystemWin.title("Sistema Cuadrático")
    squareSystemWin.geometry("300x300")
    ##Creatiing labels
    lbsquare = Label(squareSystemWin, text="Lista de Materiales:")
    lbsquare.grid(row=1, column=0, padx=10, pady=10)

    ##Creating TextBox for Input Data
    DeployedList = Entry(squareSystemWin)
    DeployedList.grid(row=1, column=1, padx=10, pady=10)
    squareSystemWin.mainloop()

def exitWindow():
    root.destroy()

    ##Creating label for #Panels

root = Tk()
root.geometry("400x300")
root.title("Calculadora de Materiales Solares")


labelP = Label(root, text="Número de Paneles:")
labelP.grid(row=1, column=0, padx=10, pady=10)


##Creatng Variables to make calculates
var1 = tk.StringVar(root)
var2 = tk.IntVar(root)
var3= tk.IntVar(root)


    


##Creating TextBox for Input Data
panels = Entry(root)
panels.grid(row=1, column=1, padx=10, pady=10)

##Creating Buttons To deploy a new Window
linealSButton = Button(root, text="Sistema Lineal", command=lambda:[getValue(),linealOperations(),value1(),linealSWin()])
linealSButton.grid(row=2, column=0, pady=10)

squareArrayButton = Button(root, text="Sistema Cuadrático", command=squareSWin)
squareArrayButton.grid(row=2, column=1, pady=10)

quitButton = Button(root, text="Salir", command=exitWindow)
quitButton.grid(row=2, column=2, pady=10)

root.mainloop()
