from sqlalchemy import create_engine, text

db_connection_string = "postgresql://qa\:skyqa\@5.101.50.27:5432/x\_clients"
db = create_engine(db_connection_string)

# Создаем и используем соединение

def test_spisok():
    connection = db.connect()
    select_all = text("SELECT * FROM company")
    result = connection.execute(select_all)
    rows = result.mappings().all()  # Получаем строки как словари

# Работа с результатами

    print(rows[0] ["name"])
    for row in rows:
        print( row ["id"], row ["name"])

# Закрываем соединение

    connection.close()