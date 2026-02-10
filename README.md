# Mechanic Shop API

A RESTful API built with Flask using the Application Factory Pattern to manage a mechanic shop's customers, mechanics, and service tickets.

## Features

- Full CRUD operations for Customers, Mechanics, and Service Tickets
- Application Factory Pattern with modular blueprints
- Marshmallow schemas for data validation and serialization
- Many-to-many relationships between Service Tickets and Mechanics
- SQLite database with SQLAlchemy ORM

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Tlappas-23/Building-API-with-Application-Factory-Pattern.git
cd Building-API-with-Application-Factory-Pattern
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

The API will be available at `http://127.0.0.1:5000`

## API Endpoints

### Customers
- `POST /customers/` - Create a customer
- `GET /customers/` - Get all customers
- `GET /customers/<id>` - Get a customer by ID
- `PUT /customers/<id>` - Update a customer
- `DELETE /customers/<id>` - Delete a customer

### Mechanics
- `POST /mechanics/` - Create a mechanic
- `GET /mechanics/` - Get all mechanics
- `PUT /mechanics/<id>` - Update a mechanic
- `DELETE /mechanics/<id>` - Delete a mechanic

### Service Tickets
- `POST /service-tickets/` - Create a service ticket
- `GET /service-tickets/` - Get all service tickets
- `PUT /service-tickets/<ticket_id>/assign-mechanic/<mechanic_id>` - Assign mechanic to ticket
- `PUT /service-tickets/<ticket_id>/remove-mechanic/<mechanic_id>` - Remove mechanic from ticket

## Testing

Import the Postman collection from `postman/MechanicShop.postman_collection.json` to test all endpoints.

## Project Structure

```
application/
├── blueprints/
│   ├── customer/
│   ├── mechanic/
│   └── service_ticket/
├── models.py
└── extensions.py
```

## Technologies

- Flask
- SQLAlchemy
- Flask-Marshmallow
- SQLite
