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
        user_choice = int(input(("Escriba el ID del juego que desea mostrar: ")))
        for game in self.storage:
            if user_choice == game.id:
                print(game.gameDescription())

    def deleteG(self):
        gameID = int(input(("Escriba el ID del juego que desea eliminar: ")))
        indice = 0 
        for delete_game in self.storage:
            if delete_game.id == gameID:

                answer = input(("El juego que desea eliminar es: \n" + delete_game.toString()))
                if answer == "Si" or "si":
                    self.storage.pop(indice)
                    print("Se ha eliminado correctamente")
                    break
            indice += 1

    def gameInDiscount(self):
        for game_offer in self.storage:
            self.validateFSG()
            discount = int(input(("Escriba el porcentaje de descuento que tiene el juego: ")))
            final_price = game_offer.price / 100 * (100-discount) 
            print("El juego pasó de: $" + str(game_offer.price) + " a: $" + str(final_price))
            break

    def gameDates(self):
        show_date = int(input(("Seleccione el rango de fechas en el que desea mostrar los juegos \n 1)Últimos 3 meses \n 2)Últimos 6 meses \n 3)1 año \n ")))
        if  show_date == 1: 
            days_before = 90 
        elif show_date == 2:
            days_before = 180
        elif show_date == 3:
            days_before = 365
        dateFS2 = datetime.now()
        lastDate = dateFS2 - timedelta(days = days_before)
        for compare_dates in self.storage:
            dateFS = compare_dates.release 
            if dateFS > lastDate:
                print(" El título del juego es: " + compare_dates.name + " con ID: " + str(compare_dates.id) +" Fecha de estreno: "+ str(compare_dates.release))


def showMEnu(): 
    print("""
    Menú de libreria de juegos, presione la tecla correspondiente a lo que desea hacer
1) Agregar un nuevo juego
2) Listar toda la libreria
3) Desplegar información de uno en específico
4) Eliminar un juego
5) Mostrar juegos con descuento
6) Mostrar juegos con rango de fecha
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
        library.gameDates()


