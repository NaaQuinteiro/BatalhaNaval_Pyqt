# importando bibliotecas
from PyQt5 import QtWidgets, uic, QtCore
import random
import sys

# classe para executar as telas
class telas:
    def __init__(self):
        self.app = QtWidgets.QApplication([])
        # importando as telas
        self.inicio = uic.loadUi("inicial.ui")
        self.inicio.show() #apresntar a tela inicio
        self.batalha = uic.loadUi("batalha.ui")
        self.vitoria = uic.loadUi("vitoria.ui")
        self.game_over = uic.loadUi("game_over.ui")

        # comando para conectar as telas com click do botao
        self.inicio.btn_start.clicked.connect(self.mudar_telas)

        #comando para sair  
        self.inicio.btn_exit.clicked.connect(self.encerrar_programa)
        self.vitoria.btn_exit.clicked.connect(self.encerrar_programa)
        self.game_over.btn_exit.clicked.connect(self.encerrar_programa)

        #comando para tentar novamente
        self.vitoria.btn_again.clicked.connect(self.again)
        self.game_over.btn_again.clicked.connect(self.again)

        self.vidas = 20
        self.tentativas = 0

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
        
        #concatena as coordenadas sorteadas que tem o mesmo nome dos botões 
        for i in range(len(sorteio_letras)):
            coordenadas.append(f"{sorteio_letras[i]}{sorteio_numeros[i]}")
        
        print(coordenadas)

        #lista para adicionar as coordenadas finais 
        self.coordenadas_barcos = []

        # laço para separar os caracteres letras de numeros de cada coordenada
        for a in range(len(coordenadas)):

            if a == 0:
                for i in range(len(coordenadas)):
                    self.coordenadas_barcos.append(coordenadas[i])
            
            if a == 1: 
                separa = list(coordenadas[a])
                self.coordenadas_barcos.append(f"{separa[0]}{int(separa[1]) + 1}")
                print(self.coordenadas_barcos)

            if a == 2:
                for i in range(2):
                    separa = list(coordenadas[a])
                    self.coordenadas_barcos.append(f"{separa[0]}{int(separa[1]) + (i + 1)}")
                    print(self.coordenadas_barcos)
                
            if a == 3:
                 for i in range(3):
                    separa = list(coordenadas[a])
                    self.coordenadas_barcos.append(f"{separa[0]}{int(separa[1]) + (i + 1)}")
                    print(self.coordenadas_barcos)
            
        # comando para executar sempre que o botões da tela forem clicados 
        for button in self.batalha.findChildren(QtWidgets.QPushButton):
            button.clicked.connect(self.select_button)

        self.app.exec()
        sys.exit(self.app.exec_()) # encerra a vida do pyQt
 
    def restart(self):
        QtCore.QCoreApplication.quit() #permite sair da aplicação 
        QtCore.QProcess.startDetached(sys.executable, sys.argv) # permite que o programa incie novamente antes de sair por completo da aplicação

    def mudar_telas(self):
        self.inicio.close() # fechar a tela
        self.batalha.show() # apresentar a tela
    
    def again(self):
        self.restart()
    
    def encerrar_programa (self):
        self.inicio.close()
        self.vitoria.close()
        self.game_over.close()
        exit()
    
    def select_button(self):

        sender = self.inicio.sender()
        senderCoordenada = sender.objectName()

        if self.tentativas < self.vidas:

            if senderCoordenada in self.coordenadas_barcos:
                sender.setStyleSheet("background-image: url('img/naufrago.png'); border: none")
                self.coordenadas_barcos.remove(senderCoordenada)

                if len(self.coordenadas_barcos) == 0:
                    self.batalha.close()
                    self.vitoria.show()

            else: 
                sender.setStyleSheet("background-image: url('img/bomb.png'); border: none")
                self.tentativas +=1
                print(self.tentativas)
        
        else:
            self.batalha.close()
            self.game_over.show()
        


if __name__  == '__main__':
    c = telas()