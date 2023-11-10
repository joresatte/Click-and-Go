from email import header
from flask import Flask, request
from flask_cors import CORS
from src.lib.utils import object_to_json
import requests
import json

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
        if one_customer is not None:
            return object_to_json(one_customer)


    @app.route("/api/remove_one_customer/<id>", methods=["DELETE"])
    def delete_one_customer(id):
        remove_one_customer = repositories['customer_data'].deleted_record_by_id(id)
        return ""
    
    def pull_data_from_external_Api():
        url= 'https://api.covid19india.org/state_district_wise.json'
        header= {"Content-Type":"appliction/json"}
        response_API = requests.get(url, header)
        print(response_API.status_code)
        data = response_API.json #response_API.text
        print(data)
        parse_json= json.loads(data)
        active_case = parse_json['id']['cliente']['dni']['address']['phone']['delivery_note']['order_data']['orders_packages']['receptor_data']['returned_product']
        print("Active cases in South Andaman:", active_case)
        return active_case
    
    # def save_data_from_external_Api():
    #     drivers= pull_data_from_external_Api()
    #     for dr in drivers:
    #         name = dr["familyName"]
    #         number = dr["permanentNumber"]
    #         sql = 'INSERT INTO Drivers (name,number) VALUES(?,?)'
    #         val = (name,number)
    #         cur.execute(sql,val)

    return app
