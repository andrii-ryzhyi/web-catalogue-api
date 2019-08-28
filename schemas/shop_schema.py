from marshmallow import Schema, fields, validates
import numbers


class Category(Schema):
    id = fields.String()
    name = fields.String(required=True)
    desc = fields.String()


class Product(Schema):
    id = fields.String()
    name = fields.String(max_length=30, required=True)
    price = fields.Float(required=True)
    availability = fields.Bool(default=True)
    category = fields.Nested(Category)


@validates('name')
def validate_name(self, value):
    if not value:
        raise ValidationError('Product\'s name is missing')

@validates('price')
def validate_price(self, value):
    if not value or not isinstance(value, numbers.Real):
        raise ValidationError('Price validation failed')
