import re
import json


def parse(file_path):
    data = list()

    with open(file_path) as f:
        reg_exp = re.compile(r"(?P<p_folder>\d+)::(?P<b_year>\d{4})\-(?P<b_month>\d{2})\-(?P<b_day>\d{2})::(?P<name>[a-zA-Z ]+)::(?P<f_name>[a-zA-Z ]+)::(?P<m_nome>[a-zA-Z ]+)::(?P<obs>.*)::")
        
        matches = reg_exp.finditer(f.read())
        data += [match.groupdict() for match in matches]

    return data


def processes_per_year(data):
    frequency = dict() # {ano1: qtd, ano2: qtd, ...}

    for entry in data:
        year = entry["b_year"]

        if year not in frequency:
            frequency[year] = 1
        else:
            frequency[year] += 1
            
    return frequency


def names_per_century(data):
    # {sec1: {nome1: qtd, nome2:qtd, ...}, sec2: {...} , ...}
    fst_names = dict()
    last_names = dict()

    for entry in data:
        fst_name = re.match(r"[a-zA-Z]+\b", entry["name"]).group()
        last_name = re.search(r"\b[a-zA-Z]+$", entry["name"]).group()

        year = int(entry["b_year"])
        century = year//100 + 1;

        if century not in fst_names:
            fst_names[century] = dict()

        if century not in last_names:
            last_names[century] = dict()

        if fst_name not in fst_names[century]:
            fst_names[century][fst_name] = 1
        else:
            fst_names[century][fst_name] += 1

        if last_name not in last_names[century]:
            last_names[century][last_name] = 1
        else:
            last_names[century][last_name] += 1

    return fst_names, last_names


def relationship_frequency(data):
    frequency = dict() # {relacao1: qtd, relacao2: qtd, ...}

    for entry in data:
        obs = entry["obs"]

        if match := re.search(r"(?i)\b(pai|mae|filho|filha|irmao|irma|avo|neto|neta|tio|tia|sobrinho|sobrinha|primo|prima)\b", obs):
            rel = match.group().lower()

            if rel not in frequency:
                frequency[rel] = 1    
            else:
                frequency[rel] += 1
    
    return frequency
    

def data_to_json(data, file_path):
    with open(file_path, "w") as f:
        json.dump(data[:20], f)


def print_dict(data):
    items = list(data.items())
    items.sort(key=lambda p: p[1], reverse=True)

    for item in items:
        print(item)


def print_names(fst_names, last_names):
    fst_names_keys = list(fst_names.keys())
    fst_names_keys.sort()
    last_names_keys = list(last_names.keys())
    last_names_keys.sort()

    print("\n----------NOMES PRÓPRIOS----------")
    for century in fst_names_keys:
        print(f"Século {century}")

        items = list(fst_names[century].items())
        items.sort(key=lambda p: p[1], reverse=True)

        for i in range(0,5):
            print(items[i])
                    
        print()
    print("----------------------------------")    

    print("-------------APELIDOS-------------")
    for century in last_names_keys:
        print(f"Século {century}")

        items = list(last_names[century].items())
        items.sort(key=lambda p: p[1], reverse=True)
                    
        for i in range(0,5):
            print(items[i])
                    
        print()
    print("----------------------------------\n")


def main():
    data = parse("processos.txt")

    opt = -1
    while opt != 0:
        print("----------------------------------------------------------------------------")
        print("1... Frequência de processos por ano")
        print("2... Frequência de nomes próprios e apelidos por séculos")
        print("3... Frequência dos vários tipos de relação")
        print("4... Converter os 20 primeiros registos num novo ficheiro de output em json")
        print("0... Sair")
        print("----------------------------------------------------------------------------")

        opt = int(input("Introduza a sua opção: "))

        match opt:
            case 1:
                print("\n---------------")
                print_dict(processes_per_year(data))
                print("---------------\n")

            case 2:
                fst_names, last_names = names_per_century(data)
                print_names(fst_names, last_names)

            case 3:
                print("\n-------------------------")
                print_dict(relationship_frequency(data))
                print("-------------------------\n")

            case 4:
                data_to_json(data, "data.json")
                print("\nNovo ficheiro gerado com sucesso!\n")

            case 0:
                print("\nA sair...\n")

            case other:
                print("\nOpção inválida!\n")


if __name__ == "__main__":
    main()