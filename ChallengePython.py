'''
Grupo: HCBridge
Integrantes: Pedro de Matos, RM: 564184 | Murillo Fernandes Carapia, RM: 564969 | João Vitor Lacerda, RM: 565565
Turma: 1TDSPH

Para fazer o uso do código é necessario da biblioteca oracledb


Agora iremos criar uma função no programa para mostrar os integrantes do grupo
(def integrantes())
 - Nessa definição os todos os integrantes participantes do Grupo no Challenge irá aparecer 

Iremos agora criar uma conexão com o banco de dados para guardar na tabela os nomes das pessoas que marcarem as consultas
def getConnection()
 - Aqui iremos usar o connect do oracledb(con =oracledb.connect) para estabelecer a conexão, dentro da passagem de parametros colocamos as informações para a hospedagem no oracle, como usuario, senha, servidor e etc...

Agora iremos criar uma função para que o código crie uma tabela no banco de dados 

def criar_tabela(con)



'''

import oracledb



def integrantes():
    print ('Você escolheu a função ver integrantes!\n')
    print ('Murillo Fernandes Carapia, RM: 564969\n Pedro De Matos, RM: 564184 \n João Vitor Lacerda, RM: 565565\n\n')
    print ('Pressione ENTER para voltar para o menu...')

#dominio da tabela no banco de dados = 'oracle.fiap.com.br:1521/orcl'
def get_conexao():
    try:
        con = oracledb.connect(usuario = 'rm564969', senha = '210207', host = 'oracle.fiap.com.br', port = '1521',nome_servico = 'ORCL')
        print('A conexão com o Oracle Banco de Dados foi estabelecidade com sucesso!')
    
    except Exception as e:
        print (f'Não foi possível estabelecer uma conexão com o Oracle Banco de dados pelo seguinte motivo: {e}')
    
    return con

def criar_tabela(con):
    cursor = con.cursor() # essa função é utilizada para criar as intruções do SQL

    try:
        sql = """
            CREATE TABLE paciente_hc(
            id number GENERATED ALWAYS AS IDENTITY,
            first_name VARCHAR(30) NOT NULL,
            last_name VARCHAR(30) NOT NULL,
            whatsapp NUMBER(15),
            email VARCHAR(255),
            idade NUMBER(3),
            data_consulta DATE NOT NULL,
            hora_consulta VARCHAR(5),
            especialidade VARCHAR(50),
            status VARCHAR(20) DEFAULT 'Agendada',
            PRIMARY KEY (id)
            );

            
"""


        cursor.execute(sql)
        print (f'Tabela de Pacientes foi criada com sucesso!')

    except oracledb.Error as e:
        print (f'Erro para criar a tabela pelo seguinte motivo: {e}')

def inserir_paciente(first_name, last_name, whatsapp, email, idade, data_consulta, hora_consulta, especialidade, status):
    print('--- Estamos inserindo os Dados do paciente! --- ')
    con = get_conexao()


    if not con: #aqui estamos validando a conexão com o Oracle 

        return
    
    try:
        cursor = con.cursor()
        sql = """
            INSERT INTO paciente_hc (first_name, last_name, whatsapp, email, idade, data_consulta, hora_consulta, especialidade, status)
            VALUES (:first_name, :last_name, :whatsapp, :email, :idade, :data_consulta, :hora_consulta, :especialidade, :status)
        """

        cursor.execute(sql, {
            'first_name' : first_name,
            'last_name' : last_name,
            'whatsapp' : whatsapp,
            'email' : email,
            'idade' : idade,
            'data_consulta' : data_consulta,
            'hora_consulta' : hora_consulta,
            'especialidade' : especialidade,
            'status' : status

        })

        con.commit()
        print(f'Paciente {first_name} {last_name} adicionado com sucesso na tabela de pacientes!')

    except oracledb.Error as e:
        print (f'Erro ao inserir o paciente na consulta! {e} \n')
        con.rollback()

    finally:
        if con:
            con.close()

