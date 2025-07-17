from sqlalchemy import create_engine, text


class CompanyTable:
    __scripts = {
        "select": text("select * from company where deleted_at is null"),
        "select active": text("select * from company where \"is_active\" = true AND deleted_at is null"),
        "delete by id": text("delete from company where id =:id_to_delete"),
        "insert_new": text("INSERT INTO company(\"name\") values (:new_name)"),
        "get_max_id": text("SELECT MAX(\"id\") FROM company WHERE deleted_at IS NULL")
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
        result = conn.execute(self.__scripts["select active"])
        rows = result.mappings().all()
        conn.close()
        return rows

    def delete(self, id):
        conn = self.__db.connect()
        conn.execute(self.__scripts ["delete by id"], {"id_to_delete": id})
        conn.close()


    def create(self, name):
        conn = self.__db.connect()
        conn.execute(self.__scripts ["insert_new"], {"new_name" : name})
        conn.commit()
        conn.close()


    def get_max_id(self):
        conn = self.__db.connect()
        result = conn.execute(self.__scripts["get_max_id"])
        max_id = result.scalar()
        conn.close()
        return max_id