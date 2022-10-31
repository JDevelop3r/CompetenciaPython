from exceptions import BadData, InvalidText
from util.clearScreen import clearScreen
from util.sortData import sortData
from util.verifyPlainTextFile import verifyPlainTextFile

def loadFile(dic:dict)->dict:
    data = None

    # Obtenemos el archivo por su nombre y lo formatemos al uso que le daremos en el proyecto
    try:
        file_name = input("Ingrese el nombre del archivo: ")
        f = open(file_name,"rt")
        if not verifyPlainTextFile(file_name):
            raise InvalidText("Debe ser un archivo de texto plano")

        data = f.readlines()
        f.close()

        dic = {"data": data}

        dic = sortData(dic)

    except FileNotFoundError:
        print("\nError: Archivo no encontrado\n")
        wait = input("Presione una tecla para continuar")
        clearScreen()
        dic = None

    except PermissionError:
        print("\nError: El archivo se encuentra en un directorio sin permisos\n")
        wait = input("Presione una tecla para continuar")
        clearScreen()
        dic = None

    except InvalidText as e:
        print("\nError: ", e)
        wait = input("Presione una tecla para continuar")
        clearScreen()
        dic = None

    except BadData as e:
        print("\nError: ", e)
        wait = input("Presione una tecla para continuar")
        clearScreen()
        dic = None

    except:
        print("\nError no esperado mientras se lee el archivo\n")
        wait = input("Presione una tecla para continuar")
        clearScreen()
        dic = None

    else:
        print("\nArchivo Leido Exitosamente\n")
        wait = input("Presione una tecla para continuar")
        clearScreen()

    return dic