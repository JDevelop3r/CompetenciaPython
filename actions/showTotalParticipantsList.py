
from util.clearScreen import clearScreen


def showTotalParticipantsList(dic:dict)->dict:
    print("**********   LISTA CON TOTALIDAD DE PARTICIPANTES   **********\n")

    print ("--------------------------------------------------------------------------------------------------------------------")
    participants = dic["participants"]
    print ("|{:15}|{:20}|{:12}|{:20}|{:20}|{:5}|{:5}|{:10}|".format('Cedula'.center(15),'Primer Nombre'.center(20),'2do Nombre'.center(12), 
                                                                    'Primer Apellido'.center(20),'Segundo Apellido'.center(20) , 'Sexo'.center(5), 
                                                                    'Edad'.center(5), 'Tiempo'.center(10)))
    print ("--------------------------------------------------------------------------------------------------------------------")
    
    for participant in participants:
        
        # Obtengo los datos de cada particpante
        ci, f_surname, s_surname, f_name, s_name, sex, age, hours, minutes, seconds, total_time  = participant
        
        print ("|{:15}|{:20}|{:12}|{:20}|{:20}|{:5}|{:5}|{:10}|".format(str(ci).center(15), str(f_name).center(20),str(s_name).center(12),
                                                                        str(f_surname).center(20), str(s_surname).center(20),str(sex).center(5),
                                                                        str(age).center(5), str(total_time).center(10)))
        print ("--------------------------------------------------------------------------------------------------------------------")
        
    wait = input("\nPresione una tecla para continuar")
    clearScreen()
    return dic
