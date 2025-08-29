from sqlalchemy import  create_engine
USUARIO = 'root'
SENHA = 'M%40gnus1990'
HOST = 'localhost'
BANCO = 'cars'

engine = create_engine(f"mysql+mysqlconnector://{USUARIO}:{SENHA}@{HOST}/{BANCO}",echo=True)