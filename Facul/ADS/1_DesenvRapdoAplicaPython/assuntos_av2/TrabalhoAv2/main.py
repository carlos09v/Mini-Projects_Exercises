import sqlite3 as conector
from random import randint

conexao = conector.connect('./hospital.db')
cursor = conexao.cursor()

# Aluno: Carlos Vinicius

def menu():
    print('''\n========================= MENU =========================
1 - Criar Tabelas [Hospital, Médico, Enfeirmeira, Paciente, Especialidade, Telefone];
2 - Cadastrar...
3 - Relatórios...
4 - Deletar registro...
5 - [ Sair ]''')

    opc = int(input('Qual a opção? '))
    while opc < 1 or opc > 5:
        print('Opção Inválida ! Digite um número de 1 a 5 :)')
        opc = int(input('Qual a opção? '))
    return opc

def main():
    opc = menu()

    match opc:
        case 1:
            if check_tables():
                print('Estas tabelas ja existem/criadas !')
                return main()

            create_dbs()
            main()
        case 2:
            print('''=> 1 - Médico
=> 2 - Paciente
=> 3 - Hospital
=> 4 - Especialidade
=> 5 - Enfermeira
=> 6 - Telefone
=> 7 - [ Voltar ]''')

            opcRegister = int(input('Qual a opção? '))
            while opcRegister < 1 or opc > 7:
                print('Opção Inválida ! Digite um número de 1 a 7 :)')
                opcRegister = int(input('Qual a opção? '))

            if check_tables():
                match opcRegister:
                    case 1:
                        inserirNoDB('Médico')
                        main()
                    case 2:
                        inserirNoDB('Paciente')
                        main()
                    case 3:
                        inserirNoDB('Hospital')
                        main()
                    case 4:
                        inserirNoDB('Especialidade')
                        main()
                    case 5:
                        inserirNoDB('Enfermeira')
                        main()
                    case 6:
                        inserirNoDB('Telefone')
                        main()
                    case 7:
                        main()
            else:
                print('=> Alerta: As tabelas precisam ser criadas primeiro! [Dica: Opção 1]')
                main()
        case 3:
            print('''=> 1 - Listar todos os médicos, pacientes e hospitais
=> 2 - Listar pacientes que moram no Centro de Aracaju
=> 3 - Listar TUDO !
=> 4 - [ Voltar ]''')

            opcRelatorios = int(input('Qual a opção? '))
            while opcRelatorios < 1 or opc > 3:
                print('Opção Inválida ! Digite um número de 1 a 3 :)')
                opcRelatorios = int(input('Qual a opção? '))

            if check_tables():
                if opcRelatorios != 4:
                    show_relatorio(opcRelatorios)
                    main()
                main()
            else:
                print('=> Alerta: As tabelas precisam ser criadas primeiro! [Dica: Opção 1]')
                main()
        case 4:
            print('''=> 1 - Médico
=> 2 - Paciente
=> 3 - Hospital
=> 4 - Especialidade
=> 5 - Enfermeira
=> 6 - Telefone
=> 7 - [ Voltar ]''')

            opcDelete = int(input('Qual a opção? '))
            while opcDelete < 1 or opc > 7:
                print('Opção Inválida ! Digite um número de 1 a 7 :)')
                opcDelete = int(input('Qual a opção? '))

            if check_tables():
                id = int(input('Qual o ID que deseja apagar? '))
                match opcDelete:
                    case 1:
                        deleteById('Médico', id)
                        main()
                    case 2:
                        deleteById('Paciente', id)
                        main()
                    case 3:
                        deleteById('Hospital', id)
                        main()
                    case 4:
                        deleteById('Especialidade', id)
                        main()
                    case 5:
                        deleteById('Enfermeira', id)
                        main()
                    case 6:
                        deleteById('Telefone', id)
                        main()
                    case 7:
                        main()
            else:
                print('=> Alerta: As tabelas precisam ser criadas primeiro! [Dica: Opção 1]')
                main()
        case 5:
            conexao.close()
            print('Encerrado...')
            

