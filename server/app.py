from flask import Flask ,  jsonify , request , make_response
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource
from flask_migrate import Migrate
from model import db ,  Restaurant , Pizza , RestaurantPizza
from sqlalchemy.exc import IntegrityError



app = Flask(__name__)

api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    restaurant_list = []

    for restaurant in restaurants:
        restaurant_data = restaurant.to_dict()
        restaurant_list.append(restaurant_data)

    return jsonify(restaurant_list)

class RestrauntByID(Resource):

    def get(self, id):

        response_dict = Restaurant.query.filter_by(id=id).first().to_dict()
        response = make_response(
            jsonify(response_dict),
            200,
        )

        return response


    def delete(self, id):

        record = Restaurant.query.filter_by(id=id).first()

        db.session.delete(record)
        db.session.commit()

        response_dict = {"message": "record successfully deleted"}

        response = make_response(
            jsonify(response_dict),
            200
        )

        return response


api.add_resource(RestrauntByID, '/restaurant/<int:id>')

@app.route('/Pizzas', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    pizzas_list = []

    for pizza in pizzas:
        pizzas_data =pizza.to_dict()
        pizzas_list.append(pizzas_data)

    return jsonify(pizzas_list)


class RestaurantPizzaResource(Resource):
    def post(self):
        data = request.get_json()

        # Validate input data
        if 'price' not in data or 'pizza_id' not in data or 'restaurant_id' not in data:
            return {"errors": ["price, pizza_id, and restaurant_id are required"]}, 400

        price = data['price']
        pizza_id = data['pizza_id']
        restaurant_id = data['restaurant_id']

        pizza = Pizza.query.get(pizza_id)
        restaurant = Restaurant.query.get(restaurant_id)

        if not pizza or not restaurant:
            return {"errors": ["Pizza or Restaurant not found"]}, 400

        try:
            restaurant_pizza = RestaurantPizza(
                price=price,
                pizza_id=pizza_id,
                restaurant_id=restaurant_id
            )
            db.session.add(restaurant_pizza)
            db.session.commit()

            # Get data related to the Pizza
            pizza_data = {
                "id": pizza.id,
                "name": pizza.name,
                "ingredients": pizza.ingredients
            }
            return pizza_data, 201
        except IntegrityError as e:
            db.session.rollback()
            return {"errors": ["Validation errors"]}, 400

# Add the RestaurantPizza resource to the API with the route '/restaurant_pizzas'
api.add_resource(RestaurantPizzaResource, '/restaurant_pizzas')

if __name__ == '__main__':
    app.run(port=5555)