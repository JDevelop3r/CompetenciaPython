
# METODO PARA SEPARAR PARTICIPANTES (ORDENAR DATA)
from datetime import time
from util.verifyData import verifyData

from exceptions.BadData import BadData

def sortData(dic:dict)->dict:
    data = dic["data"]
    participants = []
    
    # Cargar los participantes en una lista por el formato de la data
    for i in range(len(data)):
        participant = data[i].replace("'", "").replace("\n","").replace(" ","")
        listParticipants = participant.split(",")
        participants.append(listParticipants) 

    # Verificar los datos de los participantes
    dic["participants"] = participants
    if verifyData(dic) == False:
        raise BadData("Los datos de los participantes estan incompletos")

    # Agregar tiempo total de participantes
    dic = addTotalTime(dic)

    # Argrear lista ordenada de participantes
    dic = orderList(dic)

    # Separar participantes por grupo etario
    dic = splitParticipantsEtarios(dic)

    # Separar participantes por sexo
    dic = splitParticipantsSex(dic)

    # Agregar grupos divididos por sexo
    dic = splitJuniorsSex(dic)
    dic = splitSeniorsMens(dic)
    dic = splitMastersMens(dic)

    # Agregar grupos por tiempo
    dic = averageJuniorsTime(dic)
    dic = averageSeniorsTime(dic)
    dic = averageMastersTime(dic)

    return dic


# Separar los participantes por sexo
def splitParticipantsSex(dic:dict)->dict:
    mens = []
    womens = []
    participants = dic["participants"]
    for i in participants:
        sex = str(i[5])
        if sex.upper() == 'M' or sex.upper() == "M" :
            mens.append(i)
        if sex.upper() == 'F' or sex.upper() == "F":
            womens.append(i) 
    
    dic["mens"] = mens
    dic["womens"] = womens
    
    return dic

# Separar los participantes por grupo etario
def splitParticipantsEtarios(dic:dict)->dict:
    juniors = []
    seniors = []
    masters = []
    
    participants = dic["participants"]
    for i in participants:
        age = int(i[6])
        if age <= 25:
            juniors.append(i)
        if age > 25 and age <= 40:
            seniors.append(i)
        if age > 40:
            masters.append(i)
            
    dic["juniors"] = juniors
    dic["seniors"] = seniors
    dic["masters"] = masters

    return dic


# Agregar tiempos totales a cada participante
def addTotalTime(dic:dict)->dict:
    newParticipants = []
    participants = dic["participants"]
    for i in participants:
        addTime = time(int(i[7]),int(i[8]),int(i[9]))
        i.append(addTime)
        newParticipants.append(i)
        
    dic["participants"] = newParticipants
    return dic


# Ordenar la lista de participantes por tiempo total
def orderList(dic:dict)->dict:
    participants = dic["participants"]
    participants.sort(key=lambda participant: participant[10])
    dic["participants"] = participants
    return dic

# Separar los juniors por sexo
def splitJuniorsSex(dic:dict)-> dict:
    juniors = dic["juniors"] 
    juniorsMens = []
    juniorsWomens = []
    
    for i in juniors:
        sex = str(i[5])
        if sex.upper() == 'M' or sex.upper() == "M" :
            juniorsMens.append(i)
        if sex.upper() == 'F' or sex.upper() == "F":
            juniorsWomens.append(i) 
            
    dic["juniorsMens"] = juniorsMens
    dic["juniorsWomens"] = juniorsWomens
    return dic
    
    
# Separar los seniors por sexo
def splitSeniorsMens(dic:dict)-> dict:
    seniors = dic["seniors"] 
    seniorsMens = []
    seniorsWomens = []
    
    for i in seniors:
        sex = str(i[5])
        if sex.upper() == 'M' or sex.upper() == "M" :
            seniorsMens.append(i)
        if sex.upper() == 'F' or sex.upper() == "F":
            seniorsWomens.append(i) 
    
    dic["seniorsMens"] = seniorsMens
    dic["seniorsWomens"] = seniorsWomens
    return dic


# Separar los masters por sexo
def splitMastersMens(dic:dict)-> dict:
    masters = dic["masters"]  
    mastersMens = []
    mastersWomens = []
    
    for i in masters:
        sex = str(i[5])
        if sex.upper() == 'M' or sex.upper() == "M" :
            mastersMens.append(i)
        if sex.upper() == 'F' or sex.upper() == "F":
            mastersWomens.append(i) 
    
    dic["mastersMens"] = mastersMens
    dic["mastersWomens"] = mastersWomens
    return dic

