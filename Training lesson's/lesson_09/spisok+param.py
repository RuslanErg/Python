from sqlalchemy import create_engine, text

db_connection_string = "postgresql://qa:skyqa@5.101.50.27:5432/x_clients"
db = create_engine(db_connection_string, echo=True)

select_by = text("SELECT * FROM company WHERE id = :id AND is_active = :is_active")
params = {"id": 1, "is_active": True}

connection = db.connect()
result = connection.execute(select_by, params)
rows = result.mappings().all()  # Получаем строки как словари
connection.close()

print(rows [0] ["name"]) if rows else print("No results")