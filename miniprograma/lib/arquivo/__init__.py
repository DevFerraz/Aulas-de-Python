import time

from miniprograma.lib.interface import *


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt') # O parâmetro 'rt' é read text, e tenta ler o arquivo.
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+') # O parâmetro 'wt' é write text e o '+' cria um novo arquivo de texto.
        a.close()
    except Exception as error:
        print(f'Houve um erro na criação do arquivo! Erro {error}')
    else:
        print(f'Arquivo {nome} criado com sucesso! ')


def lerArquivo(arq):
    try:
        a = open(arq, 'rt')
    except Exception as error:
        print(f'Erro {error} ao ler o arquivo.')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'Nome: {dado[0]:<20} Código: {dado[1]:>3}')
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', codigo=0):
    try:
        a = open(arq, 'at') # A função 'at' é de append text, para incluir novos textos.
    except Exception as error:
        print(f'Houve um erro {error} na abertura do arquivo! ')
    else:
        try:
            a.write(f'{nome};{codigo}\n')
        except Exception as error1:
            print(f'Houve um erro {error1} na hora de cadastrar os dados')
        else:
            print(f'Novo registro de {nome} adicionado com sucesso! ')
            time.sleep(1.5)
        finally:
            a.close()


def pacienteId(arq, num):
    try:
        a = open(arq, 'rt')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            idDaVez = int(dado[1])
            if idDaVez == num:
                print(f'Com o código \033[32m{dado[1]}\033[m encontramos o paciente \033[32m{dado[0]:<20}\033[m')
                return
        print(f'Não foi encontrado nenhum paciente com código {num}')
        a.close()
    except Exception as error2:
        print(f'Houve um erro {error2} na sua solicitação. ')