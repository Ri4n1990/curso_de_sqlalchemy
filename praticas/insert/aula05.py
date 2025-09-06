from sqlalchemy import  create_engine, text, insert
from sqlalchemy.orm import DeclarativeBase, Mapped, MappedColumn, Session
from sqlalchemy.types import String, Integer, DATE, Enum, DECIMAL, CHAR

USUARIO = 'root'
SENHA = 'M%40gnus1990'
HOST = 'localhost'
BANCO = 'loja_de_carros'

engine = create_engine(f"mysql+mysqlconnector://{USUARIO}:{SENHA}@{HOST}/{BANCO}", echo=True)

class Base(DeclarativeBase):
    pass


class Cliente(Base):
    __tablename__ = 'cliente'

    cpf_cliente : Mapped[str] = MappedColumn(String(14), primary_key = True)
    nome : Mapped[str] = MappedColumn(String(230), nullable = False)
    data_nascimento = MappedColumn(DATE, nullable = False)
    genero = MappedColumn(Enum('Feminino', "Masculino"), nullable = False)
    telefone : Mapped[str] = MappedColumn(String(15), nullable = False)


    def __repr__(self):
        return f"""
        [
        cpf : {self.cpf_cliente} , 
        nome : {self.nome} , 
        data_nascimento : {self.data_nascimento} , 
        genero : {self.genero} , 
        telefone : {self.telefone}

        ]
        """




with Session(engine) as session:
    try:

        stmt = insert(Cliente)
        session.execute(
            stmt,
            [
                {"cpf_cliente": '00000000000', "nome" : "jorge" , "data_nascimento" : "2004-01-03" , "genero" : "Masculino", "telefone" : "51993746389"}
            ],
        )
        session.commit()
    except Exception as erro:
        session.rollback()
        print(f'erro {erro}')

