import sqlite3


class Carrito:
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


class CarritoRepository:
    def __init__(self, database_path):
        self.database_path = database_path
        self.init_tables()

    def create_conn(self):
        conn = sqlite3.connect(self.database_path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_tables(self):
        sql = """
            create table if not exists carritos(
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

    def carrito_get_all(self):
        sql = """select * from carritos"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)

        data = cursor.fetchall()
        baskets = []
        for item in data:
            basket_phones = Carrito(
                id= item["id"],
                nombre= item["nombre"],
                precio= item["precio"],
                caracteristicas= item["caracteristicas"],
            )
            baskets.append(basket_phones)


        return baskets

    def get_by_id(self, id):
        sql = """select * from carritos where id=:id"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"id": id})

        data = cursor.fetchone()
        newphone = Carrito(**data)

        return newphone

    def deleted_carrito_phones_by_id(self, phone_deleted):
        sql = """ DELETE FROM carritos
            WHERE id = :id """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(
            sql, {"id": phone_deleted}
        )
        conn.commit()

    
    def save(self, basket_phone):
        sql = """insert into carritos (id, nombre, precio, caracteristicas) values (
            :id, :nombre, :precio, :caracteristicas
        ) """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, basket_phone.to_dict())
        conn.commit()
        cursor.close()
