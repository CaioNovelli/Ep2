def valida_questao (questao):
    opcoes = ['A', 'B', 'C', 'D']
    erros = {}
    chaves = ['titulo', 'nivel', 'opcoes', 'correta']
    for chave in chaves:
        if chave not in questao:
            erros[chave] = 'nao_encontrado'
        if 'correta' not in questao:
            erros['correta'] = 'nao_encontrado'
        else:
            if  questao['correta'] not in opcoes:
                erros['correta'] = 'valor_errado'
        if len(questao) != 4:
            erros['outro'] = 'numero_chaves_invalido'
        if 'titulo' in questao:
            if len(questao['titulo'].strip()) == 0:
                erros['titulo'] = 'vazio'
        if 'nivel' in questao:
            nivel = questao['nivel']
            if nivel != 'facil' and nivel != 'medio' and nivel != 'dificil':
                erros['nivel'] = 'valor_errado'
        if 'opcoes' in questao:
            if len(questao['opcoes']) != 4:
                erros['opcoes'] = 'tamanho_invalido'
            else:
                dicionario = {}
                if 'A' not in questao['opcoes'] or 'B' not in questao['opcoes'] or 'C' not in questao['opcoes'] or 'D' not in questao['opcoes']:
                    erros['opcoes'] = 'chave_invalida_ou_nao_encontrada'               
                else:
                    if len(questao['opcoes']['A'].strip()) == 0:
                        dicionario['A'] = 'vazia'
                    if len(questao['opcoes']['B'].strip()) == 0:
                        dicionario['B'] = 'vazia'
                    if len(questao['opcoes']['C'].strip()) == 0:
                        dicionario['C'] = 'vazia'
                    if len(questao['opcoes']['D'].strip()) == 0:
                        dicionario['D'] = 'vazia'
                    if len(dicionario) > 0:
                        erros['opcoes'] = dicionario                       
    return erros
def valida_questoes(questoes: list) -> list:
    resultado = []
    for questao in questoes:
        erros = valida_questao(questao)
        if not erros:
            resultado.append({})
        else:
            resultado.append(erros)       
    return resultado