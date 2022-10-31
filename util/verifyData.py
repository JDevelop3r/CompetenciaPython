def verifyData(dic:dict)->bool:
    participants = dic["participants"]

    for i in participants:
        if len(i) != 10:
            return False

    return True