from mongoengine import *
connect('ishop-2')


class Category(EmebeddedDocument):
    name = StringField(max_length=30, required=True)
    desc = StringField(max_lenght=100)


class Product(Document):

    name = StringField(max_length=30, required=True)
    price = FloatField(required=True)
    stock = IntField(default=1)
    availability = BooleanField(default=True)
    category = ReferenceField(EmbeddedDocumentField(Category))
    seen = IntField(default=0)


# tv = Product(name='Samsung', price=13010.3)
# tv_c = Category(name='49\" TVs', desc='TVs 2019 model year')
# tv.category = tv_c
# tv.stock = 20
# tv_c.save()
# tv.save()
