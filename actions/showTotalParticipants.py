from util.clearScreen import clearScreen


def showTotalPartipants(dic:dict)->dict:
    print("**********   CANTIDAD TOTAL DE PARTICIPANTES   **********\n")
    
    participants = dic["participants"]
    print(f"Cantidad Total de Participantes: {len(participants)}")
    
    wait = input("\nPresione una tecla para continuar")
    clearScreen()
    return dic

