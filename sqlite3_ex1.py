import sqlite3

class Database:
    def __init__(self, path):
        self.con = sqlite3.connect(path)

    def create_table(self):
        query = "DROP TABLE Customers;"
        self.con.execute(query)
        query = ("CREATE TABLE IF NOT EXISTS Customers(id INTEGER PRIMATY KEY, name TEXT NOT NULL, "
                 "surname TEXT NOT NULL, date_joined DATE NOT NULL);")
        self.con.execute(query)

    def add_to_customers(self, id, name, surname, date_joined):
        query = "INSERT INTO Customers(id, name, surname, date_joined) VALUES(?, ?, ?, ?)"
        self.con.execute(query, (id, name, surname, date_joined))

    def preview_table(self, table_name):
        query = f"SELECT * FROM {table_name}"
        result = self.con.execute(query).fetchall()
        print(result)

    def delete_customer_by_id(self, id):
        query = f"DELETE FROM Customers WHERE id = {id}"
        self.con.execute(query)

    def update_by_id(self, id, name, surname):
        query = f"UPDATE Customers SET name = '{name}',  surname = '{surname}' WHERE id = {id}"
        print(query)
        self.con.execute(query)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if isinstance(exc_val, Exception):
            self.con.rollback()
        else:
            self.con.commit()
        self.con.close()

with Database("file1.db") as my_db:
    my_db.create_table()
    my_db.add_to_customers(1, 'James', 'Bond', '2023-01-20')
    my_db.add_to_customers(2, 'John', 'Wick', '2021-01-20')
    my_db.add_to_customers(3, 'Indiana', 'Jones', '1982-07-11')
    my_db.preview_table("Customers")
    my_db.delete_customer_by_id(1)
    my_db.update_by_id(3, 'Han', 'Solo')
    my_db.preview_table("Customers")