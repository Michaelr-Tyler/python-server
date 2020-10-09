from locations.request import create_location


CUSTOMERS = [
    {
      "email": "example@yahoo.com",
      "password": "asdf",
      "name": "Michael Tyler",
      "id": 1
    },{
      "email": "example@email.com",
      "password": "asdf",
      "name": "Payton Downey",
      "id": 2
    },{
      "email": "example@gmail.com",
      "password": "adsf",
      "name": "Hunter Spitale",
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

def create_customer(location):
  max_id = CUSTOMERS[-1]["id"]
  new_id = max_id + 1
  location["id"] = new_id
  CUSTOMERS.append(location)
  return location

def delete_customer(id):
    # Initial -1 value for customer index, in case one isn't found
    customer_index = -1

    # Iterate the CUSTOMERS list, but use enumerate() so that you
    # can access the index value of each item
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            # Found the customer. Store the current index.
            customer_index = index

    # If the customer was found, use pop(int) to remove it from list
    if customer_index >= 0:
        CUSTOMERS.pop(customer_index)

def update_customer(id, new_customer):
  for index, customer in enumerate(CUSTOMERS):
    if customer["id"] == id:
      CUSTOMERS[index] = new_customer
      break