def transforma_base(questoes):
    resultado = {}

    for questao in questoes:
        nivel = questao['nivel']

        if nivel in resultado:
            resultado[nivel].append(questao)

        else:
            resultado[nivel] = [questao]
            
    return resultado