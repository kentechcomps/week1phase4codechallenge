from wsgiref import validate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

# Define the association table for the many-to-many relationship
restaurant_pizza_association = db.Table('restaurant_pizza_association',
    db.Column('id', db.Integer, primary_key=True),
    db.Column('restaurant_id', db.Integer, db.ForeignKey('restaurant.id')),
    db.Column('pizza_id', db.Integer, db.ForeignKey('pizza.id')),
    db.Column('price', db.Float, nullable=False),
    db.Column('created_at', db.DateTime, default=db.func.current_timestamp(), nullable=False),
    db.Column('updated_at', db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp(), nullable=False)
)


class Pizza(db.Model):
    __tablename__ = 'Pizza'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.String(255), nullable=False)
    restaurants = db.relationship('Restaurant', secondary=restaurant_pizza_association, back_populates='pizzas')


class Restaurant(db.Model):
    __tablename__ = 'restaurant'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    pizzas = db.relationship('Pizza', secondary=restaurant_pizza_association, back_populates='restaurants')

    @validate('name')
    def validate_name(self, key, name):
        if len(name) > 50:
            raise ValueError("Name must be less than 50 characters.")
        return name
    

class RestaurantPizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'))
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.id'))
    price = db.Column(db.Float, nullable=False)

    @validate('price')
    def validate_price(self, key, price):
        if not (1 <= price <= 30):
            raise ValueError("Price must be between 1 and 30.")
        return price
