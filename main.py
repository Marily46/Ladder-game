import random
from shutil import move 
from turtle import position

Escalera = {3:11, 6:17, 9:18, 10:12} #recorrido por escalera
Serpiente = {4:14, 8:19, 16:24, 20:22} # recorrido por serpiente

turno = 0 


def move(position): #funcion que define posicion y estado en el que cae (escalera o serpiente) sube o baja
    tir = random.randint(1,6) #cae entre los num 1,6
    print(f"Avanza:{tir}") # avanza la cantidad que cae en dado 
    position = position + tir # suma numero generado de 1,6 random y posicion
    if position in Serpiente: # condicion validar cuando desciende por la serpiente
        print("Baja por la serpiente")
        position = Serpiente[position]
        print(f"Jugardor avanza a cuadro : {position}")
    elif position in Escalera: # condicion validar cuando sube por la escalera
        print("Sube por la escalera")
        position = Escalera[position]
        print(f"Jugardor avanza a cuadro : {position}")
    else:
        print(f"Jugardor avanza a cuadro:{position}")
    print("\n")
    return position

while True: # condicion que evalua la funcion anterior mayor o igual a 25 para terminar ejecucion
    turno = move(turno)
    if turno >=25:
        print("Fin")
        break






