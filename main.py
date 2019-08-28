from flask import Flask
from flask_restful import Api
from resources import ishop_api

app = Flask(__name__)
api = Api(app)

api.add_resource(ishop_api.Shop, '/')


if __name__ == "__main__":
    # product = ishop_api.P_model(name='LG', price=13010.3).save()
    # category = ishop_api.C_model(name='Tvs').save()
    # product.category = category
    # product.save()
    # result = ishop_api.Product().dump(product)
    # print(result)
    app.run(debug=True, host='192.168.56.101')
