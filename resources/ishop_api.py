from flask import request
from flask_restful import Resource
from models.products import Category as C_model
from models.products import Product as P_model
from schemas.shop_schema import Product
from schemas.shop_schema import Category

class Shop(Resource):

    def get(self):
        return Product(many=True).dump(P_model.objects()), 200

    def post(self):
        #pass
        err = Product().validate(request.json)
        if err:
            return err
        # category = request.json["category"]
        # category_object = C_model.objects(category=category)
        # if not category_object:
        #     raise ValidationError("There is incorrect category provided")
        #
        print(request.json)
        # category = request.json['category']['name']
        # print(category)
        # product = P_model(**request.json)
        # return Product().dump(product)

    def put(self):
        pass

    def delete(self):
        pass
