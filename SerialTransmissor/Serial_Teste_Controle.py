import serial
import time
import pandas as pd

#Inicialização da biblioteca e definição do baudrate do serial
ser = serial.Serial()
ser.baudrate = 115200

ser.port = 'COM5' #'/dev/ttyACM0' # Conferir a porta USB que será utilizada

ser.open()

#Robo 3
dirMot1_Robo3 = 0b10000000
dirMot2_Robo3 = 0b00100000
#Robo 2
dirMot1_Robo1 = 0b10000000
dirMot2_Robo1 = 0b00100000
#Robo 1
dirMot1_Robo2 = 0b00001000
dirMot2_Robo2 = 0b00000010
v1 = 30
v2 = 30

v3 = 30
v4 = 30

v5 = 30
v6 = 30

direcao1 = dirMot1_Robo1 + dirMot2_Robo1 + dirMot1_Robo2 + dirMot2_Robo2
direcao2 = dirMot1_Robo3 + dirMot2_Robo3
Rd = bytearray([111, direcao1, direcao2, v1, v2, v3, v4, v5, v6, 112])


dados = {1:[],2:[],3:[],4:[]}

print("Digite 1 para todos robos andarem para frente")
opc = int(input())

if (opc == 1):
    t = 0
    start = time.time()
    while t<=60:
        ser.write(Rd)
        end = time.time()
        t = end - start

        #CASO QUEIRA RETORNAR OS VALORES DE VELOCIADE DE ALGUM ROBO DESCOMENTE ESSA SEÇÃO 

        #RETORNO VELOCIDADE 1
        #v_b1 = ord(ser.read())
        #dados[1].append(t)
        #dados[2].append(v_b1)

        #RETORNO VELOCIDADE 2
        #v_b2 = ord(ser.read())
        #dados[3].append(t)
        #dados[4].append(v_b2)

    Rd = bytearray([111, 0, 0, v1, v2, v3, v4, v5, v6, 112])
    ser.write(Rd)

#Lista = pd.DataFrame({k : pd.Series(v) for k, v in dados.items()})
#print(Lista)
#Lista.to_excel("Planilha/Velocidades.xlsx")

