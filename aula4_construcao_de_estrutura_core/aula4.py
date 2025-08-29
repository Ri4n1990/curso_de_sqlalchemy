from sqlalchemy import  create_engine , MetaData , Integer, String , text, Table, Column

USUARIO = 'root'
SENHA = 'M%40gnus1990'
HOST = 'localhost'
BANCO = 'cfbcursos'

engine = create_engine(f'mysql+mysqlconnector://{USUARIO}:{SENHA}@{HOST}/{BANCO}')

metadata_obj = MetaData()

user_tabela = Table(
    'nome_tabela',
    metadata_obj,
    Column("id", String, primary_key=True),
    Column("nome", String(30), nullable= False)

)



