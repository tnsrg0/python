from sqlalchemy import text


class StudentTable:
    __scripts = {
        "insert_subject": text(
            "INSERT INTO subject (subject_id, subject_title) "
            "VALUES (:subject_id, :subject_title)"
        ),
        "insert_user": text(
            "INSERT INTO users (user_id, user_email, subject_id) "
            "VALUES (:user_id, :user_email, :subject_id)"
        ),
        "delete_user": text(
            "DELETE FROM users WHERE user_id = :user_id"
        ),
        "delete_subject": text(
            "DELETE FROM subject WHERE subject_id = :subject_id"
        ),
        "insert": text(
            "INSERT INTO student (user_id, level, education_form, subject_id) "
            "VALUES (:user_id, :level, :education_form, :subject_id)"
            ),
        "update_level": text(
            "UPDATE student "
            "SET level = :new_level "
            "WHERE user_id = :user_id"
            ),
        "delete": text(
            "DELETE FROM student WHERE user_id = :user_id"
            ),
        "select_by_user_id": text(
            "SELECT level, education_form FROM student "
            "WHERE user_id = :user_id"
            )
            }

    def __init__(self, connection):
        self.connection = connection

    def create_subject(self, subject_id: int, subject_title: str):
        self.connection.execute(
            self.__scripts["insert_subject"],
            {
                "subject_id": subject_id,
                "subject_title": subject_title
            }
        )

    def create_user(self, user_id: int, user_email: str, subject_id: int):
        self.connection.execute(
            self.__scripts["insert_user"],
            {
                "user_id": user_id,
                "user_email": user_email,
                "subject_id": subject_id
            }
        )

    def delete_user(self, user_id: int):
        self.connection.execute(
            self.__scripts["delete_user"],
            {
                "user_id": user_id
            }
        )

    def delete_subject(self, subject_id: int):
        self.connection.execute(
            self.__scripts["delete_subject"],
            {
                "subject_id": subject_id
            }
        )

    def insert_student(
            self, user_id: int,
            level: str,
            education_form: str,
            subject_id: int
            ):
        self.connection.execute(
            self.__scripts["insert"],
            {
                "user_id": user_id,
                "level": level,
                "education_form": education_form,
                "subject_id": subject_id
            }
        )

    def update_level_student(self, user_id: int, new_level: str):
        self.connection.execute(
            self.__scripts["update_level"],
            {
                "new_level": new_level,
                "user_id": user_id
            }
        )

    def delete_student(self, user_id: int):
        self.connection.execute(
            self.__scripts["delete"],
            {
                "user_id": user_id
            }
        )

    def get_student_by_user_id(self, user_id: int):
        return self.connection.execute(
            self.__scripts["select_by_user_id"],
            {"user_id": user_id}
        ).fetchone()