# Criar tabelas
def create_dbs():
    try:
        comando = '''CREATE TABLE IF NOT EXISTS Hospital (
                        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
                        nome VARCHAR(30) NOT NULL,
                        endereco VARCHAR(125) NOT NULL,
                        cep VARCHAR(9) NOT NULL,
                        telefone VARCHAR(13) NOT NULL UNIQUE);'''
        cursor.execute(comando)

        comando = '''CREATE TABLE IF NOT EXISTS Médico (
                        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
                        cpf VARCHAR(14) NOT NULL UNIQUE,
                        crm VARCHAR(6) NOT NULL UNIQUE,
                        nome VARCHAR(50) NOT NULL,
                        endereco VARCHAR(125) NOT NULL);'''
        cursor.execute(comando)

        comando = '''CREATE TABLE IF NOT EXISTS Paciente (
                        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
                        cpf VARCHAR(14) NOT NULL UNIQUE,
                        rg VARCHAR(12) NOT NULL UNIQUE,
                        nome VARCHAR(50) NOT NULL,
                        cidade VARCHAR(20) NOT NULL,
                        endereco VARCHAR(125) NOT NULL);'''
        cursor.execute(comando)

        comando = '''CREATE TABLE IF NOT EXISTS Enfermeira (
                        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
                        cpf VARCHAR(14) NOT NULL UNIQUE,
                        nome VARCHAR(50) NOT NULL,
                        endereco VARCHAR(125) NOT NULL);'''
        cursor.execute(comando)

        comando = '''CREATE TABLE IF NOT EXISTS Especialidade (
                        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
                        tx_especialidade VARCHAR(50) NOT NULL);'''
        cursor.execute(comando)

        comando = '''CREATE TABLE IF NOT EXISTS Telefone (
                        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
                        tx_telefone VARCHAR(12) NOT NULL);'''
        cursor.execute(comando)

        conexao.commit()
        print('Tabelas criadas com sucesso!')
    except conector.Error as e:
        print('Erro de banco de dados: ', e)

