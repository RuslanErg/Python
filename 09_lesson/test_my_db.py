import pytest
from sqlalchemy.orm import Session
from My_DB import SessionLocal, Student, Base, engine


@pytest.fixture(scope="function")
def db():
    Base.metadata.create_all(bind=engine)
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
        with SessionLocal() as clean_session:
            clean_session.query(Student).delete()
            clean_session.commit()


def test_add_student(db: Session):
    new_student = Student(name="Ruslan", age=44)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    assert new_student.id is not None
    assert new_student.name == "Ruslan"
    assert new_student.age == 44

    retrieved_student = db.query(Student).filter(
        Student.name == "Ruslan").first()
    assert retrieved_student is not None
    assert retrieved_student.name == "Ruslan"
    print(new_student)


def test_update_student(db: Session):
    student_to_update = Student(name="Ivan", age=42)
    db.add(student_to_update)
    db.commit()
    db.refresh(student_to_update)

    student_to_update.age = 23
    db.commit()
    db.refresh(student_to_update)

    updated_student = (db.query(Student)
                       .filter(Student.id == student_to_update.id)
                       .first())
    assert updated_student is not None
    assert updated_student.age == 23
    print(student_to_update)


def test_delete_student(db: Session):
    student_to_delete = Student(name="Petr", age=27)
    db.add(student_to_delete)
    db.commit()
    db.refresh(student_to_delete)
    student_id = student_to_delete.id

    db.delete(student_to_delete)
    db.commit()

    deleted_student = (db.query(Student)
                       .filter(Student.id == student_id)
                       .first())
    assert deleted_student is None
    print(student_to_delete)
