
dia = input("Qual dia da semana queres verificar se é útil ou não? Escolha do menu abaixo, utilizando o número correspondente (ex. prima 1 para segunda-feira):\n1 - Segunda-feira;\n2 - Terça-feira; \n3 - Quarta-feira; \n4 - Quinta-feira; \n5 - Sexta-feira; \n6 - Sábado; \n7 - Domingo;\n\nR: ")

match dia:
    case "1":
        print("A segunda-feira é um dia útil.")

    case "2":
        print("A terça-feira é um dia útil.")

    case "3":
        print("A quarta-feira é um dia útil.")

    case "4":
        print("A quinta-feira é um dia útil.")

    case "5":
        print("A sexta-feira é um dia útil.")

    case "6":
        print("O sábado é final de semana.")

    case "7":
        print("O domingo é final de semana.")

    case _:
        print("Erro. Escolha uma opção entre 1 e 7.")