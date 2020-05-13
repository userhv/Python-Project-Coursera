import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))
    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    soma = 0
    for i in range(0,6):
        soma = soma + abs(as_a[i]- as_b[i])
    
    grauSimilaridade = soma/6
    if grauSimilaridade < 0:
        grauSimilaridade = grauSimilaridade *(-1)
    
    return grauSimilaridade

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    sentenca = separa_sentencas(texto)
    fraseNova = []
    palavraNova = []
    somaSentenca = 0 ; somaFrases = 0 ; somaPalavras = 0
    for i in sentenca:
        somaSentenca += len(i)
        frases = separa_frases(i)
        for j in frases:
            fraseNova.append(j)
    
    for j in fraseNova:
        somaFrases += len(j)
        palavra = separa_palavras(j)
        
        for y in palavra:
            palavraNova.append(y)

    for y in palavraNova:
        somaPalavras  = somaPalavras  + len(y) 
    
    tamMedioPalavras = somaPalavras / len(palavraNova)
    typeToken = n_palavras_diferentes(palavraNova) / len(palavraNova)
    hapexLegomana = (n_palavras_unicas(palavraNova)) / len(palavraNova)
    tamMedioSentenca = somaSentenca / len(sentenca)
    complexidadeSentanca = len(fraseNova) / len(sentenca)
    tamMedioFrase = somaFrases / len(fraseNova)
    
    assinatura = [tamMedioPalavras,typeToken,hapexLegomana,tamMedioSentenca, complexidadeSentanca,tamMedioFrase]
       
    return assinatura

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    info = []
    for i in textos:
        assinaturaTexto = calcula_assinatura(i)
        info.append(compara_assinatura(assinaturaTexto,ass_cp))
    
    grauMenor = info[0]
    valorFinal = 1
    for i in range(len(info)):
        if grauMenor < info[i]:
            valorFinal = i
    return valorFinal

def main():
    assinaturaCp = le_assinatura()
    textosLidos = le_textos()
    print("O autor do texto {} está infectado com COH-PIAH".format(avalia_textos(textosLidos,assinaturaCp)))

main()