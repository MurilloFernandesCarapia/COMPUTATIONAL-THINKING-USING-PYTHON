''''
Escreva um programa em Python que, para uma quantidade de alunos especificada, colete as notas de cada aluno e exiba um resumo da turma

O programa deve ter (requisitos):
- função coletar_notas() - pede ao usuário para digitar umma série de notas em uma única linha. O programa deve converter as notas para numérico (float) e retorná-las em uma lista

- função preencher_turma(qtde_alunos) - recebe por parâmetro a qtde de alunos , para cada aluno, utiliza a função coletar_notas() para preencher uma lista de notas de cada aluno 

- função calcular_media(aluno) - recebe por parâmetro a lista de notas de um aluno e retorna 


'''

def coletar_notas():
    notas = input().split()
    for i in range (len(notas)):
        notas[i] = float(notas[i]) #casting para float
    return notas

def preencher_turma(qtde_alunos):
    turma = []
    for i in range(qtde_alunos):
        print(f'{i+1}º aluno ', end=' ')
        aluno = coletar_notas()
        turma.append(aluno)
    return turma

def calcular_media(notas_aluno):
    soma = 0
    for nota in notas_aluno:
        soma+=nota #acumulando 

    return soma/len(notas_aluno)

def resumo_turma(turma):
    for notas_aluno in turma:
        media = calcular_media(notas_aluno)
        print(f'Notas: {notas_aluno} | Média: {media:.2f}')

def main():
    qtde_alunos = int(input('Qtde Alunos: '))
    turma = preencher_turma(qtde_alunos)