def listar_pacientes():
    print('Estamos listando as consultas marcadas e os pacientes!')
    con = get_conexao()

    if not con:
        return
    
    try:
        cursor = con.cursor()
        sql = """
            SELECT id, first_name, last_name, whatsapp, email, idade, data_consulta, hora_consulta, especialidade, status
            FROM paciente_hc ORDER BY id

        """

        cursor.execute(sql)
        print('Exibindo todas as consultas marcadas na tela!')
        rows = cursor.fetchall()
        for row in rows:
            print(f'ID: {row[0]}, Nome: {row[1]}, Sobrenome: {row[2]}, Whatsapp: {row[3]}, Email: {row[4]}, Idade: {row[5]}, Data da consulta: {row[6]}, Hora da comsulta: {row[7]}, Especialidade: {row[8]}, Status da consulta: {row[9]} \n')

    except oracledb.Error as e:
        print(f'Não foi possível listar as consultas! {e}')

    
    finally:
        if con:
            con.close()


def deletar_consulta(id):
    print('Você quer desmarcar uma consulta !\n')
    con = get_conexao()
    if not con:
        return
    
    try:
        cursor = con.cursor()
        sql = "DELETE FROM paciente_hc WHERE id= :id "
        cursor.execute(sql, {'id' : id})
        con.commit()
        if cursor.rowcount > 0:
            print(f' Consulta do paciente {id} foi desmarcada com sucesso!\n')

        else:
            print(f' A consulta do paciente {id} não foi encontrada!\n')

    except oracledb.Error as e:
        print(f' Erro ao desmarcar a consulta! {e}\n')
        con.rollback()

    finally:
        if con:
            con.close()


def atualizar_informacoes(id, new_first_name, new_last_name, new_whatsapp, new_email, new_idade, new_data_consulta, new_hora_consulta, new_especialidade, new_status ):
    print('Atualizando o preço dos produtos pegando o produto pelo o ID!\n')
    con = get_conexao()
    if not con:
        return
    
    try:
        cursor = con.cursor()
        sql = "UPDATE paciente_hc SET first_name = :new_first_name, last_name = :new_last_name, whatsapp = :new_whatsapp, email = :new_email, idade = :new_idade, data_consulta = :new_data_consulta, hora_consulta = :new_hora_consulta, especialidade = :new_especialidade, status = :new_status WHERE id = :id "
        cursor.execute(sql, {
            'new_first_name': new_first_name,
            'new_last_name': new_last_name,
            'new_whatsapp': new_whatsapp,
            'new_email': new_email,
            'new_idade': new_idade,
            'new_data_consulta': new_data_consulta,
            'new_hora_consulta': new_hora_consulta,
            'new_especialidade': new_especialidade,
            'new_status': new_status,
            'id': id})
        con.commit()
        if cursor.rowcount > 0 :
            print (f' A consulta de número {id} foi alterada com sucesso!\n')

        else:
            print(f' A consulta de número {id} não foi encontrada!\n')

    except oracledb.Error as e:
        print(f'Erro ao atualizar a consulta pelo seguinte motivo: {e}\n')
        con.rollback()

    finally:
        if con:
            con.close() 

def buscar_consulta_por_id(id):
    print('Você escolheu buscar uma consulta por ID! \n')
    con = get_conexao()
    if not con:
        return
    
    try:
        cursor = con.cursor()
        sql = "SELECT * FROM paciente_hc WHERE id = :id"
        cursor.execute(sql, (id,))
        consulta = cursor.fetchone()

        if consulta:
            print(f'A consulta {id} foi encontrado com sucesso!\n')
            print(f'ID: {consulta[0]}, Nome: {consulta[1]}, Sobrenome: {consulta[2]}, Whatsapp: {consulta[3]}, Email: {consulta[4]}, Idade: {consulta[5]}, Data da Consulta: {consulta[6]}, Hora da consulta: {consulta[7]}, Especialidade: {consulta[8]}, Status da Consulta: {consulta[9]} \n')

        else:
            print(f'A consulta de número {id} não foi encontrada!\n')

    except oracledb.Error as e:
        print(f'Erro ao buscar consulta por id : {e}')

    finally:
        if con:
            con.close()


