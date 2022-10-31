

from actions.Winners import winners
from actions.averageTimeByGroup import averageTimeByGroup
from actions.histogram import histogram
from actions.showTotalParticipantsBySex import showTotalParticipantsBySex
from actions.showTotalParticipants import showTotalPartipants
from actions.showTotalParticipantsEtarios import showTotalParticipantsEtarios
from actions.showTotalParticipantsList import showTotalParticipantsList
from actions.showWinnersEtariosBySex import showWinnersEtariosBySex
from actions.showWinnersGroupBySex import showWinnersGroupBySex
from actions.showWinnersGroupEtarios import showWinnersGroupEtarios
from util.clearScreen import clearScreen

# ESTE ES EL MENU DE LAS OPCIONES DE ACCIONES
def ActionsMenu(dic:dict)-> dict:
    option = 0
    if(dic):
        while(True):
            try:
                print("**********   MENU ACCIONES   **********")
                print("1. Lista con Totalidad de Participantes ")
                print("2. Cantidad Total de Participantes ")
                print("3. Cantidad de Participantes por Grupo Etario")
                print("4. Cantidad de Participantes por Sexo")
                print("5. Ganadores por Grupo Etario")
                print("6. Ganadores por Sexo")
                print("7. Ganadores por Grupo Etario y Sexo")
                print("8. Ganador General")
                print("9. Histrograma de participantes por Grupo Etario")
                print("10. Promedio de Tiempo por Grupo Etario y Sexo")
                print("11. Regresar ")
                option = int(input("\nSeleccione una opcion: "));

                if(option == 1):
                    clearScreen()
                    dic = showTotalParticipantsList(dic)
                
                if(option == 2):
                    clearScreen()
                    dic = showTotalPartipants(dic)
                
                if(option == 3):
                    clearScreen()
                    dic = showTotalParticipantsEtarios(dic)
                
                if(option == 4):
                    clearScreen()
                    dic = showTotalParticipantsBySex(dic)
                
                if(option == 5):
                    clearScreen()
                    dic = showWinnersGroupEtarios(dic)
                
                if(option == 6):
                    clearScreen()
                    dic = showWinnersGroupBySex(dic)
                
                if(option == 7):
                    clearScreen()
                    dic = showWinnersEtariosBySex(dic)
                    
                if(option == 8):
                    clearScreen()
                    dic = winners(dic)

                if(option == 9):
                    clearScreen()
                    dic = histogram(dic)
                
                if(option == 10):
                    clearScreen()
                    dic = averageTimeByGroup(dic)
                    
                
                if(option == 11):
                    clearScreen()
                    break
                
                if(option < 1 or option > 11):
                    print("\nIngrese una opcion entre el 1 y el 9\n")
                    wait = input("Presione una tecla para continuar")
                    clearScreen()
                
            except ValueError:
                print("\nError: Usted debe ingresar un numero valido de la lista\n")
                wait = input("Presione una tecla para continuar")
                clearScreen()
    else:
        print("Error: Se debe cargar un archivo antes de entrar al menu de acciones")
        wait = input("Presione una tecla para continuar")
        clearScreen()

    return dic