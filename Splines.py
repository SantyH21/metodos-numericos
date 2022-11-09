#---Spline Interpolation---

import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate

pointsX = []
pointsY = []
valuesX = []
valuesY = []


root = tk.Tk()
root.geometry('600x200')
root.title("Spline Interpolation")
root.resizable(False, False)

# -----------------------------

tk.Label(root, text="Metodos númericos", font=("Italic", 25)).grid(row=4, column=0, padx=5, pady=5)

tk.Label(root, text="Cantidad de puntos:", font=("Italic", 15)).grid(row=5, column=0, padx=0, pady=5)

NumeroDePuntosEntrada = tk.Entry(root, font=("Italic", 15))
NumeroDePuntosEntrada.grid(row=5, column=1, padx=5, pady=5)
NumeroDePuntosEntrada.focus_set()

errorLabel = tk.Label(root, text="Error! Revise los campos", bg="yellow", font=("Italic", 15))

# -----------------------------


def getPoints(e=None):
    numberOfPoints = int(NumeroDePuntosEntrada.get())
    if (numberOfPoints > 10): 
        errorLabel.grid(row=10, column=0, columnspan=2, padx=5, pady=5)
        NumeroDePuntosEntrada.delete(0,"end")
    else:
        errorLabel.destroy()
        root.destroy()
        createPointsFrame(numberOfPoints)

tk.Button(root, text="Calcular", font=("Italic", 15), bg="LightSkyBlue1", command=getPoints).grid(row=8, column=0, columnspan=2, padx=5, pady=5)

# -----------------------------

def createPointsFrame(numberOfPoints):
    ventana = tk.Tk()
    ventana.geometry('1000x600')
    ventana.title("Spline Interpolation")
    ventana.resizable(True, True)
    
    tk.Label(ventana, text="Metodos númericos", font=("Italic", 25)).grid(row=4, column=0, padx=5, pady=5)

    tk.Label(ventana, text="Cantidad de puntos:", font=("Italic", 15)).grid(row=5, column=0, padx=0, pady=5)

    for i in range(numberOfPoints):
        tk.Label(ventana, text="x:", font=("Comic Sans MS", 15)).grid(row=i+6, column=0, padx=5, pady=5)
        x = tk.Entry(ventana, font=("Comic Sans MS", 15))
        x.grid(row=i+6, column=1, padx=5, pady=5)

        tk.Label(ventana, text="y:", font=("Comic Sans MS", 15)).grid(row=i+6, column=2, padx=5, pady=5)
        y = tk.Entry(ventana, font=("Comic Sans MS", 15))
        y.grid(row=i+6, column=3, padx=5, pady=5)

        pointsX.append(x)
        pointsY.append(y)

    tk.Button(ventana, text="Calcular", font=("Italic", 15), bg="LightSkyBlue1", command=FuncSplines).grid(row=numberOfPoints + 8, column=1, columnspan=2, padx=8, pady=8)

# -----------------------------
    
def FuncSplines():

    for point in pointsX:
        valuesX.append(float(point.get()))
    print(valuesX)

    for point in pointsY:
        valuesY.append(float(point.get()))
    print(valuesY)
   
    CoefPoli = scipy.interpolate.splrep(valuesX,valuesY)

    # num = scipy.interpolate.splev(valuesX[0],CoefPoli)
    # print(num)

    VectorPts =  np.arange(valuesX[0],valuesX[-1],0.01)

    CoefPoliEval = scipy.interpolate.splev(VectorPts,CoefPoli)

    plt.plot(valuesX,valuesY, 'o', ms=8)
    plt.plot(VectorPts,CoefPoliEval)

    plt.show()

# -----------------------------



root.mainloop()
