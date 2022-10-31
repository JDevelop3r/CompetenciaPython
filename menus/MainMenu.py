# ESTE ES EL MENU PRINCIPAL

from menus.ActionsMenu import ActionsMenu
from menus.FileMenu import FileMenu
from util.clearScreen import clearScreen

def MainMenu():
    option = 0
    dic = None
    while(True):
        try:
            print("**********   SISTEMA DE COMPETENCIA   **********")
            print("1. Archivos ")
            print("2. Acciones ")
            option = int(input("\nSeleccione una opcion: "));

            if(option == 1 ):
                clearScreen()
                dic = FileMenu(dic)

            if(option == 2 ):
                clearScreen()
                dic = ActionsMenu(dic)

            if(option < 1 or option > 2):
                print("\nIngrese una opcion entre el 1 y el 2\n")
                wait = input("Presione una tecla para continuar")
                clearScreen()

        except ValueError:
            print("\nERROR --> Usted debe ingresar un numero como opcion\n")
            wait = input("Presione una tecla para continuar")
            clearScreen()