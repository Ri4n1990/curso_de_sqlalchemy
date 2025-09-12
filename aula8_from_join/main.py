from sqlalchemy import  create_engine, ForeignKey, MetaData, Table, Column, select
from sqlalchemy.orm import Session, DeclarativeBase, Mapped, MappedColumn
from sqlalchemy.types import String, Integer, DATE, Enum, DECIMAL
USUARIO = 'root'
SENHA = 'M%40gnus1990'
HOST = 'localhost'
BANCO = 'loja_de_carros'

engine = create_engine(f'mysql+mysqlconnector://{USUARIO}:{SENHA}@{HOST}/{BANCO}')
metadat_obj = MetaData()

class Base(DeclarativeBase):
    pass


class Cliente(Base):
    __tablename__ = 'cliente'

    cpf_cliente : Mapped[str] = MappedColumn(String(14), primary_key = True)
    nome : Mapped[str] = MappedColumn(String(230), nullable = False)
    data_nascimento = MappedColumn(DATE, nullable = False)
    genero = MappedColumn(Enum('Feminino', 'Masculino'), nullable = False)
    telefone : Mapped[str] = MappedColumn(String(15), nullable = False)

    def __repr__(self):
        return f' [ cpf_cliente : {self.cpf_cliente} , nome : {self.nome} , data_nascimento : {self.data_nascimento} , genero : {self.genero} , Telefone : {self.telefone} ]'


compra = Table(
    'compra',
    metadat_obj,
    Column("id_compra" , Integer , primary_key = True),
    Column("data_compra" , DATE , nullable = False),
    Column("qtd" , DECIMAL(10,0) , nullable = False),
    Column("total_compra" , DECIMAL(10,0), nullable = False),
    Column("id_carro", Integer, ForeignKey("carros.id_linha"),nullable = False),
    Column("cpf_cliente", String(14),ForeignKey('cliente.cpf_cliente'),nullable = False )





)








class Carros(Base):
    __tablename__ = 'carros'

    id_linha : Mapped[int] = MappedColumn(Integer, primary_key = True)
    nome_carro : Mapped[str] = MappedColumn(String(150) , nullable = False)
    fabricante : Mapped[str] = MappedColumn(String(100) , nullable = False)
    ano : Mapped[int] = MappedColumn(nullable = False)
    cor : Mapped[str] = MappedColumn(String(100))
    preco_unitario = MappedColumn(DECIMAL(10,0))
    qtd_estoque = MappedColumn(DECIMAL(10,0))

    def __repr__(self):
      return  f' [ id_linha : {self.id_linha} , nome_carro : {self.nome_carro} , fabricante : {self.fabricante} , ano : {self.ano} , cor : {self.cor} , preco_unitario : {self.preco_unitario} , qtd_estoque : {self.qtd_estoque} ]'




#
# try:
#     with Session(engine) as session:
#         result = session.execute(
#             select(Cliente.cpf_cliente, Carros.nome_carro, Carros.fabricante).select_from(Cliente)
#             .join(compra , Cliente.cpf_cliente == compra.c.cpf_cliente)
#             .join(Carros , compra.c.id_carro == Carros.id_linha)
#
#         )
#         for row in result:
#             print(row)
#
#
#
# except Exception as erro:
#     print(f'OPS! ocorreu um erro {erro}')




stmt = (select(Cliente.nome, Cliente.data_nascimento, Cliente.genero, Carros.ano , Carros.cor, Carros.preco_unitario)
        .select_from(Cliente)
        .join(compra , Cliente.cpf_cliente == compra.c.cpf_cliente)
        .join(Carros, compra.c.id_carro == Carros.id_linha)
        )




with Session(engine) as session:

    result = session.execute(stmt)

    for row in result:
        print(row)











