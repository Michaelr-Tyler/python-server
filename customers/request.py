CUSTOMERS = [
    {
      "email": "example@yahoo.com",
      "password": "asdf",
      "name": "Michael Tyler",
      "id": 1
    },{
      "email": "example@yahoo.com",
      "password": "asdf",
      "name": "Payton Downey",
      "id": 2
    },{
      "email": "example@yahoo.com",
      "password": "adsf",
      "name": "Michael Tyler",
      "id": 3
    }
]

def get_all_customers():
    return CUSTOMERS

def get_single_customer(id):
    requested_customer = None
    for customer in CUSTOMERS:
        if customer["id"] == id:
            requested_customer = customer
    return requested_customer