# Inserir Dados no DB
def inserirNoDB(table):
    match table:
        case 'Médico':
            try:
                crm = [randint(0, 9) for _ in range(6)] # gerar CRM aleatório
                crm_formatado = ''.join(map(str, crm))
                cpf = [randint(0, 9) for _ in range(11)] # gerar CPF aleatório
                cpf_formatado = '{}{}{}.{}{}{}.{}{}{}-{}{}'.format(*cpf)

                nome = str(input('Nome: ')).strip()
                endereco = str(input('Endereço: ')).strip()
                comando = f"INSERT INTO {table}(nome, crm, cpf, endereco) VALUES(?, ?, ?, ?)"
                cursor.execute(comando, (nome, crm_formatado, cpf_formatado, endereco))

                conexao.commit()
                print('Obs: O CPF e o CRM foram gerados automaticamente')
                print(f'=> [{nome} - {crm_formatado} - {cpf_formatado} - {endereco}] foi inserido na tabela {table} com sucesso!')
            except conector.Error as e:
                print('Erro de banco de dados: ', e)
            except conector.IntegrityError:
                print('Ocorreu um erro de integridade dos dados!')  # Ocorre quando há violação de integridade dos dados, como tentar inserir um registro com uma chave primária já existente ou violar uma restrição de unicidade.
        case 'Hospital':
            try:
                ddd_telefone = [randint(0, 9), randint(0, 9)] # DDD aleatório
                ddd_telefone.extend([randint(0, 9) for _ in range(8)])  # gerar Telefone aleatório
                ddd_telefone_formatado = '({}{})9{}{}{}{}-{}{}{}{}'.format(*ddd_telefone)
                cep = [randint(0, 9) for _ in range(8)]  # gerar CEP aleatório
                cep_formatado = '{}{}{}{}{}-{}{}{}'.format(*cep)

                nome = str(input('Nome: ')).strip()
                endereco = str(input('Endereço: ')).strip()
                comando = f"INSERT INTO {table}(nome, cep, telefone, endereco) VALUES(?, ?, ?, ?)"
                cursor.execute(comando, (nome, cep_formatado, ddd_telefone_formatado, endereco))

                conexao.commit()
                print('Obs: O Telefone e o CEP foram gerados automaticamente')
                print(f'=> [{nome} - {ddd_telefone_formatado} - {cep_formatado} - {endereco}] foi inserido na tabela {table} com sucesso!')
            except conector.Error as e:
                print('Erro de banco de dados: ', e)
            except conector.IntegrityError:
                print('Ocorreu um erro de integridade dos dados!')
        case 'Paciente':
            try:
                cpf = [randint(0, 9) for _ in range(11)]  # gerar CPF aleatório
                cpf_formatado = '{}{}{}.{}{}{}.{}{}{}-{}{}'.format(*cpf)
                rg = [randint(0, 9) for _ in range(9)]  # gerar RG aleatório
                rg_formatado = '{}{}.{}{}{}.{}{}{}-{}'.format(*rg)

                nome = str(input('Nome: ')).strip()
                cidade = str(input('Cidade: ')).strip().upper()
                endereco = str(input('Endereço: ')).strip()
                comando = f"INSERT INTO {table}(nome, cidade, rg, cpf, endereco) VALUES(?, ?, ?, ?, ?)"
                cursor.execute(comando, (nome, cidade, rg_formatado, cpf_formatado, endereco))

                conexao.commit()
                print('Obs: O RG e o CPF foram gerados automaticamente')
                print(f'=> [{nome} - {cidade} - {rg_formatado} - {cpf_formatado} - {endereco}] foi inserido na tabela {table} com sucesso!')
            except conector.Error as e:
                print('Erro de banco de dados: ', e)
            except conector.IntegrityError:
                print('Ocorreu um erro de integridade dos dados!')
        case 'Enfermeira':
            try:
                cpf = [randint(0, 9) for _ in range(11)]  # gerar CPF aleatório
                cpf_formatado = '{}{}{}.{}{}{}.{}{}{}-{}{}'.format(*cpf)

                nome = str(input('Nome: ')).strip()
                endereco = str(input('Endereço: ')).strip()
                comando = f"INSERT INTO {table}(nome, cpf, endereco) VALUES(?, ?, ?)"
                cursor.execute(comando, (nome, cpf_formatado, endereco))

                conexao.commit()
                print('Obs: O CPF foi gerado automaticamente')
                print(f'=> [{nome} - {cpf_formatado} - {endereco}] foi inserido na tabela {table} com sucesso!')
            except conector.Error as e:
                print('Erro de banco de dados: ', e)
            except conector.IntegrityError:
                print('Ocorreu um erro de integridade dos dados!')
        case 'Especialidade':
            try:
                tx_especialidade = str(input('Especialidade: ')).strip()
                comando = f"INSERT INTO {table}(tx_especialidade) VALUES(?)"
                cursor.execute(comando, (tx_especialidade,))

                conexao.commit()
                print(f'=> [{tx_especialidade}] foi inserido na tabela {table} com sucesso!')
            except conector.Error as e:
                print('Erro de banco de dados: ', e)
            except conector.IntegrityError:
                print('Ocorreu um erro de integridade dos dados!')
        case 'Telefone':
            try:
                tx_telefone = str(input('Telefone: ')).strip()
                comando = f"INSERT INTO {table}(tx_telefone) VALUES(?)"
                cursor.execute(comando, (tx_telefone,))

                conexao.commit()
                print(f'=> [{tx_telefone}] foi inserido na tabela {table} com sucesso!')
            except conector.Error as e:
                print('Erro de banco de dados: ', e)
            except conector.IntegrityError:
                print('Ocorreu um erro de integridade dos dados!')


# Verificar se as tabelas existem
def check_tables():
    try:
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Médico'")
        existe_medico = cursor.fetchone()

        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Paciente'")
        existe_paciente = cursor.fetchone()

        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Hospital'")
        existe_hospital = cursor.fetchone()

        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Especialidade'")
        existe_especialidade= cursor.fetchone()

        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Enfermeira'")
        existe_enfermeira = cursor.fetchone()

        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Telefone'")
        existe_telefone = cursor.fetchone()

        if existe_medico and existe_paciente and existe_hospital and existe_especialidade and existe_enfermeira and existe_telefone:
            return True
        else:
            return False

        # cursor.commit() # Não é necessário commit em SELECT
    except conector.Error as e:
        print('Erro de banco de dados: ', e)
    except conector.OperationalError:
        print('Ocorreu um erro operacional no banco de dados!') # Essa exceção ocorre quando ocorre um erro operacional no banco de dados, como uma consulta inválida ou um nome de tabela incorreto.

