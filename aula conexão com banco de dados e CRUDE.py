
'''
CRUD - Create, Read, Update, Delete
- conjunto de operações básicas de manipulação de dados

- Módulo Oracle python-oracledb (biblioteca) (sucessor do cx_oracle)
   - permite que a aplicação Python se conecte a um banco de dados
   Oracle e execute comandos SQL

   Pré- requisito
    - pip install oracledb (*)
    - pip install cx_oracle
    - pip install python_oracledb
    - ter um banco de dados Oracle

    String de conexão
    <user_name>/<password>@<db_host_address>:<db_port>/<db_service>
    conn = 'usuario/senha@localhost:1521/orcl'

    Tabela - ceo_details
    campos - nome, sobrenome, empresa, idade
    "Steve" - str
    "Jobs" - str
    "Apple" - str
    50 - int
'''

import oracledb

#criar uma conexão com o Banco de Dados Oracle
def getConnection():
    try:
        connection = oracledb.connect(user = "rm123",
        password="123", host="oracle.fiap.com.br",
        port="1521", service_name="orcl")
    except Exception as e:
        print(f'Erro ao obter a conexão: {e}')
    return connection
    
def criar_tabela(conn):
    #obter uma conexão
    #conn = getConnection()

    #obter um cursor - objeto utilizado para executar instruções SQL
    cursor = conn.cursor()

    try:
        create_table_sql = """
        CREATE TABLE ceo_details (
        id_pessoa NUMBER GENERATED ALWAYS AS IDENTITY ,
        first_name      VARCHAR2(50) NOT NULL,
        last_name VARCHAR2(50) NOT NULL,
        email     VARCHAR2(100) UNIQUE NOT NULL,
        idade     NUMBER(3),
        empresa   VARCHAR2(100)

        PRIMARY KEY (id)
        );

        """
        cursor.execute(create_table_sql)
        print(f'Tabela CEO_DETAILS foi criada com sucesso!')
    except oracledb.Error as e:
        print(f'Erro de conexão: {e}')   



#Programa Principal
conn = getConnection() #testando a conexão
print(f'Conexão: {conn.version}')
criar_tabela(conn)

