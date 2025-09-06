from sqlalchemy import  create_engine, select, label, and_, or_
from sqlalchemy.orm import DeclarativeBase, Mapped, MappedColumn, Session
from sqlalchemy.types import Integer, String, DATE, Enum



USUARIO = 'root'
SENHA = 'M%40gnus1990'
HOST = 'localhost'
BANCO = 'loja_de_carros'

engine = create_engine(f'mysql+mysqlconnector://{USUARIO}:{SENHA}@{HOST}/{BANCO}')



class Base(DeclarativeBase):
    pass


class Cliente(Base):
    __tablename__ = 'cliente'
    cpf_cliente: Mapped[str] = MappedColumn(String(14), primary_key = True)
    nome: Mapped[str] = MappedColumn(String(230))
    data_nascimento = MappedColumn(DATE)
    genero = MappedColumn(Enum('Feminino', 'Masculino'))
    telefone: Mapped[str] = MappedColumn(String(15))

    def __repr__(self):
        return f"""[
        CPF : {self.cpf_cliente} , 
        nome : {self.nome} , 
        data_nascimento : {self.data_nascimento}
        genero : {self.genero} , 
        telefone : {self.telefone}]
        """


# stmt = select(Cliente.nome.label('nome_magrao'), Cliente.cpf_cliente.label('cpf_magrao'))
#
# with Session(engine) as session:
#     try:
#         result = session.execute(stmt)
#         for row in result:
#             print(row.cpf_magrao)
#
#     except Exception as erro:
#         print(f'erro {erro}')


stmt  = select(Cliente).where(and_(Cliente.cpf_cliente == '404.303.202-10' , Cliente.nome == 'Diego Nunes'))

with Session(engine) as session:
    result = session.execute(stmt)
    for row in result:
        print(row)


