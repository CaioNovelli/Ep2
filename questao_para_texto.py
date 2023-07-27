def questao_para_texto(quest, numero):
    opcoes = quest['opcoes']
    titulo = quest['titulo']
    nivel = quest['nivel']
    final = f"----------------------------------------\nQUESTAO {numero}\n\n{titulo}\n\nRESPOSTAS:\n"
    for x in opcoes:
        resposta = opcoes[x]
        final += f"{x}: {resposta}\n"
    return final