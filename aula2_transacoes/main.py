from sqlalchemy import  create_engine , text



USUARIO = 'root'
SENHA = 'M%40gnus1990'
HOST = 'localhost'
BANCO = 'cfbcursos'

engine = create_engine(f'mysql+mysqlconnector://{USUARIO}:{SENHA}@{HOST}/{BANCO}',echo=True)


# with engine.connect() as conn:
#     resultado = conn.execute(text('SELECT * FROM cliente'))
#     for row in resultado:
#         print(row.s_nome_cliente,row.s_cpf_cliente)
















with engine.connect() as bosta:
    try:
        bosta.execute(text('INSERT INTO cliente(s_nome_cliente,s_cpf_cliente,i_tipo_cliente) VALUES(:s_nome_cliente,:s_cpf_cliente,:i_tipo_cliente)'),
                      [{"s_nome_cliente":'jozimar antunes jacinto pintos',"s_cpf_cliente":'12345678900','i_tipo_cliente':2}])
        bosta.commit()
        print('deu certo')

    except Exception as erro:
        bosta.rollback()
        print('deu ruim magrão',erro)

