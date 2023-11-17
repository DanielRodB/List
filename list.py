"Registrador de juegos"
from datetime import datetime
data = list() 
menu = True
 

def getDetail(id):
    for i in data1:
        print(i["Nombre"])
    return " "+ str(id)

def gameList():
        print("Nombre")
        a = input() 
        print("Fecha de estreno: año, mes, día, ejemplo: 2020/05/25")
        b = input()
        releaseDate = datetime.strptime(b, "%Y/%m/%d") 
        print("Clasificación")
        c = input()
        print("Precio")
        d = float(input())
        print("Online")
        e = input()
        juego={
            "id": len(data) + 1,
            "Nombre" : a,
            "Fecha de estreno" : releaseDate,
            "Clasificación" : c,
            "Precio" : d,
            "Online" : e
        }
        data.append(juego)
def showLibrary(game):
    for clave in game.keys():
        print(clave + " : " + str(game[ clave]))

def showLibraries():
    for game in data:
        showLibrary(game)

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
    
    if q == 1:
        gameList()
    elif q == 2:
        showLibraries()
       
    elif q == 3:
        print("Desplegar información de un juego en particular, escriba el ID")
        a = int(input())
        for game in data:
            if  game["id"] == a:
                showLibrary(game)

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
