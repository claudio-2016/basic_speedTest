#!/usr/bin/env python3

import mysql.connector
import subprocess
import os
import time

#---------------------------------------------------------------------------------
def limpiarLinea(line):
    return line.strip().replace('\n','')
#---------------------------------------------------------------------------------
def obtenerLineSimple(line, etiqueta):
    line = line.replace(etiqueta, '')
    return line.strip()
#---------------------------------------------------------------------------------
def obtenerMegas(line, etiqueta):
    line = line.replace(etiqueta, '').strip()
    line = line.split(' ')[0]
    return line
#---------------------------------------------------------------------------------
def obtenerPerdidaPaquetes(line, etiqueta):
    try:
        line = line.replace(etiqueta, '').strip()
        
        if 'Not' in line:
            return '0.0'

        line = line.split(' ')[0]
        line = line.replace('%', '')
        return line
    except:
        return '0.0'

#---------------------------------------------------------------------------------

def main():
    dataSet = dict()
    serverName = 'Server:'
    isp = 'ISP:'
    download = 'Download:'
    upload = 'Upload:'
    packetLoss = 'Packet Loss:'
    url = 'Result URL:'
    fileSwap = 'swapFile.txt'
    tiempo = (60 * int(os.getenv('TIME_SPEEDTEST')))

    while True:

        os.system('speedtest --accept-license > ' + fileSwap)

        with open(fileSwap,'r') as file:
            for line in file:
                line = limpiarLinea(line)

                if(serverName in line):
                    dataSet['serverName'] = obtenerLineSimple(line, serverName)
                
                if(isp in line):
                    dataSet['isp'] = obtenerLineSimple(line, isp)

                if(download in line):
                    dataSet['download'] = obtenerMegas(line, download)
                
                if(upload in line):
                    dataSet['upload'] = obtenerMegas(line, upload)
                
                if(packetLoss in line):
                    dataSet['packetLoss'] = obtenerPerdidaPaquetes(line, packetLoss)
                
                if(url in line):
                    dataSet['url'] = obtenerLineSimple(line, url)

        connection = mysql.connector.connect(user=os.getenv('DB_USER'), password=os.getenv('PASS'), host='db', database=os.getenv('DB_NAME'))
        cursor = connection.cursor()
        
        query = """INSERT INTO speed_test (serverName,isp,download,upload,packetLoss,url) VALUES (%s,%s,%s,%s,%s,%s)"""
        data = (dataSet.get('serverName'), dataSet.get('isp'), dataSet.get('download'), dataSet.get('upload'), dataSet.get('packetLoss'), dataSet.get('url'))

        # EJECUTAMOS LA CONSULTA
        cursor.execute(query, data)

        # HACEMO EL COMMIT PARA QUE SE COMPLETE LA OPERACION, MUY IMPORTANTE
        connection.commit()

        if connection.is_connected():
            cursor.close()
            print('Coneccion cerrada')
        else:
            print("No hay conneccion activa")

        #--------------------------------------------------------------------------------#
        time.sleep(tiempo)
        


#---------------------------------------------------------------------------------

if __name__ == '__main__':
    main()
