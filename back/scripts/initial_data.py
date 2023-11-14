import sys
from sys import path
#path.append("../../")
sys.path.insert(0, "")
from src.domain.customer_data import Customer_dataRepository as repo_cl, Customer_data as cl
from src.domain.employee import Employee_Repository as repo, Employee as u
database_path = "data/database.db"

cliente_1= cl(
    id='1',
    cliente="Darn Chambers",
    dni="0268-0131",
    address="4752 Hoffman Drive",
    phone="394 937 1775",
    delivery_note= {
        'id':'12',
        'note':"Construction Expeditor",
        'customer_id':'1'},
    order_data= {
        'id':'2',
        'delivery_date':"3/7/2023",
        'delivery_time':"12:00",
        'order_number':'85',
        'delivery_time_interval':"12:00 - 12:30 ",
        'customer_id': '1'
    },
    orders_packages= {
        'id':'3',
        'drawers':{"cold":'2', "frozen":'3', "dry":'5', "out of drawers": '0'},
        'bags':{"cold":'2', "frozen":'1'},
        'substitutions': "No",
        'customer_id':'1' 
    },
    receptor_data= {
        'id':'6',
        'name':"Wallas Mulhall",
        'DNI':"0899397964",
        'customer_id':'1'
    },
    returned_product= {
        'id':'2',
        'description':"Project Manager",
        'unity':'2',
        'return_reason':"",
        'order_number':"",
        'customer_id':'1'
    }
)

cliente_5= cl(
    id='5',
    cliente="Darn Chambers",
    dni="0268-0535",
    address="4752 Hoffman Drive",
    phone="394 937 5775",
    delivery_note= {
        'id':'52',
        'note':"Construction Expeditor",
        'customer_id':'5'},
    order_data= {
        'id':'2',
        'delivery_date':"3/7/2023",
        'delivery_time':"52:00",
        'order_number':'85',
        'delivery_time_interval':"52:00 - 52:30 ",
        'customer_id': '5'
    },
    orders_packages= {
        'id':'3',
        'drawers':{"cold":'2', "frozen":'3', "dry":'5', "out of drawers": '0'},
        'bags':{"cold":'2', "frozen":'5'},
        'substitutions': "No",
        'customer_id':'5' 
    },
    receptor_data= {
        'id':'6',
        'name':"Wallas Mulhall",
        'DNI':"0899397964",
        'customer_id':'5'
    },
    returned_product= {
        'id':'2',
        'description':"Project Manager",
        'unity':'2',
        'return_reason':"",
        'order_number':"",
        'customer_id':'5'
    }
)

cliente_2= cl(
    id='2',
    cliente="Darn Chambers",
    dni="0268-0232",
    address="4752 Hoffman Drive",
    phone="394 937 2775",
    delivery_note= {
        'id':'22',
        'note':"Construction Expeditor",
        'customer_id':'2'},
    order_data= {
        'id':'2',
        'delivery_date':"3/7/2023",
        'delivery_time':"22:00",
        'order_number':'85',
        'delivery_time_interval':"22:00 - 22:30 ",
        'customer_id': '2'
    },
    orders_packages= {
        'id':'3',
        'drawers':{"cold":'2', "frozen":'3', "dry":'5', "out of drawers": '0'},
        'bags':{"cold":'2', "frozen":'2'},
        'substitutions': "No",
        'customer_id':'2' 
    },
    receptor_data= {
        'id':'6',
        'name':"Wallas Mulhall",
        'DNI':"0899397964",
        'customer_id':'2'
    },
    returned_product= {
        'id':'2',
        'description':"Project Manager",
        'unity':'2',
        'return_reason':"",
        'order_number':"",
        'customer_id':'2'
    }
)

cliente_3= cl(
    id='3',
    cliente="Darn Chambers",
    dni="0268-0333",
    address="4752 Hoffman Drive",
    phone="394 937 3775",
    delivery_note= {
        'id':'32',
        'note':"Construction Expeditor",
        'customer_id':'3'},
    order_data= {
        'id':'2',
        'delivery_date':"3/7/2023",
        'delivery_time':"32:00",
        'order_number':'85',
        'delivery_time_interval':"32:00 - 32:30 ",
        'customer_id': '3'
    },
    orders_packages= {
        'id':'3',
        'drawers':{"cold":'2', "frozen":'3', "dry":'5', "out of drawers": '0'},
        'bags':{"cold":'2', "frozen":'3'},
        'substitutions': "No",
        'customer_id':'3' 
    },
    receptor_data= {
        'id':'6',
        'name':"Wallas Mulhall",
        'DNI':"0899397964",
        'customer_id':'3'
    },
    returned_product= {
        'id':'2',
        'description':"Project Manager",
        'unity':'2',
        'return_reason':"",
        'order_number':"",
        'customer_id':'3'
    }
)

