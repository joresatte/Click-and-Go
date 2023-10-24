from src.webserver import create_app
from src.domain.newphone import NewphoneRepository
from src.domain.carrito import CarritoRepository


database_path = "data/database.db"

repositories = {
    "newphone": NewphoneRepository(database_path),
    "carrito": CarritoRepository(database_path),
}

app = create_app(repositories)

app.run(debug=True, host="0.0.0.0", port="5000")
