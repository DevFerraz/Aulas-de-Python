from miniprograma.lib.interface import *
import time
from miniprograma.lib.arquivo import *

arq = 'lista_de_pacientes.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)
while True:
    resposta = menu(['Cadastrar Um Novo Paciente', 'Listar Pacientes', 'Buscar Paciente via ID', 'Sair do Sistema'])
    if resposta == 1:
        cabecalho('NOVO CADASTRO')
        time.sleep(1.5)
        nome = str(input('Digite o nome do paciente: '))
        codigo = leiaInt('Digite o ID do paciente: ')
        cadastrar(arq, nome, codigo)
    elif resposta == 2:
        lerArquivo(arq)
        time.sleep(1.5)
    elif resposta == 3:
        validacao = leiaInt('Digite o número do ID do paciente: ')
        pacienteId(validacao)
        time.sleep(1.5)
    elif resposta == 4:
        cabecalho('\033[36mSaindo do sistema... Até logo! \033[m')
        time.sleep(1)
        break
    else:
        print('\033[31mOpção inválida. Tente novamente! \033[m')
        time.sleep(1.5)
