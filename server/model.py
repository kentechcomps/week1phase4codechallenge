from wsgiref import validate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy import MetaData

from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates 

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)


class Pizza(db.Model , SerializerMixin):
    __tablename__ = 'pizza'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.String(255), nullable=False)
  
    
    restaurant = db.relationship('RestaurantPizza', backref='pizza')
    
    serialize_rules = ('-restaurant_pizzas.pizza',)
    

class Restaurant(db.Model , SerializerMixin):
    __tablename__ = 'restaurant'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    pizza = db.relationship('RestaurantPizza', backref='restaurant')
    
    serialize_rules = ('-restaurant_pizzas.restaurant',)
    
    @validates('name')
    def validate_name(self, key, name):
        if len(name) > 50:
            raise ValueError("Name must be less than 50 characters.")
        return name
    

class RestaurantPizza(db.Model , SerializerMixin):
    __tablename__ = 'restaurantpizza'

    id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'))
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.id'))
    price = db.Column(db.Float, nullable=False)

    serialize_rules = ('-restaurant.restaurant_pizzas', '-pizza.restaurant_pizzas',)

    @validates('price')
    def validate_price(self, key, price):
        if not (1 <= price <= 30):
            raise ValueError("Price must be between 1 and 30.")
        return price
