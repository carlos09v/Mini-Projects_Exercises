import sqlite3 as conector

conexao = conector.connect('./carros.db')
cursor = conexao.cursor()


def create_table():
    try:
        comando = '''CREATE TABLE IF NOT EXISTS Marca (
                        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
                        nome TEXT NOT NULL, 
                        sigla VARCHAR(3) NOT NULL)'''

        cursor.execute(comando)
        conexao.commit()
    except conector.Error as e:
        print('Erro de banco de dados: ', e)

    finally:
        cursor.close()
        conexao.close()


def insersao_02():
    try:
        comando = "INSERT INTO Marca(nome, sigla) VALUES(:nome, :sigla)"

        cursor.execute(comando, {
            "nome": "Fiat",
            "sigla": "FT"
        })

        conexao.commit()
        print('Fiat/FT inserido com sucesso!')
    except conector.Error as e:
        print('Erro de banco de dados: ', e)
    except conector.IntegrityError:
        print('Ocorreu um erro de integridade dos dados!') # Ocorre quando há violação de integridade dos dados, como tentar inserir um registro com uma chave primária já existente ou violar uma restrição de unicidade.

    finally:
        cursor.close()
        conexao.close()


def insersao_03(nome, sigla):
    try:
        comando = f"INSERT INTO Marca(nome, sigla) VALUES(?, ?)"
        cursor.execute(comando, (nome, sigla))

        conexao.commit()
        print(f'{nome}/{sigla} inserido com sucesso!')
    except conector.Error as e:
        print('Erro de banco de dados: ', e)
    except conector.IntegrityError:
        print('Ocorreu um erro de integridade dos dados!') # Ocorre quando há violação de integridade dos dados, como tentar inserir um registro com uma chave primária já existente ou violar uma restrição de unicidade.

    finally:
        cursor.close()
        conexao.close()


def updateName(id, value):
    try:
        if not id_existe(id):
            return print('Este ID não existe :(')

        comando = "UPDATE Marca SET nome = :nome WHERE id=:id"

        cursor.execute(comando, {
            "nome": value,
            "id": id
        })

        conexao.commit()
        print('Dados atualizados com sucesso!')
    except conector.Error as e:
        print('Erro de banco de dados: ', e)

    finally:
        cursor.close()
        conexao.close()


def select():
    try:
        comando = "SELECT * FROM Marca"
        cursor.execute(comando)

        registros = cursor.fetchall()
        # print(type(registros))

        for r in registros:
            print("Tipo: ", type(r), " - Conteudo: ", r)
            # print(r[1])

        # cursor.commit() # Não é necessário commit em SELECT
    except conector.Error as e:
        print('Erro de banco de dados: ', e)
    except conector.OperationalError:
        print('Ocorreu um erro operacional no banco de dados!') # Essa exceção ocorre quando ocorre um erro operacional no banco de dados, como uma consulta inválida ou um nome de tabela incorreto.

    finally:
        cursor.close()
        conexao.close()


def delete(id):
    try:
        if not id_existe(id):
            return print('Este ID não existe :(')

        comando = "DELETE FROM Marca WHERE id=:id"
        cursor.execute(comando, {
            "id": id
        })

        conexao.commit()
        print(f'ID {id} deletado com sucesso!')
    except conector.Error as e:
        print('Erro de banco de dados: ', e)

    finally:
        cursor.close()
        conexao.close()


# Verificar se o ID existe
def id_existe(id):
    try:
        comando = "SELECT * FROM Marca WHERE id=:id"

        cursor.execute(comando, {
            "id": id
        })
        resultado = cursor.fetchone()

        if resultado:
            return True
        else:
            return False

        # cursor.commit() # Não é necessário commit em SELECT
    except conector.Error as e:
        print('Erro de banco de dados: ', e)
    except conector.OperationalError:
        print('Ocorreu um erro operacional no banco de dados!') # Essa exceção ocorre quando ocorre um erro operacional no banco de dados, como uma consulta inválida ou um nome de tabela incorreto.

# ---- CRUD => [Create, Read, Update, Delete]
# create_table()
# insersao_02()
# insersao_03('Gol', 'Yamaha')
# updateName(3, 'Motinha')
# select()
# delete(3)