# @author: Jores Atte Mottoh
# @date: 26/10/2023
# @description: Returned_product, Returned_productRepository class
# @project: Click and Go
# @modified by: 
# @modified date:

from src.domain.utils import Utils as U
from src.domain.table_fields import delivery_note_table_fields as fields

class Returned_product:

    def __init__(self, 
                 id, description, 
                 unity, return_reason, 
                 order_number, customer_id):
        self.id= id
        self.description= description
        self.unity= unity
        self.return_reason= return_reason
        self.order_number= order_number
        self.customer_id= customer_id
        
    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "unity": self.unity,
            "return_reason": self.return_reason,
            "order_number": self.order_number,
            "customer_id": self.customer_id}
    
class Returned_productRepository:
    def __init__(self, database_path):
        self.database_path = database_path
        self.init_tables()

    def create_conn(self):
        conn= U.create_conn(self.database_path)
        return conn
    
    def init_tables(self):
        sql = U.create_data_tables(self, table_variables= fields, tableName= "returned_products")
        conn= self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

    def get_the_receptor(self, customer_id):
        sql= U.fullGetDynamicQuery(self, fields=['*'], tableName='order_datas', listConditions=['customer_id'])
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {'customre_id': customer_id})
        data = cursor.fetchone()
        returned = Returned_product(**data)
        return returned

    def save(self, note):
        sql= U.getFullSaveDynamicQuery(self, table_variables= fields, tableName= "returned_products")
        conn= self.create_conn()
        cursor = conn.cursor()
        cursor.execute(
            sql,
            # {"id": note.id, "name": note.name, "email": note.email, "subject": note.subject, "comments": note.comments}
            note.to_dict()
        )
        conn.commit()
