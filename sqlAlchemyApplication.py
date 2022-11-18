import sqlalchemy
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy import inspect
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

Base = declarative_base()

class User(Base):
    __tablename__ = "user_acount"
    # atributos
    id = Column(Integer,primary_key=True )
    name = Column(String)
    fullname = Column(String)

    Address = relationship("Address", back_populates= "user")

    def __repr__(self):
        return f"User(id={self.id}, name = {self.name}, fullname= {self.fullname})"

class Address(Base):
    __tablename__ = "Address" 
    id = Column(Integer, primary_key=True)
    email_address = Column(String(30), nullable =False)
    user_id = Column(Integer, ForeignKey("user_acount.id"), nullable = False)

    user = relationship("user", back_populates="Address")

    def __repr__(self):
        return f"Address(id={self.id}, email_address = {self.email_address})"

print(User.__tablename__)

print(Address.__tablename__)

# Conexão com banco de dados.
engine = create_engine("sqlite://")

# Criando as classes como tabelas no banco de dados.
Base.metadata.create_all(engine)

inspetor_engine = inspect(engine)

print(inspetor_engine.has_table('user_account'))

print(inspetor_engine.get_table_names())

print(inspetor_engine.default_schema_name)

with Session(engine) as session:
    luiz = User(
        name='Luiz',
        fullname='Luiz Jonathan',
        Address=[Address(email_address= 'luizj@hotmail.com')]
    )
