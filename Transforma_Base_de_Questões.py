def transforma_base(questôes):
    resultado = {}

    for questao in questôes:
        nivel = questao['nivel']

        if nivel in resultado:
            resultado[nivel].append(questao)

        else:
            resultado[nivel] = [questao]
            
    return resultado