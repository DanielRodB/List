"Registrador de juegos"
from datetime import date
data = list() 
menu = True
while menu:
    print("Menú de libreria de juegos, presione la tecla correspondiente a lo que desea hacer")
    print("1) Agregar un nuevo juego")
    print("2) Listar toda la libreria")
    print("3) Desplegar información de uno en específico")
    print("4) Eliminar un juego")
    q = input()
    print(type(q))
    q = int(q)
    print(type(q))
    
    if q ==  1:
        print("Nombre")
        a = input("") 
        data1 = a
        print("Fecha de estreno")
        b = input("")
        data2 = b
        print("Clasificación")
        c = input("")
        data3 = c
        print("Precio")
        d = input("")
        data4 = d
        print("Online")
        e = input("")
        data5 = e
        juego={
            "Nombre" : a,
            "Fecha de estreno" : b,
            "Clasificación" : c,
            "Precio" : d,
            "Online" : e
        }
        data.append(juego)
        print(data)
    elif q == 2 :
        print ("opcion 2")
    elif q == 3 :
        print("opcion 3")
        menu= False
        print("vuelva pronto")
        