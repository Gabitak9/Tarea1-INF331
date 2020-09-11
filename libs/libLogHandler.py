#!/usr/bin/python3
#
# libLogHandler es un modulo que contiene las funciones para la generación de logs
#

import time
import datetime

#---------------------------------------------------------------------------------

def initFunction(date,info, filename):
    """Generación de entrada de inicialización del programa

    Args:
        date (timestamp): fecha y hora
        info (list): informacion requerida
        filename (string): nombre del archivo de logs

    Returns:
        None
    """
    newLog = str(date)+' >> Inicialización de herramienta\n'

    with open(filename, 'a') as file:
       file.write(newLog)

    return None

def endFunction(date,info, filename):
    """Generación de entrada de término del programa

    Args:
        date (timestamp): fecha y hora
        info (list): informacion requerida
        filename (string): nombre del archivo de logs

    Returns:
        None
    """
    newLog = str(date)+' >> Ejecución terminada\n'

    with open(filename, 'a') as file:
       file.write(newLog)

    return None

def initComparison(date,info, filename):
    """Generación de entrada de inicio de comparación

    Args:
        date (timestamp): fecha y hora
        info (list): informacion requerida
        filename (string): nombre del archivo de logs

    Returns:
        None
    """
    newLog = '\t|---'+str(date)+' >> Inicio de comparación n° '+str(info[0])+'\n'

    with open(filename, 'a') as file:
       file.write(newLog)

    return None

def enterString1(date,info, filename):
    """Generación de entrada de ingreso de cadena 1

    Args:
        date (timestamp): fecha y hora
        info (list): informacion requerida
        filename (string): nombre del archivo de logs

    Returns:
        None
    """
    newLog = '\t\t|---'+str(date)+' >> Ingresada cadena 1: '+str(info[0])+'\n'

    with open(filename, 'a') as file:
       file.write(newLog)

    return None

def enterString2(date,info, filename):
    """Generación de entrada de ingreso de cadena 2

    Args:
        date (timestamp): fecha y hora
        info (list): informacion requerida
        filename (string): nombre del archivo de logs

    Returns:
        None
    """
    newLog = '\t\t|---'+str(date)+' >> Ingresada cadena 2: '+str(info[0])+'\n'

    with open(filename, 'a') as file:
       file.write(newLog)

    return None

def successComparison(date,info, filename):
    """Generación de entrada de comparacion exitosa

    Args:
        date (timestamp): fecha y hora
        info (list): informacion requerida
        filename (string): nombre del archivo de logs

    Returns:
        None
    """
    newLog = '\t\t|---'+str(date)+' >> Comparación exitosa\n\t\t\t|-----------------------------result: '+str(info[0])+'\n'

    with open(filename, 'a') as file:
       file.write(newLog)

    return None

def failComparison(date,info, filename):
    """Generación de entrada de comparacion fallida

    Args:
        date (timestamp): fecha y hora
        info (list): informacion requerida
        filename (string): nombre del archivo de logs

    Returns:
        None
    """
    newLog = '\t\t|---'+str(date)+' >> Comparación fallida\n\t\t\t|-----------------------------details: '+str(info[0])+'\n'

    with open(filename, 'a') as file:
       file.write(newLog)

    return None

def interruption(date,info, filename):
    """Generación de entrada de comparacion fallida

    Args:
        date (timestamp): fecha y hora
        info (list): informacion requerida
        filename (string): nombre del archivo de logs

    Returns:
        None
    """
    newLog = '\t\t|---'+str(date)+' >> Comparación interrumpida\n\t\t\t|-----------------------------details: '+str(info[0])+'\n'

    with open(filename, 'a') as file:
       file.write(newLog)

    return None

#---------------------------------------------------------------------------------

# Switcher para introducir logs
switcher = {
        0: initFunction,
        1: endFunction,
        2: initComparison,
        3: enterString1,
        4: enterString2,
        5: successComparison,
        6: failComparison,
        7: interruption
    }

#---------------------------------------------------------------------------------

def getLog(code, filename, info):
    """getLog() es un handler que recibe desde el programa principal el código
    e información que necesita para generar una entrada en el archivo de logs

    Args:
        code (int): código identidicador del log
        filename (string): nombre del archivo donde registrar el log
        info (list): listado con información util para la generación de log

    Returns:
        None
    """    

    date = datetime.datetime.now()
    func = switcher.get(code)
    func(date,info, filename)
    
    return None