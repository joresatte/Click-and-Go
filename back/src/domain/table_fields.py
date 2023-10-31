# @author: Jores Atte Mottoh
# @date: 24/10/2023
# @description: all tables attributes with tables fields 
# @project: Click and Go
# @modified by: 
# @modified date:

customer_table_fields= [ 'id', 'cliente', 'dni', 
                         'address', 'phone']

orders_packages_table_fields= ['id', 'drawers', 'bags', 
                               'substitutions', 'customer_id', 
                               'FOREIGN KEY(customer_id) REFERENCES customers(id) ON DELETE  CASCADE']

order_data_table_fields= [ 'id', 'delivery_date', 'order_number',
                            'delivery_time', 
                            'delivery_time_interval', 'customer_id', 
                            'FOREIGN KEY(customer_id) REFERENCES customers(id) ON DELETE  CASCADE' ]

delivery_note_table_fields= ['id', 'note', 
                             'customer_id',
                             'FOREIGN KEY(customer_id) REFERENCES customers(id) ON DELETE  CASCADE']

returned_product_table_fields= ['id', 'description', 'unity', 'return_reason',
                                'order_number', 'customer_id',
                                'FOREIGN KEY (order_number) REFERENCES order_datas(order_number)',
                                'FOREIGN KEY(customer_id) REFERENCES customers(id) ON DELETE  CASCADE']

receptor_data_table_fields= ['id', 'name',
                             'DNI', 'customer_id',
                             'FOREIGN KEY(customer_id) REFERENCES customers(id) ON DELETE  CASCADE']




orders_packages_table_save_fields= ['id', 'drawers', 'bags', 
                               'substitutions', 'customer_id']

order_data_table_save_fields= [ 'id', 'delivery_date', 'order_number',
                            'delivery_time', 
                            'delivery_time_interval', 'customer_id']

delivery_note_table_save_fields= ['id', 'note', 
                             'customer_id']

returned_product_table_save_fields= ['id', 'description', 'unity', 'return_reason',
                                'order_number', 'customer_id']

receptor_data_table_save_fields= ['id', 'name',
                             'DNI', 'customer_id']