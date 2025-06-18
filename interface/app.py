from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QPixmap, QFont
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QGridLayout, QHBoxLayout,
    QLabel, QPushButton, QGroupBox, QScrollArea, QMessageBox
)
import sys
from game import time_cor  # sua função para pontuar


class JanelaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GamePoint")
        self.setStyleSheet("""
            QWidget {
                background-color: #2E2E2E;
                color: #FFFFFF;
            }
        """)
        self.pontos = 0
        self.times_pontuacao = []

        layout_principal = QVBoxLayout(self)  # Layout principal

        label_imagem = QLabel()
        pixmap = QPixmap("gamepoint.png")  # caminho da imagem
        label_imagem.setPixmap(pixmap)

        icon = QIcon("gamepoint.ico")
        icon.addPixmap(QPixmap("icone_64x64.png"))
        self.setWindowIcon(QIcon(icon))

        # Layout topo: imagem + botão limpar + botão finalizar
        layout_topo = QHBoxLayout()
        layout_topo.addWidget(label_imagem, alignment=Qt.AlignVCenter)

        self.botao_limpar = QPushButton("Limpar Seções")
        self.botao_limpar.clicked.connect(self.limpar_secoes)
        self.botao_limpar.setFixedSize(100, 30)
        layout_topo.addWidget(self.botao_limpar, alignment=Qt.AlignVCenter)

        self.botao_finalizar = QPushButton("Finalizar Partida")
        self.botao_finalizar.clicked.connect(self.finalizar_partida)
        self.botao_finalizar.setFixedSize(120, 30)
        layout_topo.addWidget(self.botao_finalizar, alignment=Qt.AlignVCenter)

        layout_principal.addLayout(layout_topo)

        self.total_secoes = 0

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)

        self.widget_conteudo = QWidget()
        self.grid_layout = QGridLayout(self.widget_conteudo)

        self.scroll_area.setWidget(self.widget_conteudo)
        layout_principal.addWidget(self.scroll_area)

        self.botao_adicionar = QPushButton("+ Adicionar Time")
        self.botao_adicionar.clicked.connect(self.adicionar_nova_secao)
        self.atualizar_posicao_adicionar()

    def criar_secao(self, titulo, cor):
        box = QGroupBox(titulo)
        box.setMaximumSize(500, 500)
        layout = QVBoxLayout()

        label_icone = QLabel()
        pixmap = QPixmap("icone.png")
        label_icone.setPixmap(pixmap.scaledToWidth(32))
        layout.addWidget(label_icone)

        pontuacao = QLabel(f"{self.pontos}")
        fonte = QFont()
        fonte.setPointSize(80)
        pontuacao.setFont(fonte)
        pontuacao.setAlignment(Qt.AlignCenter)  # Centraliza a pontuação

        cor_time = QLabel(cor)
        fonte = QFont()
        fonte.setPointSize(50)
        cor_time.setFont(fonte)
        cor_time.setAlignment(Qt.AlignCenter)  # Centraliza a pontuação

        layout.addWidget(cor_time, alignment=Qt.AlignCenter)
        layout.addWidget(pontuacao)

        botao_pontuar = QPushButton("Pontuar")
        # Ao clicar, chama a função time_cor e atualiza o label
        botao_pontuar.clicked.connect(lambda _, label=pontuacao: time_cor(label, cor))
        layout.addWidget(botao_pontuar)

        box.setLayout(layout)
        self.times_pontuacao.append(pontuacao)
        return box

    def adicionar_nova_secao(self):
        cores = ["Vermelho", "Azul", "Verde", "Amarelo", "Laranja", "Branco"]
        if self.total_secoes < len(cores):
            titulo = f"Time {self.total_secoes + 1}"
            cor = cores[self.total_secoes]
            nova_secao = self.criar_secao(titulo, cor)

            linha = self.total_secoes // 3
            coluna = self.total_secoes % 3

            self.grid_layout.addWidget(nova_secao, linha, coluna)
            self.total_secoes += 1
            self.atualizar_posicao_adicionar()
        else:
            QMessageBox.information(
                self,
                "Aviso",
                "Limite excedido!",
            )

    def atualizar_posicao_adicionar(self):
        self.grid_layout.removeWidget(self.botao_adicionar)

        linha = self.total_secoes // 3
        coluna = self.total_secoes % 3
        self.grid_layout.addWidget(self.botao_adicionar, linha, coluna)

    def limpar_secoes(self):
        # Remove todas as seções do grid layout, exceto o botão adicionar
        for i in reversed(range(self.grid_layout.count())):
            item = self.grid_layout.itemAt(i)
            widget = item.widget()
            if widget and widget != self.botao_adicionar:
                self.grid_layout.removeWidget(widget)
                widget.deleteLater()

        self.total_secoes = 0
        self.atualizar_posicao_adicionar()

    def time_mais_pontuado(self):
        if not self.times_pontuacao:
            return None

        maior_pontos = -1
        indice_maior = -1

        for i, label in enumerate(self.times_pontuacao):
            pontos = int(label.text())
            if pontos > maior_pontos:
                maior_pontos = pontos
                indice_maior = i

        return indice_maior, maior_pontos

    def finalizar_partida(self):
        resultado = self.time_mais_pontuado()
        if resultado is None:
            QMessageBox.information(self, "Resultado", "Nenhum time pontuado.")
        else:
            indice, pontos = resultado
            QMessageBox.information(
                self,
                "Resultado",
                f"O time {indice + 1} é o vencedor com {pontos} pontos!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = JanelaPrincipal()
    janela.resize(800, 600)
    janela.show()
    sys.exit(app.exec())
