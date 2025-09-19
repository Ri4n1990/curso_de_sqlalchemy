from sqlalchemy import  create_engine, ForeignKey, select
from sqlalchemy.orm import  DeclarativeBase, Mapped, MappedColumn, Session, relationship
from sqlalchemy.types import Integer, String, Enum, DATE
from typing import List


USUARIO = 'root'
SENHA = 'M%40gnus1990'
HOST = 'localhost'
BANCO = 'cfbcursos'

engine = create_engine(f'mysql+mysqlconnector://{USUARIO}:{SENHA}@{HOST}/{BANCO}', echo= True)


class Base(DeclarativeBase):
    pass




class Cliente(Base):

    __tablename__ = 'cliente'

    i_cliente_cliente : Mapped[int] = MappedColumn(primary_key = True)
    s_nome_cliente : Mapped[str] = MappedColumn(String(30), nullable = False)
    s_cpf_cliente : Mapped[str] = MappedColumn(String(11))
    d_nacs_cliente = MappedColumn(DATE)
    i_tipo_cliente : Mapped[int] = MappedColumn(ForeignKey('tipocliente.i_tipo_cliente_tipo_cliente'), nullable = False)
    s_usr_cliente : Mapped[str] = MappedColumn(String(20))
    s_senha_cliente : Mapped[str] = MappedColumn(String(20))

    rtipocliente : Mapped[List["Tipocliente"]] = relationship(back_populates =  'cliente')




    def __repr__(self):

        return f' i_cliente_cliente : {self.i_cliente_cliente} , s_nome_cliente : {self.s_nome_cliente} , s_cpf_cliente : {self.s_cpf_cliente} , d_nacs_cliente : {self.d_nacs_cliente} , i_tipo_cliente : {self.i_tipo_cliente} , s_urs_cliente : {self.s_usr_cliente} , s_senha_cliente : {self.s_senha_cliente}'

class Tipocliente(Base):

    __tablename__ = 'tipocliente'

    i_tipo_cliente_tipo_cliente : Mapped[int] = MappedColumn(primary_key = True)
    s_dsctipocliente_tipocliente : Mapped[str] = MappedColumn(String(100), nullable = False)

    cliente : Mapped[List["Cliente"]] = relationship(back_populates = 'rtipocliente')

    def __repr__(self):
        return  f'i_tipo_cliente_tipo_cliente : {self.i_tipo_cliente_tipo_cliente} , s_dsctipocliente_tipocliente : {self.s_dsctipocliente_tipocliente}'






with Session(engine) as session:
    try:
        fulano = session.get(Cliente, 64)
        session.delete(fulano)
        session.commit()
        print('deletado com sucesso')


    except Exception as erro:
        session.rollback()
        s
        print('erro', erro)
