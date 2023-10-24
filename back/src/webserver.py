from flask import Flask, request
from flask_cors import CORS
from src.lib.utils import object_to_json
from src.domain.carrito import Carrito


def create_app(repositories):
    app = Flask(__name__)
    CORS(app)

    @app.route("/", methods=["GET"])
    def hello_world():
        return "...magic!"


    @app.route("/api/newphone", methods=["GET"])
    def newphone_get_all():
        newphones = repositories["newphone"].get_all()
        return object_to_json(newphones)

    @app.route("/api/carrito", methods=["GET"])
    def carrito_get_all():
        phones = repositories["carrito"].carrito_get_all()
        return object_to_json(phones)

    @app.route("/api/carrito/<id>", methods=["GET"])
    def carrito_get_phone_by_id(id):
        phones = repositories["carrito"].get_by_id(id)
        return object_to_json(phones)

    @app.route("/api/carrito", methods=["POST"])
    def carrito_post_all():
        body= request.json
        phones= Carrito(**body)
        repositories["carrito"].save(phones)
        return object_to_json(phones)

    @app.route("/api/carrito/<id>", methods=["DELETE"])
    def delete_carrito_phones_by_id(id):
        removed_carrito_phone = repositories["carrito"].deleted_carrito_phones_by_id(id)
        return ""


    #@app.route("/api/newphone", methods=["POST"])
    #def newphone_post():
        #body = request.json
        #newphone = Newphone(**body)
        #repositories["newphone"].save(newphone)
        #return ''
        
    
    @app.route("/api/newphone/<id>", methods=["GET"])
    def newphone_get_by_id(id):
        newphones = repositories["newphone"].get_by_id(id)
        return object_to_json(newphones)

    #@app.route("/api/newphone/<id>", methods=["DELETE"])
    #def delete_contact_by_id(id):
       # contact_removed = repositories["newphone"].remove_contact_by_id(id)
        #return ""

    return app
