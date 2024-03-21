# Importando a biblioteca PyODBC
import pyodbc

# Parâmetros de conexão
server = 'localhost'
database = 'vendas'
username = 'root'
password = '123'

# Construindo a string de conexão (DSN)
conn_str = (
    f"DRIVER={{MySQL ODBC 8.0 Driver}};"
    f"SERVER={server};"
    f"DATABASE={database};"
    f"UID={username};"
    f"PWD={password};"
)

# Conectando ao banco de dados
try:
    cnxn = pyodbc.connect(conn_str)
    cursor = cnxn.cursor()
    print("Conexão bem-sucedida!")
    
    # Aqui você pode executar consultas ou realizar outras operações no banco de dados

except pyodbc.Error as ex:
    sqlstate = ex.args[1]
    print(f"Erro ao conectar ao banco de dados: {sqlstate}")
