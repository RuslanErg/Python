from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "postgresql://postgres:RusPG2025@localhost:5432/QA 61.0"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)

    def __repr__(self):
        return f"<Student(id={self.id}, name='{self.name}', age={self.age})>"


def create_db_tables():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    create_db_tables()
    print("Таблицы созданы")
