"Registrador de juegos"
from datetime import datetime
data = list() 
menu = True
 

def getDetail(id):
    for i in data1:
        print(i["Nombre"])
    return " "+ str(id)

while menu:
    print("Menú de libreria de juegos, presione la tecla correspondiente a lo que desea hacer")
    print("1) Agregar un nuevo juego")
    print("2) Listar toda la libreria")
    print("3) Desplegar información de uno en específico")
    print("4) Eliminar un juego")
    print("5) Salir del programa")
    q = input()
    print(type(q))
    q = int(q)
    print(type(q))
    
    if q ==  1:
        print("Nombre")
        a = input("") 
        data1 = a
        print("Fecha de estreno: año, mes, día, ejemplo: 2020/05/25")
        b = input()
        releaseDate = datetime.strptime(b, "%Y/%m/%d") 
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
            "id": len(data) + 1,
            "Nombre" : a,
            "Fecha de estreno" : releaseDate,
            "Clasificación" : c,
            "Precio" : d,
            "Online" : e
        }
        data.append(juego)
        print(data)
    elif q == 2:
        print("lista de juegos con ID")
        for gamelist in data :
            print("Nombre del juego: " + gamelist["Nombre"])
            print("El ID del juego es:" + str(gamelist["id"]))

    elif q == 3:
        print("Desplegar información de un juego en particular, escriba el ID")
        information = int(input())
        for showinfo in data:
            if showinfo["id"] == information:
                print("Nombre: " + showinfo["Nombre"])
                print("Fecha de lanzamiento: " + showinfo["Fecha de estreno"].strftime('%d-%m-%Y'))
                print("Id: " + str(showinfo["id"]))
                print("Clasificación: " + showinfo["Clasificación"])
                print("Precio: " + showinfo["Precio"])
                print("Online: " + showinfo["Online"]) 
                break
    elif q == 4:
        print("Escriba el número ID del juego que desea eliminar de la librería")
        gameId = int(input())
        indice = 0
        for deleteGame in data: 
            if deleteGame["id"] == gameId:
                print("El juego que desea eliminar es: " + deleteGame["Nombre"])
                print("¿Desea eliminarlo? Sí o No")
                choice = input()
                if choice == "Si" or "si":
                    data.pop(indice)
                    print("Se ha eliminado correctamente")
                    break
            indice += 1
            indice = indice + 1  
    elif q == 5:    
        menu= False
        print("vuelva pronto")
