# importando bibliotecas
from PyQt5 import QtWidgets , uic
 
class telas:
    def __init__(self) :
        app = QtWidgets.QApplication([])
        self.inicio = uic.loadUi("telas/tela_inical.ui")
        self.inicio.show()
        # self.tabela_jogo = uic.loadUi("telas/tabela_jogo.ui")
        # self.ganhador = uic.loadUi("telas/ganhador.ui")
        # self.perdedor= uic.loadUi("telas/perdedor.ui")
        # self.inicio.botao_jogar.clicked.connect(self.mudar_tela)
        app.exec()
 
    # def mudar_tela(self):
    #     self.inicio.close()
    #     self.tabela_jogo.show()
 
       
 
if __name__  == '__main__':
    c = telas()