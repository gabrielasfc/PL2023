def main():
    str_num = ""
    soma = 0
    state = True

    while inp:= input("> ").lower():
        for ind, char in enumerate(inp):
            if state:
                if char.isdigit():
                    str_num += char
                    
                elif inp[ind : ind+3] == "off":
                    state = False
                    
                elif len(str_num) > 0:
                    soma += int(str_num)
                    str_num = ""
            
            elif inp[ind : ind+2] == "on":
                state = True

            if char == "=":
                print(f"Soma: {soma}")


if __name__ == '__main__':
    main()