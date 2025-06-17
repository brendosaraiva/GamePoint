from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QGridLayout, QHBoxLayout,
    QLabel, QPushButton, QGroupBox, QScrollArea, QMessageBox
)
import sys


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

        layout_principal = QVBoxLayout(self)  # Cria e seta layout principal

        label_imagem = QLabel()
        pixmap = QPixmap("gamepoint.png")  # caminho da sua imagem
        label_imagem.setPixmap(pixmap)

        icon = QIcon("gamepoint.ico")
        icon.addPixmap(QPixmap("icone_64x64.png"))
        self.setWindowIcon(QIcon(icon))

        # Layout horizontal para imagem + botão limpar lado a lado
        layout_topo = QHBoxLayout()
        layout_topo.addWidget(label_imagem, alignment=Qt.AlignVCenter)

        self.botao_limpar = QPushButton("Limpar Seções")
        self.botao_limpar.clicked.connect(self.limpar_secoes)
        self.botao_limpar.setFixedSize(100, 30)
        layout_topo.addWidget(self.botao_limpar, alignment=Qt.AlignVCenter)

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

    def criar_secao(self, titulo):
        box = QGroupBox(titulo)
        box.setMaximumSize(500, 500)
        layout = QVBoxLayout()

        # Adiciona o ícone no topo
        label_icone = QLabel()
        pixmap = QPixmap("icone.png")  # Substitua pelo caminho do seu ícone
        label_icone.setPixmap(pixmap.scaledToWidth(32))  # Ajuste o tamanho se quiser
        layout.addWidget(label_icone)

        # Conteúdo da seção
        layout.addWidget(QLabel("Conteúdo da seção"))
        layout.addWidget(QPushButton("Botão Exemplo"))

        box.setLayout(layout)
        return box

    def adicionar_nova_secao(self):
        if self.total_secoes < 6:
            titulo = f"Time {self.total_secoes + 1}"
            nova_secao = self.criar_secao(titulo)

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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = JanelaPrincipal()
    janela.resize(800, 600)
    janela.show()
    sys.exit(app.exec())
