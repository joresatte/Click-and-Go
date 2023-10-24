from src.lib.utils import temp_file
from src.webserver import create_app
from src.domain.carrito import CarritoRepository, Carrito


def test_should_return_carrito_phone_deleted():
    carrito_repository = CarritoRepository(temp_file())
    app = create_app(repositories={"carrito": carrito_repository})
    client = app.test_client()
    mobil_1 = Carrito(
        id= "1",
        nombre= "xiaomi redmi 10",
        precio= "230 $",
        caracteristicas= "camera 64MP",
    )

    mobil_s = Carrito(
        id= "2",
        nombre= "xiaomi popofone",
        precio= "250 $",
        caracteristicas= "camera 64MP",
    )
    carrito_repository.save(mobil_1)
    carrito_repository.save(mobil_s)

    request_delete_phone = client.delete("/api/carrito/2")
    response = client.get("/api/carrito")
    assert response.json == [{
        "id": "1",
        "nombre": "xiaomi redmi 10",
        "precio": "230 $",
        "caracteristicas": "camera 64MP",
    }
    ]
