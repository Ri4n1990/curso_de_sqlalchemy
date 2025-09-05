from sqlalchemy import create_engine, ForeignKey, text, insert
from sqlalchemy.orm import  DeclarativeBase, Mapped, MappedColumn, Session
from sqlalchemy.types import String, DATE
USERNAME = 'root'
SENHA = 'M%40gnus1990'
HOST = 'localhost'
BANCO = 'cfbcursos'


engine = create_engine(f'mysql+mysqlconnector://{USERNAME}:{SENHA}@{HOST}/{BANCO}')

class Base(DeclarativeBase):
    pass

class Tipo_Cliente(Base):
    __tablename__ = 'tipocliente'
    i_tipo_cliente_tipo_cliente: Mapped[int] = MappedColumn(primary_key = True)
    s_dsctipocliente_tipocliente: Mapped[str] = MappedColumn(String(100))
    def __repr__(self):
        return f'tipo : {self.i_tipo_cliente_tipo_cliente} , desctipo : {self.s_dsctipocliente_tipocliente}'


class Cliente(Base):
    __tablename__ = 'cliente'
    i_cliente_cliente : Mapped[int] = MappedColumn(primary_key = True)
    s_nome_cliente: Mapped[str] = MappedColumn(String(30), nullable = True)
    s_cpf_cliente: Mapped[str] = MappedColumn(String(11))
    d_nacs_cliente = MappedColumn(DATE)
    i_tipo_cliente: Mapped[int] = MappedColumn(ForeignKey("tipocliente.i_tipo_cliente_tipo_cliente"))
    s_usr_cliente: Mapped[str] = MappedColumn(String(20))
    s_senha_cliente: Mapped[str] = MappedColumn(String(20))

    def __repr__(self):
        return f"""
        [ id: {self.i_cliente_cliente} ,
         nome: {self.s_nome_cliente} ,  
         cpf: {self.s_cpf_cliente} ,
         data_nasc: {self.d_nacs_cliente} , 
         tipo_cliente: {self.i_tipo_cliente} , 
         urs_cliente: {self.s_usr_cliente} , 
         senha: {self.s_senha_cliente}  
        
        ]"""

with Session(engine) as session:
    try:
        stmt = insert(Cliente).values(s_nome_cliente='lufy derretido', i_tipo_cliente=1)
        re = stmt.returning(Cliente.s_nome_cliente)
        session.execute(stmt)
        session.commit()




    except  Exception as erro:
        session.rollback()
        print(erro)


