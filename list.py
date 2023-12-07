#Libreria de juegos
from datetime import datetime
from datetime import timedelta

class Game():
    id = ''
    name = ''
    price = ''
    category = ''
    online = ''
    release = ''

    def __init__(self, id, name, price, online, release, category ) -> None:
        self.id = id
        self.name = name
        self.release = release 
        self.price = price
        self.category = category
        
        self.online = online
        
    def toString(self):
        return "Id: " + str(self.id) + " Nombre: " + self.name
    
    def gameDescription(self):
        return "Id: " + str(self.id) + " Nombre: " + self.name + " Fecha de estreno: " + str(self.release) + " Categoría: " + str(self.category) + " Online: " + str(self.online) + " Precio: $" + str(self.price)

class LibraryBase():

    storage = list()

    def __init__(self) -> None:
        for i in range(0, 5):
            self.storage.append(
                Game(
                    len(self.storage)+1,
                    str(i)+ " juego",
                    i*65+150,
                    True,
                    datetime.now(),
                    "A+"
                )
            )
        

    def addGame(self): 
        id = len(self.storage) + 1
        
        name = str(input(('Escriba el título del juego: ')))

        release = input((('Escriba la fecha de estreno: año, mes, dia:  ')))
        release = datetime.strptime(release, "%Y/%m/%d" )

        price = float(input(('Escriba el precio del juego: ')))

        category = str(input(('Escriba la clasificación del juego: ')))

        online = bool(input(('¿Se puede jugar online? : ')))
        
        game = Game(id, name, price, online, release, category)
        self.storage.append(game)
    
    def showGames(self):
        for game in self.storage:
            print(game.toString())

    def validateFSG(self):    
        userChoice = int(input(("Escriba el ID del juego que desea mostrar: ")))
        for game in self.storage:
            if userChoice == game.id:
                print(game.gameDescription())

    def deleteG(self):
        gameID = int(input(("Escriba el ID del juego que desea eliminar: ")))
        indice = 0 
        for deleteGame in self.storage:
            if deleteGame.id == gameID:

                answer = input(("El juego que desea eliminar es: \n" + deleteGame.toString()))
                if answer == "Si" or "si":
                    self.storage.pop(indice)
                    print("Se ha eliminado correctamente")
                    break
            indice += 1

    def gameInDiscount(self):
        for gameOffer in self.storage:
            if gameOffer.price >= 260:
                discount = gameOffer.price / 100 * 70
                print ("Juegos con descuento del 30% " + gameOffer.toString() + " de: $" + str(gameOffer.price) + " a $" + str(discount) )

    def gameDiffDate(self):
        for diffDate in self.storage:
            year = timedelta(days = 365)
            classicDate = 2020* year
            if  diffDate.release * 
                print("El juego: " + diffDate.name + " es classic")



def showMEnu(): 
    print("""
    Menú de libreria de juegos, presione la tecla correspondiente a lo que desea hacer
1) Agregar un nuevo juego
2) Listar toda la libreria
3) Desplegar información de uno en específico
4) Eliminar un juego
5) Mostrar juegos con descuento
6) Mostrar juegos clásicos
7) Salir del programa
          """)
    


start = True
library = LibraryBase()

while start:
    showMEnu()
    choice = int(input())
    if choice == 1:
        library.addGame()
    elif choice == 2:
        library.showGames()
    elif choice == 3:
        library.validateFSG()
    elif choice == 4:
        library.deleteG()
    elif choice == 5:
        library.gameInDiscount()
    elif choice == 6:
        library.gameDiffDate()


