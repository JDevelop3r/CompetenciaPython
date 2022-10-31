from util.clearScreen import clearScreen

def histogram(dic:dict)->dict:
    print("**********  HISTOGRAMA DE PARTICIPANTES POR GRUPO ETARIO   **********\n")
    juniors = dic["juniors"]
    seniors= dic["seniors"]
    masters= dic["masters"]
    
    print("{:7}({:3}): |{}".format('Juniors', len(juniors),len(juniors)*'*'))
    print("{:7}({:3}): |{}".format('Seniors', len(seniors),len(seniors)*'*'))
    print("{:7}({:3}): |{}".format('Masters', len(masters),len(masters)*'*'))
    

    wait = input("\nPresione una tecla para continuar")
    clearScreen()
    return dic