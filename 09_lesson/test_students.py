import pytest
from sqlalchemy import create_engine
from db_pages import StudentTable


db_connection = "postgresql://postgres:2804030301@localhost:5432/QA"
engine = create_engine(db_connection)


@pytest.fixture(scope="module")
def db():
    connection = engine.connect()
    return connection


@pytest.fixture(scope="module")
def create_test_subject(db, request):
    student_table = StudentTable(db)
    subject_test_id = 522
    student_table.create_subject(subject_test_id, "Infographics")

    def delete_subject_after_test():
        student_table.delete_subject(subject_test_id)

    request.addfinalizer(delete_subject_after_test)
    return subject_test_id


@pytest.fixture(scope="module")
def create_test_user(db, create_test_subject, request):
    student_table = StudentTable(db)
    user_test_id = 711
    student_table.create_user(
        user_test_id,
        "student_test@mail.com",
        create_test_subject
        )

    def delete_user_after_test():
        student_table.delete_user(user_test_id)

    request.addfinalizer(delete_user_after_test)
    return user_test_id


def test_insert_student(db, create_test_user, create_test_subject):
    student_table = StudentTable(db)
    student_table.insert_student(
        create_test_user,
        "Beginner", "personal",
        create_test_subject
        )
    db.commit()
    student_data = student_table.get_student_by_user_id(create_test_user)
    assert student_data is not None
    assert student_data[0] == "Beginner"
    assert student_data[1] == "personal"


def test_update_student(db, create_test_user, create_test_subject):
    student_table = StudentTable(db)
    student_table.insert_student(
        create_test_user,
        "Beginner", "personal",
        create_test_subject
        )
    db.commit()
    student_table.update_level_student(create_test_user, "Pre-Intermediate")
    db.commit()
    student_data = student_table.get_student_by_user_id(create_test_user)
    assert student_data[0] == "Pre-Intermediate"


def test_delete_student(db, create_test_user, create_test_subject):
    student_table = StudentTable(db)
    student_table.insert_student(
        create_test_user,
        "Beginner", "personal",
        create_test_subject
        )
    db.commit()
    student_table.delete_student(create_test_user)
    db.commit()
    student_data = student_table.get_student_by_user_id(create_test_user)
    assert student_data is None
