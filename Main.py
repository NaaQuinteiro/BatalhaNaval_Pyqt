# importando bibliotecas
from PyQt5 import QtWidgets, uic
import random

# classe para executar as telas
class telas:
    def __init__(self) :
        app = QtWidgets.QApplication([])
        # importando as telas
        self.inicio = uic.loadUi("inicial.ui")
        self.inicio.show() #apresntar a tela inicio
        self.batalha = uic.loadUi("batalha.ui")
        self.vitoria = uic.loadUi("vitoria.ui")
        self.game_over = uic.loadUi("game_over.ui")

        # comando para conectar as telas com click do botao
        self.inicio.btn_start.clicked.connect(self.mudar_telas) 
        self.inicio.btn_exit.clicked.connect(self.encerrar_programa)


        # sortear as coordenadas dos barcos 
        letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
        numeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        coordenadas = []

        #Sorteia 4 caracteres de uma vez sem repetir
        sorteio_letras = random.sample(letras, 4)

        #Laço para sortear novamente se a posição for invalida para o barco 
        while True: 
            sorteio_numeros = random.sample(numeros, 4)

            if int(sorteio_numeros[1]) > 8:
                continue

            if int(sorteio_numeros[2]) > 7:
                continue

            if int(sorteio_numeros[3]) > 6:
                continue

            else:
                break
        
        for i in range(len(sorteio_letras)):
            coordenadas.append(f"{sorteio_letras[i]}{sorteio_numeros[i]}")
        
        print(coordenadas)

        #parou no self. barcos = []
        app.exec()
 

    def mudar_telas(self):
        self.inicio.close() # fechar a tela
        self.batalha.show() # apresentar a tela
    
    def encerrar_programa (self):
        self.inicio.close()
        exit()


 
       
 
if __name__  == '__main__':
    c = telas()