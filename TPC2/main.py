def main():
    str_num = "0"
    sum = 0
    state = True

    while inp := input("> ").lower():
    
        for ind, char in enumerate(inp):
            last_pos = len(list(enumerate(inp)))-1

            if state:
                if char.isdigit() and ind != last_pos:
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
            
            if char == "=":
                print(f"Soma: {sum}")


if __name__ == '__main__':
    main()