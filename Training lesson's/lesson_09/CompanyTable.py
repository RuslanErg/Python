from sqlalchemy import create_engine, text
import allure


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

    @allure.step("БД. Запросить список организаций")
    def get_companies(self):
        query = self.__db.execute(self.__scripts["select"])
        allure.attach(str(query.context.cursor.query), 'SQL', allure.attachment_type.TEXT)
        return query.fetchall()


    @allure.step("БД. Запросить список активных организаций")
    def get_active_companies(self):
        query = self.__db.execute(self.__scripts["select only active"])
        allure.attach(str(query.context.cursor.query), 'SQL', allure.attachment_type.TEXT)
        return query.fetchall()


    @allure.step("БД. Удалить организацию по {id}")
    def delete(self, id):
        params = {'id_to_delete': id}
        query = self.__db.execute(self.__scripts["delete by id"], parameters=params)
        allure.attach(str(query.context.cursor.query), 'SQL', allure.attachment_type.TEXT)


    @allure.step("БД. Создать организацию с названием {name}")
    def create(self, name):
        params = {'new_name': name}
        query = self.__db.execute(self.__scripts["insert new"], parameters=params)
        allure.attach(str(query.context.cursor.query), 'SQL', allure.attachment_type.TEXT)


    @allure.step("БД. Получить максимальный id организации")
    def get_max_id(self):
        query = self.__db.execute(self.__scripts["get max id"])
        allure.attach(str(query.context.cursor.query), 'SQL', allure.attachment_type.TEXT)
        return query.fetchall()[0][0]
