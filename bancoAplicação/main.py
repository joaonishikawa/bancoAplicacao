from conta_corrente import *
import time
import os
import random


# Executar o programa
banco = Banco()
while True:
    time.sleep(1.5)
    os.system('cls')
    banco.exibir_menu_inicial()
