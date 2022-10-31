from util.clearScreen import clearScreen

def showWinnersEtariosBySex(dic:dict)->dict:
    print("**********   GANADORES POR GRUPO ETARIO Y SEXO   **********\n")
    
    juniorsMens = dic["juniorsMens"]
    juniorsWomens = dic["juniorsWomens"]
    
    seniorsMens = dic["seniorsMens"] 
    seniorsWomens = dic["seniorsWomens"]
    
    mastersMens = dic["mastersMens"]
    mastersWomens = dic["mastersWomens"]
    
    
    #Obtengo los ganadores por sexo de cada grupo etario
    junior_men_winner = juniorsMens[0]
    junior_women_winner = juniorsWomens[0]
    
    seniors_men_winner = seniorsMens[0]
    seniors_women_winner = seniorsWomens[0]
    
    master_men_winner = mastersMens[0]
    masters_women_winner = mastersWomens[0]
    
    print ("-------------------------------------------------------------------------------------------------------------------------------------------------")
    # Imprimiendo Encabezado
    print ("|{:15}|{:63}|{:63}|".format(''.center(15),'Masculino'.center(63),'Femenino'.center(63)))
    print ("-------------------------------------------------------------------------------------------------------------------------------------------------")
    print ("|{:15}|{:10}|{:20}|{:20}|{:10}|{:10}|{:20}|{:20}|{:10}|".format('Grupo'.center(15),'Cedula'.center(10),'Primer Nombre'.center(20),
                                  'Primer Apellido'.center(20),'Tiempo'.center(10),'Cedula'.center(10),'Primer Nombre'.center(20),
                                  'Primer Apellido'.center(20),'Tiempo'.center(10)))
    print ("-------------------------------------------------------------------------------------------------------------------------------------------------")
    
    #Imprimiendo Ganador Juniors por Sexo
    print("|{:15}|{:10}|{:15}|{:15}|{:10}|{:10}|{:15}|{:15}|{:10}|".format('Junior'.center(15), str(junior_men_winner[0]).center(10), str(junior_men_winner[3]).center(20),
                                                    str(junior_men_winner[1]).center(20),str(junior_men_winner[10]).center(10), 
                                                    str(junior_women_winner[0]).center(10), str(junior_women_winner[3]).center(20),
                                                    str(junior_women_winner[1]).center(20),str(junior_women_winner[10]).center(10)))    
    print ("-------------------------------------------------------------------------------------------------------------------------------------------------")
    
    #Imprimiendo Ganador Seniors por Sexo
    print("|{:15}|{:10}|{:15}|{:15}|{:10}|{:10}|{:15}|{:15}|{:10}|".format('Senior'.center(15), str(seniors_men_winner[0]).center(10), str(seniors_men_winner[3]).center(20),
                                                    str(seniors_men_winner[1]).center(20),str(seniors_men_winner[10]).center(10), 
                                                    str(seniors_women_winner[0]).center(10), str(seniors_women_winner[3]).center(20),
                                                    str(seniors_women_winner[1]).center(20),str(seniors_women_winner[10]).center(10)))    
    print ("-------------------------------------------------------------------------------------------------------------------------------------------------")

    #Imprimiendo Ganador Masters por Sexo
    print("|{:15}|{:10}|{:15}|{:15}|{:10}|{:10}|{:15}|{:15}|{:10}|".format('Master'.center(15), str(master_men_winner[0]).center(10), str(master_men_winner[3]).center(20),
                                                    str(master_men_winner[1]).center(20),str(master_men_winner[10]).center(10), 
                                                    str(masters_women_winner[0]).center(10), str(masters_women_winner[3]).center(20),
                                                    str(masters_women_winner[1]).center(20),str(masters_women_winner[10]).center(10)))    
    print ("-------------------------------------------------------------------------------------------------------------------------------------------------")


    wait = input("\nPresione una tecla para continuar")
    clearScreen()
    return dic