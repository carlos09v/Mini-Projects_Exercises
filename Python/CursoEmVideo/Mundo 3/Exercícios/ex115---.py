from Módulos_e_Pacotes.ex115.arquivo import * # Tudo
from time import sleep
arq = 'cursoemvideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu('Ver Pessoas Cadastradas','Cadastrar nova Pessoa','Sair do Programa')
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo!
        lerArquivo(arq)
    elif resposta == 2:
        # Opção de cadastrar uma nova pessoa.
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq,nome,idade)
    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo!'),sleep(2)
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m'),sleep(1)
