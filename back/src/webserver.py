from flask import Flask, request
from flask_cors import CORS
from src.lib.utils import object_to_json


def create_app(repositories):
    app = Flask(__name__)
    CORS(app)

    # @app.route("/api/carrito", methods=["POST"])
    # def carrito_post_all():
    #     body= request.json
    #     phones= Carrito(**body)
    #     repositories["carrito"].save(phones)
    #     return object_to_json(phones)

    @app.route("/api/all_customers", methods=["GET"])
    def get_customers():
        customers = repositories['customer_data'].get_all_customers()
        return object_to_json(customers)

    @app.route("/api/one_customer/<id>", methods=["GET"])
    def get_one_customer(id):
        one_customer = repositories['customer_data'].get_customer(id)
        print(one_customer)
        return object_to_json(one_customer)

    @app.route("/api/remove_one_customer/<id>", methods=["DELETE"])
    def delete_one_customer(id):
        remove_one_customer = repositories['customer_data'].deleted_record_by_id(id)
        return ""
    

    return app