# Verificar se o ID existe
def check_id(table, id):
    try:
        comando = f"SELECT * FROM {table} WHERE id=:id"

        cursor.execute(comando, {
            "id": id
        })
        result = cursor.fetchone()

        if result:
            return True
        else:
            return False

        # cursor.commit() # Não é necessário commit em SELECT
    except conector.Error as e:
        print('Erro de banco de dados: ', e)
    except conector.OperationalError:
        print('Ocorreu um erro operacional no banco de dados!') # Essa exceção ocorre quando ocorre um erro operacional no banco de dados, como uma consulta inválida ou um nome de tabela incorreto.

# Deletar pelo ID existente
def deleteById(table, id):
    # Verificar ID
    if not check_id(table, id):
        return print('Este ID não existe :(')

    try:
        comando = f"DELETE FROM {table} WHERE id=:id"
        cursor.execute(comando, {
            "id": id
        })

        conexao.commit()
        print(f'=> ID {id} da tabela {table} foi deletado com sucesso!')
    except conector.Error as e:
        print('Erro de banco de dados: ', e)


# Mostrar a Lista/Relatórios
def show_relatorio(opc):
    match opc:
        case 1:
            try:
                tabelas = ['Médico', 'Hospital', 'Paciente']  # Lista de nomes de tabelas

                resultados_combinados = []

                for tabela in tabelas:
                    comando = f'SELECT * FROM {tabela}'
                    cursor.execute(comando)
                    resultados = cursor.fetchall()

                    for resultado in resultados:
                        resultados_combinados.append((tabela,) + resultado)

                # Imprimir os resultados combinados
                for tabela, *registro in resultados_combinados:
                    print(f"Tabela: {tabela}")
                    print(registro)

                # cursor.commit() # Não é necessário commit em SELECT
            except conector.Error as e:
                print('Erro de banco de dados: ', e)
            except conector.OperationalError:
                print('Ocorreu um erro operacional no banco de dados!')  # Essa exceção ocorre quando ocorre um erro operacional no banco de dados, como uma consulta inválida ou um nome de tabela incorreto.
        case 2:
            try:
                comando = "SELECT * FROM Paciente WHERE cidade='ARACAJU'"
                cursor.execute(comando)

                resultados = cursor.fetchall()
                for result in resultados:
                    print(result)
                # cursor.commit() # Não é necessário commit em SELECT
            except conector.Error as e:
                print('Erro de banco de dados: ', e)
            except conector.OperationalError:
                print('Ocorreu um erro operacional no banco de dados!')  # Essa exceção ocorre quando ocorre um erro operacional no banco de dados, como uma consulta inválida ou um nome de tabela incorreto.
        case 3:
            try:
                tabelas = ['Médico', 'Hospital', 'Paciente', 'Enfermeira', 'Especialidade', 'Telefone']  # Lista de nomes de tabelas

                resultados_combinados = []

                for tabela in tabelas:
                    comando = f'SELECT * FROM {tabela}'
                    cursor.execute(comando)
                    resultados = cursor.fetchall()

                    for resultado in resultados:
                        resultados_combinados.append((tabela,) + resultado)

                # Imprimir os resultados combinados
                for tabela, *registro in resultados_combinados:
                    print(f"Tabela: {tabela}")
                    print(registro)

                # cursor.commit() # Não é necessário commit em SELECT
            except conector.Error as e:
                print('Erro de banco de dados: ', e)
            except conector.OperationalError:
                print('Ocorreu um erro operacional no banco de dados!')  # Essa exceção ocorre quando ocorre um erro operacional no banco de dados, como uma consulta inválida ou um nome de tabela incorreto.

if __name__ == '__main__':
    main()