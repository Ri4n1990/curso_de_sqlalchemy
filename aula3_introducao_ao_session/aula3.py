from sqlalchemy import  create_engine , text
from sqlalchemy.orm import Session


USUARIO = 'root'
SENHA = 'M%40gnus1990'
HOST = 'localhost'
BANCO = 'cfbcursos'

engine = create_engine(f'mysql+mysqlconnector://{USUARIO}:{SENHA}@{HOST}/{BANCO}',echo=True)

with Session(engine) as session:
    query = text('SELECT * FROM cliente where s_cpf_cliente = :comp')
    result = session.execute(query,{"comp":"12345678900"})
    for r in result:
        print(r.s_nome_cliente)



