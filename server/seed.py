from faker import Faker
import random

from app import app
from model import db , Pizza , Restaurant , RestaurantPizza


fake = Faker()

with app.app_context():
   
   Pizza.query.delete()
   Restaurant.query.delete()
   RestaurantPizza.query.delete()
   db.session.commit()

   pizzas = []
   for i in range(50):
      p = Pizza(
         name = fake.name() ,
         ingredients = fake.name()
      )
      pizzas.append(p)
   db.session.add_all(pizzas)
   db.session.commit()


   restaurants = []
   for i in range(50):
      p = Restaurant(
         name = fake.name() ,
         address = fake.address()
      )
      restaurants.append(p)
   db.session.add_all(restaurants)
   db.session.commit()

   restaurant_pizzas = []

   
   for i in range(100):
        
        random_pizza = random.choice(pizzas)
        random_restaurant = random.choice(restaurants)
        
        restaurant_pizza = RestaurantPizza(
            pizza_id = random_pizza.name,
            restaurant_id = random_restaurant.name,
            price = random.randint(1, 30)
        )
        restaurant_pizzas.append(restaurant_pizza)

   db.session.add_all(restaurant_pizzas)

   db.session.commit()
