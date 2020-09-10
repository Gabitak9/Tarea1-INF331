#!/usr/bin/python3
#
# INF331 - TAREA1
# Validación y Verificación
# {Una función que compara 2 cadenas de caracteres para responder a la pregunta ¿cuál cadena es más larga?}
#
# @gsepulve
#

import datetime
from libs import libLogHandler as handler

FILENAME = 'logs/[LOG] '+str(datetime.datetime.now())

def compareString(a,b):
    """compareString(a,b) compara el largo de dos cadenas para indicar cual de ellas es mas larga

    Args:
        a (string): cadena 1
        b (string): cadena 2

    Returns:
        None
    """    
    try:
        
        lenStringA = len(a)
        lenStringB = len(b)

        if lenStringA > lenStringB:
            result='\t{La cadena 1 es mas larga por %d caracteres}'%(lenStringA-lenStringB)
            print(result)
        elif lenStringA < lenStringB:
            result='\t{La cadena 2 es mas larga por %d caracteres}'%(lenStringB-lenStringA)
            print(result)
        else:
            result='\t{Las cadenas tienen el mismo largo}'
            print(result)
        
        handler.getLog(5,FILENAME,[result])

    except Exception as e:

        print('[!] Ha ocurrido un error. Saltando comparación.\ndetails : %s'%str(e))
        handler.getLog(6,FILENAME,[e])  

    return None

if __name__ == "__main__":
    
    try:

        handler.getLog(0,FILENAME,None)

        print('============================================== INF331 - Tarea 1')
        print('                                                      @gsepulve\n')
        print('(!) Ingrese "exit()" para salir\n')

        count = 1

        while(True):

            print('[*] Comparación n° %d'%count)
            handler.getLog(2,FILENAME,[count])

            firstString = str(input('\t[+] Ingrese cadena 1: '))
            firstString =  firstString.replace(" ", "")
            handler.getLog(3,FILENAME,[firstString])

            if firstString == 'exit()':
                break

            secondString = str(input('\t[+] Ingrese cadena 2: '))
            secondString = secondString.replace(" ","")
            handler.getLog(4,FILENAME,[secondString])

            compareString(firstString,secondString)

            print()
            count += 1
        
        handler.getLog(1,FILENAME,None)
        print('\nCerrando ... ')

    except Exception as a:
        
        print('[!] ERROR DE EJECUCIÓN')