def menu_principal():
    
    while True:
        print('--- Menu Principal - HCBridge ---')
        print('1. Marcar Consulta')
        print('2. Solução do Projeto HCBridge')
        print('3. Integrantes HCBridge')
        print('4. Sair do programa')

        escolha = int(input('Escolha um número: '))

        if escolha == 1:
            print('Vimos que você quer marcar uma consulta!')
            Nome = input('Nome do Paciente: ')
            Sobrenome = input('Sobrenome do Paciente: ')
            Whatsapp = int(input('Qual o seu número de Whatsapp(escreva apenas números, ex: 11999999999)? : '))
            email = input('Qual é o seu email(ex: hcbridge@gmail.com)? : ')
            idade = int(input('Qual é a idade do paciente? : '))
            data_consulta = input('Qual é a data da consulta escolhida? : ')
            hora_consulta = input('Qual a hora da consulta escolhida? : ')
            especialidade = input('Qual é a especialidade do médico que você deseja?:  ')
            status = 'Agendada'
            inserir_paciente(Nome, Sobrenome, Whatsapp, email, idade, data_consulta, hora_consulta, especialidade, status  )

            while True:
                print('Você deseja fazer alguma alteração na consulta marcada!')
                print('1. Listar pacientes com consultas marcadas!')
                print('2. Buscar paciente pelo ID')
                print('3. Atualizar alguma informação de algum paciente!')
                print('4. Desmarcar alguma consulta de algum paciente!')
                print('5. Sair ')

                escolha2 = int(input('Escolha alguma opção! (1 - 5): '))

                if escolha2 == 1:
                    listar_pacientes()

                elif escolha2 == 2:
                    id_buscar_consulta = int(input('Escolha o ID da consulta que você deseja buscar: '))
                    buscar_consulta_por_id(id_buscar_consulta)

                elif escolha2 == 3:
                    listar_pacientes()
                    print('\n Por favor caso você não deseja mudar alguma opção escolhida apenas escrea novamente a mesma informação\n')
                    id_paciente =int(input('Digite o ID do Produto para atualizar: '))
                    new_nome = input('Novo nome do Paciente: ')
                    new_sobrenome = input('Novo sobrenome do Paciente: ')
                    new_whatsapp = int(input('Qual é o novo número de Whatsapp(escreva apenas números, ex: 11999999999)? : '))
                    new_email = input('Qual é o novo email(ex: hcbridge@gmail.com)? : ')
                    new_idade = int(input('Qual é a nova idade do paciente? : '))
                    new_data_consulta = input('Qual é a nova data da consulta escolhida? : ')
                    new_hora_consulta = input('Qual a nova hora da consulta escolhida? : ')
                    new_especialidade = input('Qual é a nova especialidade do médico que você deseja?:  ')
                    atualizar_informacoes(id_paciente, new_nome, new_sobrenome, new_whatsapp, new_email, new_idade, new_data_consulta, new_hora_consulta, new_especialidade)

                elif escolha2 == 4:
                    print('Você quer desmarcar uma consulta!')
                    listar_pacientes()
                    id_desmarcar = int(input('Digite o ID que deseja desmarcar a consulta: '))
                    deletar_consulta(id_desmarcar)

                elif escolha2 == 5:
                    print('Você escolheu sair dessa parte do programa!')
                    break

        elif escolha == 2:
            solu

        elif escolha ==3:
            integrantes()

        elif escolha == 4:
            print('Você escolheu sair! Até a próxima, a HCBridge agradece!')
            break
        

        else:
            print('Escolha uma opção válida entre (1 a 6)')






