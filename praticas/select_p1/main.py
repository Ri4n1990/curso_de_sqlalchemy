from sqlalchemy import  create_engine, select, insert, label, and_
from sqlalchemy.orm import  DeclarativeBase, Mapped, MappedColumn, Session
from sqlalchemy.types import String, DATE , Integer, Enum, DECIMAL, CHAR

USUARIO = 'root'
SENHA = 'M%40gnus1990'
HOST = 'localhost'
BANCO = 'loja_de_carros'

engine = create_engine(f'mysql+mysqlconnector://{USUARIO}:{SENHA}@{HOST}/{BANCO}')


class Base(DeclarativeBase):
    pass

class Cliente(Base):
    __tablename__ = 'cliente'
    cpf_cliente : Mapped[str] = MappedColumn(String(14), primary_key = True)
    nome : Mapped[str] = MappedColumn(String(230), nullable = False)
    data_nascimento = MappedColumn(DATE, nullable = False)
    genero = MappedColumn(Enum('Masculino' , 'Feminino'), nullable = False)
    telefone : Mapped[str] = MappedColumn(String(15), nullable = False)

    def __repr__(self):
        return f'[ cpf_cliente : {self.cpf_cliente} , nome : {self.nome} , data_nascimento : {self.data_nascimento} , genero : {self.genero} , telefone : {self.telefone} '

# stmt = select(Cliente.cpf_cliente.label("cpf") , Cliente.nome)
#
# with Session(engine) as session:
#     try:
#         result = session.execute(stmt)
#         for row in result:
#             print(row.cpf)
#
#     except Exception as erro:
#         print(f'Erro ao tentar executar a query! {erro}')
#
#
# stmt = insert(Cliente)
#
# with Session(engine) as session:
#     try:
#         session.execute(stmt,
#                         [
#                             {"cpf_cliente" : "00312034211", "nome" : "pedrinho butijão", "data_nascimento": "2004-01-03" , "genero" : "Masculino" , "telefone" : '51222222222'}
#                         ],)
#
#         session.commit()
#         print('adicionado com sucesso!')
#     except Exception as erro:
#         session.rollback()
#         print(f'Erro ao tentar executar query {erro}')


stmt  = select(Cliente).where(and_(Cliente.cpf_cliente == '00312034211' , Cliente.nome == 'pedrinho butijão'))

with Session(engine) as session:
    try:
        result = session.execute(stmt)

        for row in result:
            print(row)
    except Exception as erro:
        print(f'erro ao tentar executar a query! {erro}')