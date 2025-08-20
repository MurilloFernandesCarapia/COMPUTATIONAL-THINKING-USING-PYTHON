try:
    arquivo = open('meu_arquivo.txt' , 'r')
    conteudo = arquivo.read()
    print('Arquivo foi lido com sucesso!')

except FileNotFoundError:
    print('O arquivo não foi encontrado!')

else:
    print('Não ocorreu nenhum erro!') 

finally:
    arquivo.close()
    print('Arquivo fechado!')      