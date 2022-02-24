from glob import escape
import random
from shutil import move 
from turtle import position

Escalera = {3:11, 6:17, 9:18, 10:12} #recorrido por escalera
Serpiente = {4:14, 8:19, 16:24, 20:22} # recorrido por serpiente

turno = 0

def dar_bienvenida_usuarios(lista_nombres: list) : # ingresa al tablero
    ingresar_nombres(lista_nombres)
    move()
    print("Sigue el tablero")
    
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


def principal(nom_player: list, contador_casilleros_especiales: dict) :# se valida la opcion seleccionada
        eleccion: int = validar_opcion(1,2)
        if eleccion == 2:
            print(f"has seleccionado la 2 {nom_player[1]}")
        else:
            print("APAGUE Y VAMONOS")


def selec_tab(opcion: int, contador_casilleros_especiales: dict): # si la opcion es 1 sigue el proceso sino, sale
    lista_nombres: list = [0]
    if opcion == 1:
        dar_bienvenida_usuarios(lista_nombres)
        principal(lista_nombres, contador_casilleros_especiales)


def validar_opcion(num_min: int, num_max: int): # valida que la opcion sea las dos que tenemos en consola, por el contrario pide nuevamente ingresar
    selec: str = input("Ingrese su opción: ")
    while not selec.isnumeric() or int(selec) > num_max or int(selec) < num_min:
        print("Opcion no es válida.")
        selec = input("Ingrese nuevamente la opción: ")

    return int(selec)

def nom_val(num_player: int) : # funcion valida que el nombre sea un str cadena y no int 
    nombre: str = input(f"Ingrese el nombre del jugador {num_player}: ")
    while not nombre.isalpha() or nombre.isspace():
        print("Invalido, solo letras.")
        nombre = input(f"Intente nuevamente, nombre del jugador {num_player} es: ")

    return nombre.capitalize()

def ingresar_nombres(cant_jug: list) : # funcion indica cantidad de jugadores
    numero = int(input("ingrese cantida de jugadores : "))
    for i in range(1, numero):
        nombre: str = nom_val(i)
        cant_jug.append(nombre)
        


def principal_P() : #funcion que evalua la opcion seleccionada y la redirige a la funcion principal a seguir
    cerrar_menu: bool = False
    while not cerrar_menu:
        print("""
        Elija una opcion
        1. Iniciar juego.
        2. Salir.
        """)
        opcion: int = validar_opcion(1, 2)
        if opcion == 2:
            print("""
            Has salido sin jugar el juego de la escalera
            """)
            cerrar_menu = True
        else:
            selec_tab(opcion, Escalera)
principal_P()
