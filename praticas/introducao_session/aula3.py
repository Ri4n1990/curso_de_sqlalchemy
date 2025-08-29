from sqlalchemy.orm import  Session
from sqlalchemy import  text , create_engine

USUARIO = 'root'
SENHA = 'M%40gnus1990'
HOST = 'localhost'
BANCO = 'cfbcursos'



engine = create_engine(f'mysql+mysqlconnector://{USUARIO}:{SENHA}@{HOST}/{BANCO}')

try:

    with Session(engine) as ses:
        print('Banco conectado...')
        try:
            query = text('SELECT * FROM cliente WHERE s_cpf_cliente = :cpf')
            res = ses.execute(query, {"cpf": '9999999999'})
            for r in res:
                print('Nome:',r.s_nome_cliente)


        except Exception as erro:
            print(f'Erro ao tentar executar a query {erro}')




except Exception as erro:
    print(f'Erro ao tentar se conectar com o banco {erro}')

