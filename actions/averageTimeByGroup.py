from util.clearScreen import clearScreen


def averageTimeByGroup(dic:dict)->dict:
    print("**********   PROMEDIO DE TIEMPO DE CADA GRUPO  **********\n")
    averageTimeJuniorMens = dic["averageTimeJuniorMens"]
    averageTimeJuniorWomens = dic["averageTimeJuniorWomens"]
    
    averageTimeSeniorMens = dic["averageTimeSeniorMens"]
    averageTimeSeniorWomens = dic["averageTimeSeniorWomens"]
    
    averageTimeMasterMens = dic["averageTimeMasterMens"]
    averageTimeMasterWomens = dic["averageTimeMasterWomens"]
    
    # Imprimr Encabezado
    print ("-------------------------------------------------")
    print ("|{:15}|{:15}|{:15}|".format('Grupo'.center(15),'Masculino'.center(15), 'Femenino'.center(15)))
    print ("-------------------------------------------------")

    # Imprimr Promedio Grupo Junior
    print ("|{:15}|{:15}|{:15}|".format('Juniors'.center(15),str(averageTimeJuniorMens).center(15),str(averageTimeJuniorWomens).center(15)))
    print ("-------------------------------------------------")

    # Imprimir Promedio Grupo Senior
    print ("|{:15}|{:15}|{:15}|".format('Senior'.center(15),str(averageTimeSeniorMens).center(15),str(averageTimeSeniorWomens).center(15)))
    print ("-------------------------------------------------")
    
    # Imprimir Promedio Grupo Master
    print ("|{:15}|{:15}|{:15}|".format('Master'.center(15),str(averageTimeMasterMens).center(15),str(averageTimeMasterWomens).center(15)))

    print ("-------------------------------------------------")

    wait = input("\nPresione una tecla para continuar")
    clearScreen()

    return dic