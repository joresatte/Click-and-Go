from src.lib.utils import temp_file
from src.webserver import create_app
from src.domain.customer_data import Customer_data, Customer_dataRepository

def test_get_customers_data():
    customer_repository = Customer_dataRepository(temp_file())
    app = create_app(repositories={"customer_data": customer_repository})
    client = app.test_client()
    
    first_cliente= Customer_data(
        id=1,
        cliente="Darn Chambers",
        dni="0268-0131",
        address="4752 Hoffman Drive",
        phone="394 937 1775"
    )
    second_cliente= Customer_data(
        id=2,
        cliente="Townsend Moakson",
        dni="49999-608",
        address="9 Victoria Junction",
        phone="436 246 3857"
    )

    customer_repository.save(first_cliente)
    customer_repository.save(second_cliente)

    response = client.get("/api/all_customers")
    if len(response.json)!= 2:
        assert False, 'fail assertion'
    assert response.json ==[
        {"id":"1",
        "cliente":"Darn Chambers",
        "dni":"0268-0131",
        "address":"4752 Hoffman Drive",
        "phone":"394 937 1775"
        },
        {"id":"2",
        "cliente":"Townsend Moakson",
        "dni":"49999-608",
        "address":"9 Victoria Junction",
        "phone":"436 246 3857"
        },
    ]

    