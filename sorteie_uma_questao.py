import random
def sorteia_questao (questao,opcao):
    if opcao in questao:
        questoes_1 = questao[opcao]
        dado = random.randint(0,len(questoes_1)-1)       
        return questoes_1[dado]
    else:
        return None