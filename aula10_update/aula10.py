from sqlalchemy import  create_engine, bindparam, update, ForeignKey, select, insert
from sqlalchemy.orm import  Session, Mapped, MappedColumn, DeclarativeBase, aliased
from sqlalchemy.types import String, Integer, Enum, DATE


USUARIO = 'root'
SENHA = 'M%40gnus1990'
HOST = 'localhost'
BANCO = 'cfbcursos'


engine = create_engine(f'mysql+mysqlconnector://{USUARIO}:{SENHA}@{HOST}/{BANCO}', echo = True)

class Base(DeclarativeBase):
    pass


class Cliente(Base):
    __tablename__ = 'cliente'

    i_cliente_cliente : Mapped[int] = MappedColumn(primary_key = True)
    s_nome_cliente : Mapped[str] = MappedColumn(String(30) , nullable = False)
    s_cpf_cliente : Mapped[str] = MappedColumn(String(11))
    d_nacs_cliente = MappedColumn(DATE)
    i_tipo_cliente :Mapped[int] = MappedColumn(ForeignKey('tipocliente.i_tipo_cliente_tipo_cliente'), nullable= False)
    s_usr_cliente : Mapped[str] = MappedColumn(String(20))
    s_senha_cliente : Mapped[str] = MappedColumn(String(20))

    def __repr__(self):
        return  f'  i_cliente_cliente : {self.i_cliente_cliente} , s_nome_cliente : {self.s_nome_cliente} , s_cpf_cliente : {self.s_cpf_cliente} , d_nacs_cliente : {self.d_nacs_cliente} , i_tipo_cliente : {self.i_tipo_cliente} , s_usr_cliente : {self.s_usr_cliente} , s_senha_cliente : {self.s_senha_cliente}  '


class Tipocliente(Base):
    __tablename__ = 'tipocliente'
    i_tipo_cliente_tipo_cliente :Mapped[int] = MappedColumn(primary_key = True)
    s_dsctipocliente_tipocliente : Mapped[str] = MappedColumn(String(100), nullable = False)

    def __repr__(self):
        return  f' i_tipo_cliente_tipo_cliente : {self.i_tipo_cliente_tipo_cliente} , s_dsctipocliente_tipocliente: {self.s_dsctipocliente_tipocliente}   '



cli = aliased(Cliente)
tip = aliased(Tipocliente)

# stmt = (update(cli)
#         .where(cli.s_nome_cliente == 'lufy derretido')
#         .values(s_nome_cliente  = 'borrachão')
#
#
#
#         )

# stmt = (update(cli)
#               .where(cli.i_tipo_cliente == 1)
#               .values(s_nome_cliente = 'bet onesta (sem h)')
#
#
#               )

stmt = insert(Cliente)

with Session(engine) as session:

    try:
        session.execute(stmt,
                        [
                            {"s_nome_cliente" : 'naruto antes do boruto' , "i_tipo_cliente" : 2}
                        ],
                        )
        session.commit()
        print('change sucesful (lá ele)')
        result = session.execute(select(cli))
        for row in result:
            print(row)


    except Exception as erro:
        print(f'Erro ao tentar executar a query {erro}')




