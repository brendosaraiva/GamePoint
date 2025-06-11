def time_cor(cor):
    cor += 10
    return cor


def equipes(q, times):
    cores = ["Vermelho", "Azul", "Verde", "Amarelo", "Laranja", "Branco"]
    times_partida = {}

    for c in range(1, q+1):
        times_partida[cores[c-1]] = times[c-1]

    return times_partida


def main():
    time_vermelho = 0
    time_azul = 0
    time_verde = 0
    time_amarelo = 0
    time_laranja = 0
    time_branco = 0

    qnt_equipe = int(input("Quantas equipes? "))

    while True:
        print("O ponto vai para quem? ")
        equipe = input("Time: ")

        if equipe.capitalize() == "Vermelho":
            time_vermelho = time_cor(time_vermelho)

        elif equipe.capitalize() == "Azul":
            time_azul = time_cor(time_azul)

        elif equipe.capitalize() == "Verde":
            time_verde = time_cor(time_verde)

        elif equipe.capitalize() == "Amarelo":
            time_amarelo = time_cor(time_amarelo)

        elif equipe.capitalize() == "Laranja":
            time_laranja = time_cor(time_laranja)

        elif equipe.capitalize() == "Branco":
            time_branco = time_cor(time_branco)
        else:
            print("Cor inválida!!!")

        continuar = input("Quer continuar? ")

        if continuar == "S":
            pass

        else:
            times = [time_vermelho, time_azul, time_verde, time_amarelo, time_laranja, time_branco]
            print(equipes(qnt_equipe, times))
            break


if __name__ == "__main__":
    main()


