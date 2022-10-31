
from util.clearScreen import clearScreen


def showTotalParticipantsBySex(dic:dict)->dict:
    print("**********  CANTIDAD DE PARTICIPANTES POR SEXO   **********\n")
    mens = dic["mens"] 
    womens = dic["womens"] 
    print(f"Cantidad De Participantes por Sexo: Masculino: {len(mens)} | Femenino: {len(womens)}")
        
    wait = input("\nPresione una tecla para continuar")
    clearScreen()
    return dic