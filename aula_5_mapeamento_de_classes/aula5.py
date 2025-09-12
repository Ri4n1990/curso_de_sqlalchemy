from sqlalchemy import create_engine, ForeignKey , Select
from sqlalchemy.orm import  DeclarativeBase, MappedColumn, Mapped
from sqlalchemy.types import  String, DATE

USUARIO = 'root'
SENHA = 'M%40gnus1990'
HOST = 'localhost'
BANCO = 'cfbcursos'

engine = create_engine(f'mysql+mysqlconnector://{USUARIO}/:{SENHA}@{HOST}/{BANCO}', echo=True)

class Base(DeclarativeBase):
    pass

class Cliente(Base):
    __tablename__ = 'cliente'
    id : Mapped[int] = MappedColumn(primary_key = True)
    nome: Mapped[str] = MappedColumn(String(30), nullable = False)
    cpf : Mapped[str] = MappedColumn(String(11))
    d_nasc = MappedColumn(DATE)
    t_cliente: Mapped[int] = MappedColumn(ForeignKey('tipocliente.i_tipo_cliente_tipo_cliente'), nullable=False)
    s_urs_cli: Mapped[str] = MappedColumn(String(20))
    senha: Mapped[str] = MappedColumn(String(20))


    def __repr__(self):
        return  f'id: {self.id} nome: {self.nome} CPF: {self.cpf}'


novo = Cliente(id = 2, nome = 'lolo', cpf = '04922014047',d_nasc = '2004-01-03', t_cliente = 1,s_urs_cli = 'sei lá', senha = '12334444'   )

