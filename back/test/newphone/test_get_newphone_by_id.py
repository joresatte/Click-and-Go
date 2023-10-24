from src.lib.utils import temp_file

from src.webserver import create_app
from src.domain.newphone import NewphoneRepository, Newphone


def test_should_return_newphone_by_id():
    newphone_repository = NewphoneRepository(temp_file())
    app = create_app(repositories={"newphone": newphone_repository})
    client = app.test_client()

    mobil_1 = Newphone(
        id= "1",
        nombre= "xiaomi redmi 10",
        precio= "230 $",
        caracteristicas= "camera 64MP",
    )

    mobil_s = Newphone(
        id= "2",
        nombre= "xiaomi popofone",
        precio= "250 $",
        caracteristicas= "camera 64MP",
    )

    newphone_repository.save(mobil_1)
    newphone_repository.save(mobil_s)

    response = client.get("/api/newphone/1")
    assert response.json == {
        "id": "1",
        "nombre": "xiaomi redmi 10",
        "precio": "230 $",
        "caracteristicas": "camera 64MP",
    }
    

