from util.clearScreen import clearScreen


def showWinnersGroupBySex(dic:dict)->dict:
    print("**********   GANADORES POR SEXO   **********\n")
    
    mens = dic["mens"]
    womens = dic["womens"] 
    mens_winner = mens[0]
    womens_winner = womens[0]

    # Imprimiendo Encabezado
    print ("--------------------------------------------------------------------")
    print ("|{:12}|{:10}|{:15}|{:15}|{:10}|".format('Sexo'.center(12),'Cedula'.center(10),'Primer Nombre'.center(15),
                                  'Primer Apellido'.center(15),'Tiempo'.center(10)))
    print ("--------------------------------------------------------------------")
    
    #Imprimiendo Ganador Masculino
    print("|{:12}|{:10}|{:15}|{:15}|{:10}|".format('Masculino'.center(12), str(mens_winner[0]).center(10), str(mens_winner[3]).center(15),
                                                    str(mens_winner[1]).center(15),str(mens_winner[10]).center(10)))    
    print ("--------------------------------------------------------------------")
    
    #Imprimiendo Ganador Femenino
    print("|{:12}|{:10}|{:15}|{:15}|{:10}|".format('Femenino'.center(12), str(womens_winner[0]).center(10),str(womens_winner[3]).center(15),
                                                    str(womens_winner[1]).center(15),str(womens_winner[10]).center(10)))
    print ("--------------------------------------------------------------------")


    wait = input("\nPresione una tecla para continuar")
    clearScreen()
    return dic