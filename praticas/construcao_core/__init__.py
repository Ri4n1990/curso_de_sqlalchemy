import  sqlalchemy as sqla

USUARIO = 'root'
SENHA = 'M%40gnus'
HOST = 'localhost'
BANCO = 'cfbcursos'




engine = sqla.create_engine(f'mysql+mysqlconnector://{USUARIO}:{SENHA}@{HOST}/{BANCO}')

metadata_obj = sqla.MetaData()

clientes = sqla.Table(
    "clientes",
    metadata_obj,
    sqla.Column("id", sqla.String(10), primary_key= True),
    sqla.Column("nome", sqla.String, nullable = False)






)