# week1phase4codechallenge

This is a flask application for building api. it has 3 models , the restaurant , pizza and a RestaurantPizza

## Table of Contents

- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Database Schema](#database-schema)
- [Features](#features)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

To get started with this project, you should have the following prerequisites installed on your system:

- Python 3.x
- Flask-SQLAlchemy
- SQLite (for database storage)
- render
- Postman

Clone the project repository to your local machine:

git clone git@github.com:kentechcomps/week1phase4codechallenge.git

`~Run pipenv install`

## Project Structure

The project structure is organized as follows:

- `models.py`: Contains the SQLAlchemy models for `Pizza`, `Restaurant`, and `RestaurantPizza`.
- `seeds.py`: Provides seed data to populate the database for testing.
-  `app.py` : This file contains the routes and queries
- `README.md`: The project's README file.

## Database Schema

The database schema consists of three tables:

- `Restaurant`: Stores information about restaurants, including their name , address and pizza
- `Pizza`: Contains details about id , name and ingredients used 
- `RestaurantPizza`: Its a join table that has pizza id , price

The relationships between these tables are defined as follows:

- `Restaurant`  has many Pizzas through RestaurantPizza
- `Pizza` also has a one-to-many relationship with restaurant with RestaurantPizza
- `RestaurantPizza` belongs to a Restaurant and belongs to a Pizz

## Features

This project demonstrates several features for performing crud operations:
-Has a GET/restaurant route - This endpoint returns Jsondata of all restaurant
-Has a GET/restaurants/:id - This end point returns data of a single restaurant
-Has a DELETE/restaurant/:id - This endpoint deletes a single record from a database
- Has a GET/pizzas - This endpoint returns list of pizzas in json format
- Has a POST/restaurant_pizza - This creates a new RestaurantPizza.If the RestaurantPizza is created successfully, send back a response with the data related to the Pizza:


## Contributors

Kennedy Mutuku
For more info contact : https://github.com/kentechcomps/week1phase4codechallenge
## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
