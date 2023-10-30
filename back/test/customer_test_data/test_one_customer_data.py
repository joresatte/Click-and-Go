from src.lib.utils import temp_file
from src.webserver import create_app
from src.domain.customer_data import Customer_data, Customer_dataRepository
from src.domain.order_data import Order_dataRepository, Order_data
from src.domain.order_packages import Order_packagesRepository, Order_packages
from src.domain.delivery_note import Delivery_noteRepository, Delivery_note
from src.domain.returned_product import Returned_productRepository, Returned_product
from src.domain.receptor_data import Receptor_dataRepository, Receptor_data  

def test_get_one_customer_data():
    customer_data_repository = Customer_dataRepository(temp_file())
    order_data_repository = Order_dataRepository(temp_file())
    order_packages_repository = Order_packagesRepository(temp_file())
    delivery_note_repository = Delivery_noteRepository(temp_file())
    return_product_repository = Returned_productRepository(temp_file())
    receptor_data_repository = Receptor_dataRepository(temp_file())
    app = create_app(repositories={"customer_data": customer_data_repository})
    app = create_app(repositories={"order_data": order_data_repository})
    app = create_app(repositories={"order_packages": order_packages_repository})
    app = create_app(repositories={"Delivery_note": delivery_note_repository})
    app = create_app(repositories={"returned_product": return_product_repository})
    app = create_app(repositories={"receptor_data": receptor_data_repository})
    client = app.test_client()

    first_cliente= Customer_data(
        id=1,
        cliente="Darn Chambers",
        dni="0268-0131",
        address="4752 Hoffman Drive",
        phone="394 937 1775"
    )
    customer_data_repository.save(first_cliente)

    first_cliente_note= Delivery_note(
        id=12,
        note="Construction Expeditor",
        customer_id=1
    )
    delivery_note_repository.save(first_cliente_note)

    first_cliente_order= Order_data(
        id=2,
        delivery_date="3/7/2023",
        delivery_timed="12:00",
        order_number=85,
        delivery_time_interval="12:00 - 12:30 ",
        customer_id= 1
    )
    order_data_repository.save(first_cliente_order)

    first_cliente_order_packages= Order_packages(
        id=3,
        drawers={"cold":2, "frozen":3, "dry":5, "out of drawers": 0},
        bags={"cold":2, "frozen":1},
        substitutions= "No",
        customer_id=1 
    )
    order_packages_repository.save(first_cliente_order_packages)

    first_cliente_receptor= Receptor_data(
        id=6,
        name="Wallas Mulhall",
        DNI="0899397964",
        customer_id=1
    )
    receptor_data_repository.save(first_cliente_receptor)

    first_cliente_returns= Returned_product(
        id=2,
        description="Project Manager",
        unity=2,
        return_reason="",
        order_number="",
        customer_id=1
    )
    return_product_repository.save(first_cliente_returns)

    response= client.get("/api/one_customer/1")
    if len(response== 1):
        assert True, 'Correct assertion'
    else:
        assert False, 'Assertion failed'
    assert response!=[]