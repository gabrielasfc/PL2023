import numpy as np
import matplotlib.pyplot as plt


def disease_by_sex(data):
    distr = {
        "M": {False: 0, True: 0},
        "F": {False: 0, True: 0}
    }

    for person in data.people:
        distr[person.sex][person.has_disease] += 1

    return distr


def disease_by_age(data):
    min = data.bounds["age"]["min"]
    max = data.bounds["age"]["max"]

    distr = dict()

    for i in range(min // 5, (max // 5) + 1):
        distr[f"{i * 5} - {(i * 5) + 4}"] = {False: 0, True: 0}

    for person in data.people:
        lower_bound = (person.age // 5) * 5
        upper_bound = lower_bound + 4
        distr[f"{lower_bound} - {upper_bound}"][person.has_disease] += 1

    return distr


def disease_by_cholesterol(data):
    min = data.bounds["cholesterol"]["min"]
    max = data.bounds["cholesterol"]["max"]

    distr = dict()
    
    for i in range(min // 10, (max // 10) + 1):
        distr[f"{i * 10} - {(i * 10) + 9}"] = {False: 0, True: 0}

    for person in data.people:
        lower_bound = (person.cholesterol // 10) * 10
        upper_bound = lower_bound + 9
        distr[f"{lower_bound} - {upper_bound}"][person.has_disease] += 1

    return distr


def distribution_to_table(distribution, type):
    keys = list(distribution.keys())

    if type == 0:
        table = "     Com doença   Sem doença  \n"
        for i in range(len(keys)):
            table += ' ' * (len(keys[i])) + f"{keys[i]} "
            table += ' ' * (12 - len(str(distribution[keys[i]][True]))) + f"{distribution[keys[i]][True]}  "
            table += ' ' * (11 - len(str(distribution[keys[i]][False]))) + f"{distribution[keys[i]][False]} \n"

    elif type == 1 or type == 2:
        table = "            Com doença   Sem doença  \n"
        for i in range(len(keys)):
            table += ' ' * (9 - len(keys[i])) + f"{keys[i]} "
            table += ' ' * (12 - len(str(distribution[keys[i]][True]))) + f"{distribution[keys[i]][True]}  "
            table += ' ' * (11 - len(str(distribution[keys[i]][False]))) + f"{distribution[keys[i]][False]} \n"

    print(table)


def distribution_to_graph(distribution, type):
    plt.figure(figsize=[19, 9])

    x_axis = np.arange(len(distribution.keys()))  # alinhar posiçoes das legendas (keys)
    x_values = [str(key) for key in distribution.keys()]  # keys (sexos, faixas etarias, niveis de colesterol)
    y_wdisease = [values[True] for values in distribution.values()]  # numero de doentes
    y_wtdisease = [values[False] for values in distribution.values()]  # numero de nao doentes

    plt.barh(x_axis - 0.2, y_wdisease, label="Com doença", tick_label=x_values, height=0.4)
    plt.barh(x_axis + 0.2, y_wtdisease, label="Sem doença", tick_label=x_values, height=0.4)

    plt.yticks(x_axis, distribution.keys())  # desenhar legendas (keys)
    plt.xlabel("Frequência")

    title = "Distribuição de doença"

    match type:
        case 0:
            size = 18
            title += " por sexo"
            plt.ylabel("Sexo")
        case 1:
            size = 11
            title += " por idade"
            plt.ylabel("Escalão etário")
        case 2:
            size = 4
            title += " por colesterol"
            plt.ylabel("Nível de colesterol")

    plt.title(title)

    # valores à frente das barras
    for i, v in enumerate(y_wdisease):
        if v != 0:
            plt.text(v, i - 0.2, " " + str(v), fontsize=size, color='black', va='center')

    for i, v in enumerate(y_wtdisease):
        if v != 0:
            plt.text(v, i + 0.2, " " + str(v), fontsize=size, color='black', va='center')

    plt.legend()
    plt.show()
