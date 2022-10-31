from util.clearScreen import clearScreen


def showWinnersGroupEtarios(dic:dict)->dict:
    print("**********   GANADORES POR GRUPO ETARIO   **********\n")
    
    juniors = dic["juniors"] 
    seniors = dic["seniors"] 
    masters = dic["masters"] 
    
    junior_winner = juniors[0]
    seniors_winner = seniors[0]
    masters_winner = masters[0]
    
    # Imprimiendo Encabezado
    print ("--------------------------------------------------------------------------------------")
    print ("|{:15}|{:15}|{:20}|{:20}|{:10}|".format('Grupo Etario'.center(15),'Cedula'.center(15),'Primer Nombre'.center(20),
                                  'Primer Apellido'.center(20),'Tiempo'.center(10)))
    print ("--------------------------------------------------------------------------------------")
    
    #Imprimiendo Ganador Junior
    print("|{:15}|{:15}|{:20}|{:20}|{:10}|".format('Juniors'.center(15), str(junior_winner[0]).center(15), str(junior_winner[3]).center(20),
                                                    str(junior_winner[1]).center(20),str(junior_winner[10]).center(10)))    
    print ("--------------------------------------------------------------------------------------")

    
    #Imprimiendo Ganador Senior
    print("|{:15}|{:15}|{:20}|{:20}|{:10}|".format('Seniors'.center(15), str(seniors_winner[0]).center(15),str(seniors_winner[3]).center(20),
                                                    str(seniors_winner[1]).center(20),str(seniors_winner[10]).center(10)))
    print ("--------------------------------------------------------------------------------------")

    
    #Imprimiendo Ganador Master    
    print("|{:15}|{:15}|{:20}|{:20}|{:10}|".format('Masters'.center(15), str(masters_winner[0]).center(15),str(masters_winner[3]).center(20),
                                                    str(masters_winner[1]).center(20),str(masters_winner[10]).center(10)))
    print ("--------------------------------------------------------------------------------------")
    

    wait = input("\nPresione una tecla para continuar")
    clearScreen()
    return dic