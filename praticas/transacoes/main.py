from sqlalchemy import  create_engine, text

USUARIO = 'root'
SENHA = 'M%40gnus1990'
HOST = 'localhost'
BANCO = 'cfbcursos'

# engine = create_engine(f'mysql+mysqlconnector://{USUARIO}:{SENHA}@{HOST}/{BANCO}',echo=True)
#
# try:
#     with engine.connect() as bostakkk:
#         print('Banco conectado com sucesso!')
#         try:
#             resultado = bostakkk.execute(text('SELECT * FROM cliente'))
#             for l in resultado:
#                 print(l)
#
#         except Exception as erro:
#
#             print('ERRO! :',erro)
# except Exception as erro:
#
#     print(f'Erro ao se conectar com o banco!: {erro}')

# engine = create_engine(f'mysql+mysqlconnector://{USUARIO}:{SENHA}@{HOST}/{BANCO}',echo= True)


# with engine.connect() as conection:
#     try:
#         result = conection.execute(text('INSERT INTO cliente_aux(i_cliente_cliente,s_nome_cliente,i_tipo_cliente) VALUES(:i_cliente_cliente,:s_nome_cliente,:i_tipo_cliente)'),
#                                    [{
#                                        "i_cliente_cliente":30,
#                                        "s_nome_cliente" : 'Adalberto lolo pocaronto',
#                                        "i_tipo_cliente" : 2
#
#                                    }])
#         conection.commit()
#     except Exception as erro:
#         conection.rollback()
#         print(f"ERRO: {erro}")



engine = create_engine(f'mysql+mysqlconnector://{USUARIO}:{SENHA}@{HOST}/{BANCO}',echo=True)
try:
    with engine.connect() as connection:
        print('Banco conectado com sucesso!')
        try:
            connection.execute(text("DELETE FROM cliente_aux WHERE i_cliente_cliente = 30"))
            connection.commit()
        except Exception as erro:

            connection.rollback()
            print('Erro',erro)




except Exception as erro:
    print(f'Erro ao tentar se conectar com o banco! {erro}')