# Tiempo promedio de juniors
def averageJuniorsTime(dic:dict)->dict:
    
    juniorsMens = dic["juniorsMens"] 
    juniorsWomens = dic["juniorsWomens"] 
    hours = 0
    minutes = 0
    seconds = 0
    totalSeconds = 0
    
    # Calcular tiempo de juniors hombres en segundos
    for i in juniorsMens:
        totalSeconds =  totalSeconds + int(i[7])*3600 +  int(i[8])*60 +  int(i[9])
    
    averageSeconds = totalSeconds / len(juniorsMens)
    minutes, seconds = divmod(averageSeconds,60)
    hours, minutes = divmod(minutes,60)
    averageTimeJuniorMens = time(round(hours),round(minutes),round(seconds))
    dic["averageTimeJuniorMens"] = averageTimeJuniorMens
    
    hours = 0
    minutes = 0
    seconds = 0
    totalSeconds = 0
    
    # Calcular tiempo de juniors mujeres en segundos
    for i in juniorsWomens:
        totalSeconds =  totalSeconds + int(i[7])*3600 +  int(i[8])*60 +  int(i[9])
    
    averageSeconds = totalSeconds / len(juniorsWomens)
    minutes, seconds = divmod(averageSeconds,60)
    hours, minutes = divmod(minutes,60)
    averageTimeJuniorWomens = time(round(hours),round(minutes),round(seconds))
    dic["averageTimeJuniorWomens"] = averageTimeJuniorWomens
    
    
    return dic

# Tiempo promedio de seniors
def averageSeniorsTime(dic:dict)->dict:
    
    seniorsMens = dic["seniorsMens"] 
    seniorsWomens = dic["seniorsWomens"]
    hours = 0
    minutes = 0
    seconds = 0
    totalSeconds = 0
    
    # Calculo de tiempo promedio de seniors hombres
    for i in seniorsMens:
        totalSeconds =  totalSeconds + int(i[7])*3600 +  int(i[8])*60 +  int(i[9])
    
    averageSeconds = totalSeconds / len(seniorsMens)
    minutes, seconds = divmod(averageSeconds,60)
    hours, minutes = divmod(minutes,60)
    averageTimeSeniorMens = time(round(hours),round(minutes),round(seconds))
    dic["averageTimeSeniorMens"] = averageTimeSeniorMens
    
    hours = 0
    minutes = 0
    seconds = 0
    totalSeconds = 0
    
    # Calculo de tiempo promedio de seniors mujeres
    for i in seniorsWomens:
        totalSeconds =  totalSeconds + int(i[7])*3600 +  int(i[8])*60 +  int(i[9])
    
    averageSeconds = totalSeconds / len(seniorsWomens)
    minutes, seconds = divmod(averageSeconds,60)
    hours, minutes = divmod(minutes,60)
    averageTimeSeniorWomens = time(round(hours),round(minutes),round(seconds))
    dic["averageTimeSeniorWomens"] = averageTimeSeniorWomens
    
    return dic


# Tiempo promedio de masters
def averageMastersTime(dic:dict)->dict:
    
    mastersMens = dic["mastersMens"]
    mastersWomens = dic["mastersWomens"]
    hours = 0
    minutes = 0
    seconds = 0
    totalSeconds = 0
    
    # Calculo de tiempo promedio de masters hombres
    for i in mastersMens:
        totalSeconds =  totalSeconds + int(i[7])*3600 +  int(i[8])*60 +  int(i[9])
    
    averageSeconds = totalSeconds / len(mastersMens)
    minutes, seconds = divmod(averageSeconds,60)
    hours, minutes = divmod(minutes,60)
    averageTimeMasterMens = time(round(hours),round(minutes),round(seconds))
    dic["averageTimeMasterMens"] = averageTimeMasterMens
    
    hours = 0
    minutes = 0
    seconds = 0
    totalSeconds = 0
    
    # Calculo de tiempo promedio de masters mujeres
    for i in mastersWomens:
        totalSeconds =  totalSeconds + int(i[7])*3600 +  int(i[8])*60 +  int(i[9])
    
    averageSeconds = totalSeconds / len(mastersWomens)
    minutes, seconds = divmod(averageSeconds,60)
    hours, minutes = divmod(minutes,60)
    averageTimeMasterWomens = time(round(hours),round(minutes),round(seconds))
    dic["averageTimeMasterWomens"] = averageTimeMasterWomens
    
    return dic
