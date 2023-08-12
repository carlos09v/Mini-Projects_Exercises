import sqlite3 as conector

conexao = conector.connect('./escola.db')
cursor = conexao.cursor()

def menu():
    print('''\n------ MENU ------
1 - Criar tabelas (tipo_curso, titulo, instituicao, tipo_disciplina);
2 - Criar...
3 - [ Sair ]''')

    opc = int(input('Qual a opção? '))
    while opc < 1 or opc > 3:
        print('Opção Inválida ! Digite um número de 1 a 3 :)')
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
            print('''=> 1 - Criar Tipo de curso
=> 2 - Criar Titulo
=> 3 - Criar Instituição
=> 4 - Criar Tipo de Disciplina
=> 5 - [ Voltar ]
            ''')

            opcCreate = int(input('Qual a opção? '))
            while opcCreate < 1 or opcCreate > 5:
                print('Opção Inválida ! Digite um número entre 1 e 5 :)')
                opcCreate = int(input('Qual a opção? '))

            if check_tables():
                match opcCreate:
                    case 1:
                        insertData('tipo_curso')
                        main()
                    case 2:
                        insertData('titulo')
                        main()
                    case 3:
                        insertData('instituicao')
                        main()
                    case 4:
                        insertData('tipo_disciplina')
                        main()
                    case 5:
                        main()
            else:
                print('=> Alerta: As tabelas precisam ser criadas primeiro!')
                main()
        case 3:
            conexao.close() # Fechar DB
            print('Encerrado...')
        case _:
            print('Erro total !!!')

def create_dbs():
    try:
        comando = '''CREATE TABLE IF NOT EXISTS titulo (
                        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
                        tx_descricao VARCHAR(45) NOT NULL);'''
        cursor.execute(comando)

        comando = '''CREATE TABLE IF NOT EXISTS instituicao (
                        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
                        tx_sigla VARCHAR(45) NOT NULL, 
                        tx_descricao VARCHAR(255) NOT NULL);'''
        cursor.execute(comando)

        comando = '''CREATE TABLE IF NOT EXISTS tipo_curso (
                        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
                        tx_descricao VARCHAR(45) NOT NULL);'''
        cursor.execute(comando)

        comando = '''CREATE TABLE IF NOT EXISTS tipo_disciplina (
                        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
                        tx_descricao VARCHAR(45) NOT NULL);'''
        cursor.execute(comando)

        conexao.commit()
        print('Tabelas criadas com sucesso!')
    except conector.Error as e:
        print('Erro de banco de dados: ', e)

# Verificar se o ID existe
def check_id(id):
    try:
        comando = "SELECT * FROM Marca WHERE id=:id"

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

# Verificar se as tabelas existem
def check_tables():
    try:
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='tipo_curso'")
        existe_tipo_curso = cursor.fetchone()

        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='titulo'")
        existe_titulo = cursor.fetchone()

        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='instituicao'")
        existe_instituicao = cursor.fetchone()

        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='tipo_disciplina'")
        existe_tipo_disciplina = cursor.fetchone()

        if existe_tipo_curso and existe_titulo and existe_instituicao and existe_tipo_disciplina:
            return True
        else:
            return False

        # cursor.commit() # Não é necessário commit em SELECT
    except conector.Error as e:
        print('Erro de banco de dados: ', e)
    except conector.OperationalError:
        print('Ocorreu um erro operacional no banco de dados!') # Essa exceção ocorre quando ocorre um erro operacional no banco de dados, como uma consulta inválida ou um nome de tabela incorreto.

def insertData(table):
    match table:
        case 'tipo_curso':
            try:
                data = str(input('Escreva o tipo do curso: ')).strip()
                comando = f"INSERT INTO {table}(tx_descricao) VALUES(?)"
                cursor.execute(comando, (data, ))

                conexao.commit()
                print(f'=> {data} foi inserido na tabela {table} com sucesso!')
            except conector.Error as e:
                print('Erro de banco de dados: ', e)
            except conector.IntegrityError:
                print(
                    'Ocorreu um erro de integridade dos dados!')  # Ocorre quando há violação de integridade dos dados, como tentar inserir um registro com uma chave primária já existente ou violar uma restrição de unicidade.
        case 'titulo':
            try:
                data = str(input('Qual o titulo do curso: ')).strip()
                comando = f"INSERT INTO {table}(tx_descricao) VALUES(?)"
                cursor.execute(comando, (data, ))

                conexao.commit()
                print(f'=> {data} foi inserido na tabela {table} com sucesso!')
            except conector.Error as e:
                print('Erro de banco de dados: ', e)
            except conector.IntegrityError:
                print(
                    'Ocorreu um erro de integridade dos dados!')  # Ocorre quando há violação de integridade dos dados, como tentar inserir um registro com uma chave primária já existente ou violar uma restrição de unicidade.
        case 'instituicao':
            try:
                dataSigla = str(input('Qual a sigla da Instituição: ')).strip()
                data_Descri = str(input('Fale sobre a Instituição: ')).strip()
                comando = f"INSERT INTO {table}(tx_sigla, tx_descricao) VALUES(?, ?)"
                cursor.execute(comando, (dataSigla, data_Descri))

                conexao.commit()
                print(f'=> [{dataSigla}/ {data_Descri}] foram inseridos na tabela {table} com sucesso!')
            except conector.Error as e:
                print('Erro de banco de dados: ', e)
            except conector.IntegrityError:
                print(
                    'Ocorreu um erro de integridade dos dados!')  # Ocorre quando há violação de integridade dos dados, como tentar inserir um registro com uma chave primária já existente ou violar uma restrição de unicidade.
        case 'tipo_disciplina':
            try:
                data = str(input('Qual o Tipo da Disciplina? ')).strip()
                comando = f"INSERT INTO {table}(tx_descricao) VALUES(?)"
                cursor.execute(comando, (data, ))

                conexao.commit()
                print(f'=> {data} foi inserido na tabela {table} com sucesso!')
            except conector.Error as e:
                print('Erro de banco de dados: ', e)
            except conector.IntegrityError:
                print(
                    'Ocorreu um erro de integridade dos dados!')  # Ocorre quando há violação de integridade dos dados, como tentar inserir um registro com uma chave primária já existente ou violar uma restrição de unicidade.


if __name__ == '__main__':
    main()