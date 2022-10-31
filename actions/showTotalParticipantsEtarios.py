
from util.clearScreen import clearScreen

def showTotalParticipantsEtarios(dic:dict)->dict:
    print("**********   CANTIDAD PARTICIPANTES POR GRUPO ETARIO   **********\n")
    
    juniors = dic["juniors"] 
    seniors = dic["seniors"] 
    masters = dic["masters"]
    
    print ("----------------------------")    
    print ("|{:15}|{:10}|".format('Grupo Etario'.center(15),'Cantidad'.center(10)))
    print ("----------------------------")
    
    print("|{:15}|{:10}|".format('Juniors'.center(15), str(len(juniors)).center(10)))
    print ("----------------------------")
    print("|{:15}|{:10}|".format('Seniors'.center(15), str(len(seniors)).center(10)))
    print ("----------------------------")
    print("|{:15}|{:10}|".format('Masters'.center(15), str(len(masters)).center(10)))
    print ("----------------------------")

    wait = input("\nPresione una tecla para continuar")
    clearScreen()
    return dic
