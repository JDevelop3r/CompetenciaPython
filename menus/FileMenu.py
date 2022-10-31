
import sys
from menus.ActionsMenu import ActionsMenu
from util.clearScreen import clearScreen
from util.loadFile import loadFile

# MENU SECCION ARCHIVOS
def FileMenu(dic:dict)->dict:
    option = 0
    while(True):
        try:
            print("**********   MENU ARCHIVOS   **********")
            print("1. Cargar Archivo ")
            print("2. Regresar al Menu Principal ")
            print("3. Salir del Sistema ")
            option = int(input("\nSeleccione una opcion: "));

            if(option == 1 ):
                clearScreen()
                dic = loadFile(dic)

            if(option == 2 ):
                clearScreen()
                dic = ActionsMenu(dic)

            if(option == 3 ):
                clearScreen()
                sys.exit()

            if(option < 1 or option > 3):
                print("\nIngrese una opcion entre el 1 y el 3\n")
                wait = input("Presione una tecla para continuar")
                clearScreen()

        except ValueError:
            print("\nError: Usted debe ingresar un numero valido\n")
            wait = input("Presione una tecla para continuar")
            clearScreen()