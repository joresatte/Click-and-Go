# @author: Jores Atte Mottoh
# @date: 24/10/2023
# @description: Order_data, Order_dataRepository class
# @project: Click and Go
# @modified by: 
# @modified date:

from src.domain.utils import Utils as U
from src.domain.table_fields import order_data_table_fields as fields

class Order_data:

    def __init__(self, 
                 id,
                 delivery_date, order_number,
                 delivery_time, delivery_time_interval, customer_id ):
        self.id= id
        self.delivery_date= delivery_date
        self.order_number= order_number
        self.delivery_time= delivery_time
        self.delivery_time_interval= delivery_time_interval
        self.customer_id= customer_id
        
    def to_dict(self):
        return {
            "id": self.id,
            "delivery_date": self.delivery_date,
            "delivery_time": self.delivery_time,
            "order_number": self.order_number,
            "delivery_time_interval": self.delivery_time_interval,
            "customer_id": self.customer_id}
    
class Order_dataRepository:
    def __init__(self, database_path):
        self.database_path = database_path
        self.init_tables()

    def create_conn(self):
        conn= U.create_conn(self.database_path)
        return conn
    
    def init_tables(self):
        # sql= """
        #         create table if not exists order_datas(
        #                     'id', 'delivery_date', 'order_number',
        #                     'delivery_time', 
        #                     'delivery_time_interval', 'customer_id', 
        #                     'FOREIGN KEY (customer_id) REFERENCES customers(id) ON DELETE  CASCADE'
        #         )
        #      """
        sql = U.create_data_tables(self, table_variables= fields, tableName= "order_datas")
        conn= self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

    def get_an_order(self, customer_id):
        sql= U.fullGetDynamicQuery(self, fields=['*'], tableName='order_datas', listConditions=['customer_id'])
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {'customre_id': customer_id})
        data = cursor.fetchone()
        order = Order_data(**data)
        return order

    def save(self, request):
        sql= U.getFullSaveDynamicQuery(self, table_variables= fields, tableName= "order_datas")
        conn= self.create_conn()
        cursor = conn.cursor()
        cursor.execute(
            sql,
            # {"id": request.id, "name": request.name, "email": request.email, "subject": request.subject, "comments": request.comments}
            request.to_dict()
        )
        conn.commit()
