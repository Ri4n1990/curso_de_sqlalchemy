from sqlalchemy import  create_engine, ForeignKey, select, delete
from sqlalchemy.orm import  DeclarativeBase, Mapped, MappedColumn, Session
from sqlalchemy.types import Integer, String, Enum, DATE

USUARIO ='root'
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
    s_cpf_cliente : Mapped[str]  = MappedColumn(String(11))
    d_nacs_cliente = MappedColumn(DATE)
    i_tipo_cliente : Mapped[int] = MappedColumn(ForeignKey('tipocliente.i_tipo_cliente_tipo_cliente'), nullable = False)
    s_usr_cliente : Mapped[str] = MappedColumn(String(20))
    s_senha_cliente : Mapped[str] = MappedColumn(String(20))




    def __repr__(self):
        return f' i_cliente_cliente : {self.i_cliente_cliente} , s_nome_cliente : {self.s_nome_cliente} , s_cpf_cliente : {self.s_cpf_cliente} , d_nacs_cliente : {self.d_nacs_cliente} , i_tipo_cliente : {self.i_tipo_cliente} , s_urs_cliente : {self.s_usr_cliente} , s_senha_cliente : {self.s_senha_cliente}'


class Tipocliente(Base):
    __tablename__ = 'tipocliente'

    i_tipo_cliente_tipo_cliente : Mapped[int] = MappedColumn(primary_key = True)
    s_dsctipocliente_tipocliente : Mapped[str] = MappedColumn(String(100))


    def __repr__(self):
        return f'i_tipo_cliente_tipo_cliente : {self.i_tipo_cliente_tipo_cliente} , s_dsctipocliente_tipocliente  : {self.s_dsctipocliente_tipocliente} '





with Session(engine) as session:
    try:
        stmt = (delete(Cliente)
                .where(Cliente.i_cliente_cliente == 56)
                )
        result = session.execute(stmt)
        session.commit()
        print(f'{result.rowcount} linhas afetadas!')


    except Exception as erro:
        session.rollback()
        print(f'erro ao tentar executar a query! {erro}')
