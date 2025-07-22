from sqlalchemy import create_engine, text
from datetime import datetime


class CompanyTable:
    __scripts = {
        "select": text("select * from company where deleted_at is null"),
        "select_active": text("select * from company where \"is_active\" = true AND deleted_at is null"),
        "delete_by_id": text("delete from company where id =:id_to_delete"),
        "insert_new": text("""
        INSERT INTO company("name", "is_active", "create_timestamp", "change_timestamp")
        VALUES (:name, :is_active, :create_timestamp, :change_timestamp)
    """),
        "get_max_id": text("SELECT MAX(\"id\") FROM company WHERE deleted_at IS NULL"),
        "select by id": text("SELECT \* FROM company "
                             "WHERE id =:select_id AND deleted_at IS NULL")
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    def get_companies(self):
        conn = self.__db.connect()
        result = conn.execute(self.__scripts["select"])
        rows = result.mappings().all()
        conn.close()
        return rows

    def get_active_companies(self):
        conn = self.__db.connect()
        result = conn.execute(self.__scripts["select_active"])
        rows = result.mappings().all()
        conn.close()
        return rows

    def delete(self, id):
        conn = self.__db.connect()
        conn.execute(self.__scripts ["delete_by_id"], {"id_to_delete": id})
        conn.commit()
        conn.close()

    def create(self, name, is_active, create_timestamp, change_timestamp):
        if create_timestamp is None:
            create_timestamp = datetime.now()
            change_timestamp = datetime.now()
        conn = self.__db.connect()
        conn.execute(self.__scripts["insert_new"],
                     {"new_name": name, "is_active": is_active, "create_timestamp": create_timestamp, "change_timestamp": change_timestamp})
        conn.commit()
        conn.close()


    def get_max_id(self):
        conn = self.__db.connect()
        result = conn.execute(self.__scripts["get_max_id"])
        max_id = result.scalar()
        conn.close()
        return max_id

    def get_company_by_id(self, id):
        conn = self.__db.connect()
        result = conn.execute(
            self.__scripts["select by id"],{"select_id": id}
        )
        company = result.mappings().all()
        conn.close()
        return company

    def get_company_by_id(self, id):
        conn = self.__db.connect()
        result = conn.execute(
            self.__scripts["select by id"],
        {"select_id": id}
        )
        company = result.mappings().all()
        conn.close()
        return company