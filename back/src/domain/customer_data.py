# @author: Jores Atte Mottoh
# @date: 24/10/2023
# @description: Customer_data, Customer_dataRepository class
# @project: Click and Go
# @modified by: 
# @modified date:

from src.domain.utils import Utils as U
from src.domain.table_fields import customer_table_fields as fields
from src.domain.table_fields import delivery_note_table_fields as delivery_fields, delivery_note_table_save_fields as delivery_save_fields


class Customer_data:

    def __init__(self, 
                 id, cliente, dni, 
                 address, phone):
        self.id= id
        self.dni= dni
        self.cliente= cliente
        self.address= address
        self.phone= phone
        
    def to_dict(self):
        return {
            "id": self.id,
            "dni": self.dni,
            "cliente": self.cliente,
            "address": self.address,
            "phone": self.phone}
    
class Customer_dataRepository:
    def __init__(self, database_path):
        self.database_path = database_path
        self.init_tables()

    def create_conn(self):
        conn= U.create_conn(self.database_path)
        return conn
    
    def init_tables(self):
        sql = U.createTable(self, tables_variables= fields, tableName= "customers")
        sql = U.create_data_tables(self, table_variables= delivery_fields, tableName= "delivery_notes")
        conn= self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

    def get_all_customers(self):
        sql = U.fullGetDynamicQuery(self, fields=['*'], tableName='customers', listConditions=[])
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        customers = [Customer_data(**item) for item in data]
        return customers

    def get_customer(self, id):
        sql= """
                select * , 
                (select * from delivery_notes where customre_id=: id ), 
                (select * from order_datas where customre_id=:id), 
                (select * from order_packages where customre_id=:id), 
                (select * from receptor_datas where customre_id=:id),
                (select * from returned_products where customre_id=:id) 
                from customers where id=:id

             """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {'id': id})
        data = cursor.fetchone()
        customer = Customer_data(**data)
        print(customer)
        return customer

    def deleted_record_by_id(self, record):
        sql = U.fullDeleteDynamicQuery(self, tableName= "customers", listConditions=['id'])
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(
            sql, {"id": record}
        )
        conn.commit()

    def save(self, request):
        sql= U.getFullSaveDynamicQuery(self, table_variables= fields, tableName= "customers")
        conn= self.create_conn()
        cursor = conn.cursor()
        cursor.execute(
            sql,
            {"id": request.id, "dni": request.dni, "cliente": request.cliente, "address": request.address, "phone": request.phone}
            #request.to_dict()
        )
        self.save_delivery_note()
        self.save_order_data()
        self.save_order_packages()
        self.save_receptor_data()
        self.save_returned_product()
        conn.commit()

    def save_delivery_note(self, note):
        sql= U.getFullSaveDynamicQuery(self, table_variables= delivery_save_fields, tableName= "delivery_notes")
        print(sql)
        conn= self.create_conn()
        cursor = conn.cursor()
        cursor.execute(
            sql,
            # {"id": note.id, "name": note.name, "email": note.email, "subject": note.subject, "comments": note.comments}
            note.to_dict()
        )
        conn.commit()