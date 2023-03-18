import re
import sys

state = {
    "on": False,
    "balance": 0
}


def get_balance():
    euros = state["balance"]//100
    cents = state["balance"]%100

    return f"saldo = {euros}e{cents}c"


def parse_coins(coins):
    invalid = list()

    for coin in coins:
        if match := re.match(r"(\d+)c", coin):
            if (value := int(match.group(1))) in [1,2,5,10,20,50]:
                state["balance"] += value
            
            else: invalid += [coin]
        
        elif match := re.match(r"(\d+)e", coin):
            if (value := int(match.group(1))) in [1,2]:
                state["balance"] += value*100
            
            else: invalid += [coin]
            
        else:
            invalid += [coin]

    msg = 'maq: "'
    for coin in invalid:
        msg += f"{coin} - moeda inválida; "
    msg += f'{get_balance()}"'

    return msg


def get_change():
    coins = {
        1: 0, 
        2: 0,
        5: 0,
        10: 0,
        20: 0,
        50: 0,
        100: 0,
        200: 0 
    }

    for coin in [200, 100, 50, 20, 10, 5, 2, 1]:
        while state["balance"] >= 0 and state["balance"] // coin != 0:
            qtt = state["balance"] // coin
            state["balance"] -= qtt*coin
            coins[coin] += 1
    
    return f"{coins[200]}x2e, {coins[100]}x1e, {coins[50]}x50c, {coins[20]}x20c, {coins[10]}x10c, {coins[5]}x5c, {coins[2]}x2c, {coins[1]}x1c"


def call(num):
    if state["on"]:
        if not re.match(r"(\d{9}|00\d{9})$", num):
            msg = 'maq: "Número inválido!"'

        elif re.match(r"601|641", num):
            msg = 'maq: "Esse número não é permitido neste telefone. Queira discar novo número!"'

        elif re.match(r"00", num):
            if state["balance"] >= 150:
                state["balance"] -= 150
                msg = f'maq: "{get_balance()}"'
            else:
                msg = 'maq: "Saldo insuficiente!"'

        elif re.match(r"2", num):
            if state["balance"] >= 25:
                state["balance"] -= 25
                msg = f'maq: "{get_balance()}"'
            else:
                msg = 'maq: "Saldo insuficiente!"'
        
        elif re.match(r"800", num):
            msg = f'maq: "{get_balance()}"'

        elif re.match(r"808", num):
            if state["balance"] >= 10:
                state["balance"] -= 10
                msg = f'maq: "{get_balance()}"'
            else:
                msg = 'maq: "Saldo insuficiente!"'
    
    else:
        msg = 'maq: "O telefone não está em uso!"'
    
    return msg
    

def start():
    if state["on"]:
        msg = 'maq: "O telefone já está em uso!"'
    
    else:
        state["on"] = True
        msg = 'maq: "Introduza moedas."'
    
    return msg


def stop():
    if not state["on"]:
        msg = 'maq: "O telefone não está em uso!"'
    
    else:
        state["on"] = False
        state["balance"] = 0
        msg = f'maq: "troco= {get_change()}; Volte sempre!"'
    
    return msg


def cancel():
    if not state["on"]:
        msg = 'maq: "O telefone não está em uso!"'
    
    else:
        state["balance"] = 0
        msg = f'maq: "troco= {get_change()}; Volte sempre!"'
    
    return msg


def main():
    for line in sys.stdin:
        line = line[:-1]

        if re.match(r"LEVANTAR", line):
            print(start())

        elif re.match(r"POUSAR", line):
            print(stop())

        elif re.match(r"MOEDA", line):
            print(parse_coins(re.split(r"\s*,\s*", line[6:-1])))

        elif re.match(r"T=", line):
            print(call(line[2:]))

        elif re.match(r"ABORTAR", line):
            print(cancel())


if __name__ == "__main__":
    main()
