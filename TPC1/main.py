from parser import *
from distributions import *


def main_menu(data):
    opt = -1

    while opt != 0:
        print("--------------------------------------")
        print("Qual distribuição pretende visualizar?")
        print("--------------------------------------")
        print("1... Doença por sexo")
        print("2... Doença por idade")
        print("3... Doença por colesterol")
        print("0... Sair")
        print("--------------------------------------")

        opt = int(input("Introduza a sua opção: "))

        if opt in [1, 2, 3]:
            distr_menu(opt, data)
        elif opt == 0:
            print("\nA sair...")
        else:
            print("\nOpção inválida!\n")
    

def distr_menu(opt, data):
    print("\n------------------------------------")
    print("Em qual formato pretende visualizar?")
    print("------------------------------------")
    print("1... Tabela")
    print("2... Gráfico de barras")
    print("------------------------------------")

    format = int(input("Introduza a sua opção: "))

    match opt: 
        case 1:
            if format == 1:
                print()
                distribution_to_table(disease_by_sex(data), 0)
            elif format == 2:
                distribution_to_graph(disease_by_sex(data), 0)
                print()
            else:
                print("\nOpção inválida!")
                distr_menu(opt, data)

        case 2:
            if format == 1:
                print()
                distribution_to_table(disease_by_age(data), 1)
            elif format == 2:
                distribution_to_graph(disease_by_age(data), 1)
                print()
            else:
                print("\nOpção inválida!")
                distr_menu(opt, data)
            
        case 3:
            if format == 1:
                print()
                distribution_to_table(disease_by_cholesterol(data), 2)
            elif format == 2:
                distribution_to_graph(disease_by_cholesterol(data), 2)
                print()
            else:
                print("\nOpção inválida!")
                distr_menu(opt, data)


def main():
    data = parse("myheart.csv")
    main_menu(data)


if __name__ == "__main__":
    main()
