import sqlite3


class Newphone:
    def __init__(self, id, nombre, precio, caracteristicas):
        self.id= id
        self.nombre = nombre
        self.precio = precio
        self.caracteristicas = caracteristicas


    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "precio": self.precio,
            "caracteristicas": self.caracteristicas,
            }


class NewphoneRepository:
    def __init__(self, database_path):
        self.database_path = database_path
        self.init_tables()

    def create_conn(self):
        conn = sqlite3.connect(self.database_path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_tables(self):
        sql = """
            create table if not exists newphones(
                id varchar,
                nombre varchar,
                precio varchar,
                caracteristicas varchar
            )
        """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

    def get_all(self):
        sql = """select * from newphones"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)

        data = cursor.fetchall()
        phones = []
        for item in data:
            each_phone = Newphone(
                id= item["id"],
                nombre= item["nombre"],
                precio= item["precio"],
                caracteristicas= item["caracteristicas"],
            )
            phones.append(each_phone)


        return phones

    def get_by_id(self, id):
        sql = """select * from newphones where id=:id"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"id": id})

        data = cursor.fetchone()
        newphone = Newphone(**data)

        return newphone
    
    def save(self, contact):
        sql = """insert into newphones (id, nombre, precio, caracteristicas) values (
            :id, :nombre, :precio, :caracteristicas
        ) """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, contact.to_dict())
        conn.commit()
        cursor.close()
