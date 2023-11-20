"Registrador de juegos"
from datetime import datetime
data = list() 
menu = True

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
        print("¿Es online?")
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

def showLibrary():
        print("Desplegar información de un juego en específico, escriba el ID")
        a = int(input())
        for game in data:
            if  game["id"] == a:
                for clave in game.keys():
                    print(clave + " : " + str(game[clave]))

def showLibraries():
    for libraries in data:
        print("El nombre del juego es: " + libraries["Nombre"])
        print("El ID del juego es: " + str(libraries["id"]))

def deleteGame():     
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

def showMEnu(): 
    print("Menú de libreria de juegos, presione la tecla correspondiente a lo que desea hacer")
    print("1) Agregar un nuevo juego")
    print("2) Listar toda la libreria")
    print("3) Desplegar información de uno en específico")
    print("4) Eliminar un juego")
    print("5) Salir del programa")

while menu:
    showMEnu()
    q = int(input())

    if q == 1:
        gameList()
    elif q == 2:
        showLibraries()
       
    elif q == 3:
        showLibrary()

    elif q == 4:
        deleteGame()

    elif q == 5:    
        menu= False
        print("vuelva pronto")