cliente_4= cl(
    id='4',
    cliente="Darn Chambers",
    dni="0268-0434",
    address="4752 Hoffman Drive",
    phone="394 937 4775",
    delivery_note= {
        'id':'42',
        'note':"Construction Expeditor",
        'customer_id':'4'},
    order_data= {
        'id':'2',
        'delivery_date':"3/7/2023",
        'delivery_time':"42:00",
        'order_number':'85',
        'delivery_time_interval':"42:00 - 42:30 ",
        'customer_id': '4'
    },
    orders_packages= {
        'id':'3',
        'drawers':{"cold":'2', "frozen":'3', "dry":'5', "out of drawers": '0'},
        'bags':{"cold":'2', "frozen":'4'},
        'substitutions': "No",
        'customer_id':'4' 
    },
    receptor_data= {
        'id':'6',
        'name':"Wallas Mulhall",
        'DNI':"0899397964",
        'customer_id':'4'
    },
    returned_product= {
        'id':'2',
        'description':"Project Manager",
        'unity':'2',
        'return_reason':"",
        'order_number':"",
        'customer_id':'4'
    }
)

cliente_6= cl(
    id='6',
    cliente="Darn Chambers",
    dni="0268-0636",
    address="4752 Hoffman Drive",
    phone="394 937 6775",
    delivery_note= {
        'id':'62',
        'note':"Construction Expeditor",
        'customer_id':'6'},
    order_data= {
        'id':'2',
        'delivery_date':"3/7/2023",
        'delivery_time':"62:00",
        'order_number':'85',
        'delivery_time_interval':"62:00 - 62:30 ",
        'customer_id': '6'
    },
    orders_packages= {
        'id':'3',
        'drawers':{"cold":'2', "frozen":'3', "dry":'5', "out of drawers": '0'},
        'bags':{"cold":'2', "frozen":'6'},
        'substitutions': "No",
        'customer_id':'6' 
    },
    receptor_data= {
        'id':'6',
        'name':"Wallas Mulhall",
        'DNI':"0899397964",
        'customer_id':'6'
    },
    returned_product= {
        'id':'2',
        'description':"Project Manager",
        'unity':'2',
        'return_reason':"",
        'order_number':"",
        'customer_id':'6'
    }
)

cliente_7= cl(
    id='7',
    cliente="Darn Chambers",
    dni="0268-0737",
    address="4752 Hoffman Drive",
    phone="394 937 7775",
    delivery_note= {
        'id':'72',
        'note':"Construction Expeditor",
        'customer_id':'7'},
    order_data= {
        'id':'2',
        'delivery_date':"3/7/2023",
        'delivery_time':"72:00",
        'order_number':'85',
        'delivery_time_interval':"72:00 - 72:30 ",
        'customer_id': '7'
    },
    orders_packages= {
        'id':'3',
        'drawers':{"cold":'2', "frozen":'3', "dry":'5', "out of drawers": '0'},
        'bags':{"cold":'2', "frozen":'7'},
        'substitutions': "No",
        'customer_id':'7' 
    },
    receptor_data= {
        'id':'6',
        'name':"Wallas Mulhall",
        'DNI':"0899397964",
        'customer_id':'7'
    },
    returned_product= {
        'id':'2',
        'description':"Project Manager",
        'unity':'2',
        'return_reason':"",
        'order_number':"",
        'customer_id':'7'
    }
)

def save_cliente_initial_data(clientes):
    path_repo= repo_cl(database_path)
    for cliente in clientes:
        path_repo.save_customer(cliente)
    return 'Saved successfully'
def save_employee_initial_data(employees):
    path_repo= repo(database_path)
    for employee in employees:
        path_repo.save(employee)
    return 'Saved successfully'

employee_1= u(
    id= 'test_id_1',
    identification='test_identification_1',
    password='test_password_1'
)
employee_2= u(
    id= 'test_id_2',
    identification='test_identification_2',
    password='test_password_2'
)

if __name__ == '__main__':
    cliente_list= [cliente_1, cliente_2, cliente_3, cliente_4, cliente_5, cliente_6, cliente_7]
    employee_list= [employee_1, employee_2]
    save_cliente_initial_data(cliente_list)
    save_employee_initial_data(employee_list)