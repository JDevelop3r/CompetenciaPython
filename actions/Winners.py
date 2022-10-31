

from util.clearScreen import clearScreen


def winners(dic:dict)->dict:
    print("**********   GANADOR   **********\n")
    
    particpants = dic["participants"] 

    winner = particpants[0]
    
    print("El Ganador de la Competencia es: CI: {} | Nombre Completo: {} {} | Tiempo = {}".format(winner[0], winner[3], winner[1], winner[10]))

    wait = input("\nPresione una tecla para continuar")
    clearScreen()
    return dic