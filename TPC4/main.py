import re
import json
from statistics import mean


def get_header_info(header_line):
    header_reg_exp = re.compile(r"([^,{]+)(?:\{(\d+)(?:,(\d+))?\}(?:::(\w+))?)?[,]?")
    header_fields = header_reg_exp.findall(header_line)

    header = [] # lista com os nomes dos campos do cabeçalho
    size_bounds = dict() # para cada nome (caso seja uma lista) tem um tuplo (limite inferior, limite superior) ou (limite superior, '')
    aggr_functions = dict() # para cada nome (caso tenha funçao de agregaçao) tem a respetiva funçao

    for i in range(0, len(header_fields)):
        name = header_fields[i][0]
        bound1 = header_fields[i][1]
        bound2 = header_fields[i][2]
        aggr_funct = header_fields[i][3]

        header += [name]

        if aggr_funct != '':
            aggr_functions[name] = aggr_funct

        if bound1 != '':
            size_bounds[name] = (bound1, bound2)
    
    return header, size_bounds, aggr_functions


def make_reg_exp(header, size_bounds, aggr_functions):
    reg_exp = ""

    for name in header:
        if name in size_bounds:
            bound1 = size_bounds[name][0]
            bound2 = size_bounds[name][1]

            if bound2 != '':
                list_range = f"{{{int(bound1)},{int(bound2)}}}"
            else: # significa que não tem limite inferior
                list_range = f"{{{int(bound1)}}}"

            reg_exp += rf"(?P<{name}>([^,]+[,]?){list_range})[,]?"
        
        else:
            reg_exp += rf"(?P<{name}>[^,]+)[,]?"

    reg_exp = re.compile(reg_exp)

    return reg_exp


def collect_data(reg_exp, lines):
    data = list()
    
    for line in lines[1:]:
        matches = reg_exp.finditer(line.strip())

        for m in matches:
            data.append(m.groupdict())

    return data


def insert_lists_and_aggr_functs(data, header, size_bounds, aggr_functions):
    for entry in data:
        for name in header:
            if name in size_bounds:  # se for uma lista
                entry[name] = [int(num) for num in re.findall(r"\d+", entry[name])]
            
                if name in aggr_functions:  # se houver funçao de agregaçao aplicada a essa lista
                    aggr_funct = aggr_functions[name]
                
                    if aggr_funct == "sum":
                        entry[name] = sum(entry[name])
                
                    elif aggr_funct == "media":
                        entry[name] = mean(entry[name])
    
    return data


def main():
    csv_file = "csv/alunos5.csv"
    json_file = "json/alunos5.json"

    with open(csv_file) as f:
        lines = f.readlines()

    header, size_bounds, aggr_functions = get_header_info(lines[0].strip())
    reg_exp = make_reg_exp(header, size_bounds, aggr_functions)
    data = collect_data(reg_exp, lines)
    data = insert_lists_and_aggr_functs(data, header, size_bounds, aggr_functions)

    with open(json_file, "w") as f:
        json.dump(data, f, indent=len(header), ensure_ascii=False)


if __name__ == "__main__":
    main()