from sqlalchemy import  create_engine, ForeignKey, select
from sqlalchemy.orm import  DeclarativeBase, Mapped, MappedColumn, Session
from sqlalchemy.types import String, Integer, Enum, DATE

USER = 'root'
PASSWORD = 'M%40gnus1990'
HOST = 'localhost'
DATABASE = 'cfbcursos'


engine = create_engine(f'mysql+mysqlconnector://{USER}:{PASSWORD}@{HOST}/{DATABASE}', echo= True)


class Base(DeclarativeBase):
    pass



class Cliente(Base):
    __tablename__ = 'cliente'

    i_cliente_cliente : Mapped[int] = MappedColumn(primary_key = True)
    s_nome_cliente : Mapped[str] = MappedColumn(String(30), nullable = False)
    s_cpf_cliente : Mapped[str] = MappedColumn(String(11))
    d_nacs_cliente  = MappedColumn(DATE)
    i_tipo_cliente : Mapped[int] = MappedColumn(ForeignKey('tipocliente.i_tipo_cliente_tipo_cliente'),nullable = False)
    s_usr_cliente : Mapped[str] = MappedColumn(String(20))
    s_senha_cliente : Mapped[str] = MappedColumn(String(20))


    def __repr__(self):
        def __repr__(self):
            return f' i_cliente_cliente : {self.i_cliente_cliente} , s_nome_cliente : {self.s_nome_cliente} , s_cpf_cliente : {self.s_cpf_cliente} , d_nacs_cliente : {self.d_nacs_cliente} , i_tipo_cliente : {self.i_tipo_cliente} , s_urs_cliente : {self.s_usr_cliente} , s_senha_cliente : {self.s_senha_cliente}'



class Tipocliente(Base):
    __tablename__ = 'tipocliente'

    i_tipo_cliente_tipo_cliente : Mapped[int] = MappedColumn(primary_key = True)
    s_dsctipocliente_tipocliente : Mapped[str] = MappedColumn(String(100), nullable = False)

stmt = (select(Cliente.s_nome_cliente,Tipocliente.s_dsctipocliente_tipocliente)
        .select_from(Cliente)
        .join(Tipocliente, Cliente.i_tipo_cliente == Tipocliente.i_tipo_cliente_tipo_cliente))

with Session(engine) as session:
    try:

        kailo = Cliente(i_cliente_cliente = None, s_nome_cliente ='kailo', i_tipo_cliente = 2)
        session.add(kailo)
        session.flush()
        session.commit()
        print('adicionado com sucesso!')

    except Exception as erro:
        session.rollback()
        print(f'erro ao tentar executar a query {erro}')