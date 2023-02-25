def main():
    str_num = ""
    sum = 0
    state = True

    while inp:= input("> ").lower():
        for ind, char in enumerate(inp):
            if char == "=":
                print(f"Soma: {sum}")

            elif state:
                if char.isdigit() and ind != len(list(enumerate(inp)))-1:
                    str_num += char
                    
                elif inp[ind : ind+3] == "off":
                    state = False
                
                else:
                    if char.isdigit():
                        str_num += char
                
                    sum += int(str_num)
                    str_num = "0"

            elif inp[ind : ind+2] == "on":
                state = True


if __name__ == '__main__':
    main()