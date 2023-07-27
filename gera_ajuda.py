from random import randint, choice

def gera_ajuda(questao):
    incorretas = []
    items = list(questao['opcoes'].items())
    i = 0
    while i < len(items):
        x, quest_incorreta = items[i]
        if x != questao['correta']:
            incorretas.append(quest_incorreta)
        i += 1
    qnt = randint(1,2)
    if qnt == 1:
        return f'DICA:\nOpções certamente erradas: {choice(incorretas)}'
    else:
        return f'DICA:\nOpções certamente erradas: {choice(incorretas)} | {choice(incorretas)}'