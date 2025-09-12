from sqlalchemy import  create_engine, ForeignKey, Table, Column, MetaData, select, func
from sqlalchemy.orm import  DeclarativeBase, Mapped, MappedColumn, Session
from sqlalchemy.types import String, Integer,DECIMAL, Enum,DATE

from aula_6_insert.main import Tipo_Cliente
from praticas.insert.aula05 import Cliente

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
    s_nome_cliente : Mapped[str] = MappedColumn(String(30), nullable = True)
    s_cpf_cliente : Mapped[str] = MappedColumn(String(11))
    d_nacs_cliente = MappedColumn(DATE)
    i_tipo_cliente : Mapped[int] = MappedColumn(ForeignKey('tipo_cliente.i_tipo_cliente_tipo_cliente'),nullable = False)
    s_usr_cliente : Mapped[str] = MappedColumn(String(20))
    s_senha_cliente : Mapped[str] = MappedColumn(String(20))

    def __repr__(self):
        return f'[ i_cliente_cliente : {self.i_cliente_cliente} , s_nome_cliente : {self.s_nome_cliente} , s_cpf_cliente : {self.s_cpf_cliente} , d_nasc_cliente : {self.d_nacs_cliente} , i_tipo_cliente : {self.i_tipo_cliente}, s_urs_cliente : {self.s_usr_cliente} , s_senha_cliente : {self.s_senha_cliente} ] '


    class Tipocliente(Base):
        __tablename__ = 'tipocliente'

        i_tipo_cliente_tipo_cliente : Mapped[int] = MappedColumn(primary_key = True)
        s_dsctipocliente_tipocliente : Mapped[str] = MappedColumn(nullable = False)

        def __repr__(self):
            return  f' [ i_tipo_cliente_tipo_cliente : {self.i_tipo_cliente_tipo_cliente} , s_dsctipocliente_tipocliente : {self.s_dsctipocliente_tipocliente} ]'



# stmt = (select(Tipo_Cliente.s_dsctipocliente_tipocliente, func.count(Cliente.i_tipo_cliente))
#         .select_from(Cliente)
#         .join(Tipo_Cliente, Cliente.i_tipo_cliente == Tipo_Cliente.i_tipo_cliente_tipo_cliente)
#         .group_by(Cliente.i_tipo_cliente)
#
#
#
#
#         )

# stmt = select(Cliente.s_nome_cliente).order_by(Cliente.s_nome_cliente.desc())

# stmt = (select(Cliente.s_nome_cliente, Cliente.i_tipo_cliente, Tipo_Cliente.s_dsctipocliente_tipocliente)
#         .select_from(Cliente)
#         .join(Tipo_Cliente, Cliente.i_tipo_cliente == Tipo_Cliente.i_tipo_cliente_tipo_cliente)
#         .where(Cliente.i_tipo_cliente == 1)
#
#
#
#         )


stmt = select(Cliente)

with Session(engine) as session:
    try:
        result = session.execute(stmt).all()
        for row in result:
            print(row)
    except Exception as erro:
        print(f'Erro {erro}')


















