from PySide6.QtWidgets import QLabel


def time_cor(label: QLabel, cor: str):
    valor = int(label.text())
    valor += 10
    label.setText(str(valor))

    # Cores usadas para modificar as cores dos botões de pontos
    if cor == "Vermelho":
        label.setStyleSheet("color: red")
    elif cor == "Azul":
        label.setStyleSheet("color: lightblue")
    elif cor == "Verde":
        label.setStyleSheet("color: green")
    elif cor == "Amarelo":
        label.setStyleSheet("color: yellow")
    elif cor == "Laranja":
        label.setStyleSheet("color: orange")
    elif cor == "Branco":
        label.setStyleSheet("color: white")
