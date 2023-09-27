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

@app.route('/')
def index():
    return make_response(
        {'message': 'welcome'},
         200
    )

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
    new_record = RestaurantPizza(
        price=request.form.get('price'),
        pizza_id=request.form.get('pizza_id'),
        restaurant_id=request.form.get('restaurant_id')
    )
    try:
        db.session.add(new_record)
        db.session.commit()
        id = request.form["pizza_id"]
        pizza = Pizza.query.get(int(id))
        pizzaobject = pizza.to_dict()

        response = make_response(jsonify(pizzaobject), 200)
        return response

    except:
        return {"errors": ["validationerrors"]}, 404
    
api.add_resource(RestaurantPizzaResource, '/restaurant_pizzas')

if __name__ == '__main__':
    app.run(port=5555)