from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Smartphone(Base):
    __tablename__ = "ponsel"
    id = Column(Integer, primary_key=True)
    brand = Column(String(50))
    ram = Column(String(50))
    storage = Column(String(10))
    prosesor = Column(String(50))
    baterai = Column(String(20))
    ukuran_layar = Column(String(10))
    harga = Column(Integer)

    def __repr__(self):
        return f"Smartphone(id={self.id!r}, brand={self.brand!r}, harga={self.harga!r})"
