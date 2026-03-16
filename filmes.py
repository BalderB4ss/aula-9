from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

#Filmes

class Filme(Base):
    __tablename__ = "filmes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(150), nullable=True)
    genero = Column(String(100), nullable=True)
    ano_lancamento = Column(Integer)
    nota = Column(Float)
    disponivel = Column(Boolean, default=True)

    def __init__(self, titulo, genero, ano_lancamento, nota ):
        self.titulo = titulo
        self.genero = genero
        self.ano_lancamento = ano_lancamento
        self.nota = nota
    
engine = create_engine("sqlite:///cinema.db")

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

#Criar funções CRUD
def cadastrar_filme():
    print(f"\n--- CADASTRAR FILME ---\n")
    titulo = input("Digite o título do filme: ")
    genero = input("Digite o genero do filme: ")
    ano_lancamento = int(input("Digite o ano de lançamento do filme: "))
    nota = float(input("Digite a nota do filme: "))

    with Session() as session:
        try:
            # Verificar o título duplicado
            buscar_filme = session.query(Filme).filter_by(titulo = titulo, ano_lancamento = ano_lancamento).first()
            if buscar_filme == None:
                novo_filme = Filme(titulo, genero, ano_lancamento, nota)
                session.add(novo_filme)
                session.commit()
                print("Filme cadastrado com sucesso!")
            print("Já existe um filme com esse filme e esse ano!")

        except Exception as error:
            session.rollback()
            print(f"Ocorreu um erro {error}")

cadastrar_filme()

