import sqlite3
import json
import sqlite3
from models import Employee


EMPLOYEES = [
    {
      "name": "Sam",
      "locationId": 2,
      "animalId": 1,
      "id": 1
    },{
      "name": "Pam",
      "locationId": 2,
      "animalId": 2,
      "id": 2
    },{
      "name": "Tam",
      "locationId": 2,
      "animalId": 3,
      "id": 3
    }
]

def get_all_employees():
    with sqlite3.connect("./kennel.db") as conn:
      conn.row_factory = sqlite3.Row
      db_cursor = conn.cursor()

      db_cursor.execute("""
      SELECT
          e.id,
          e.name,
          e.address,
          e.location_id
      FROM employee e
      """)

      employees = []

      dataset = db_cursor.fetchall()

      for row in dataset:
          employee = Employee(row['id'], row['name'], row['address'], row['location_id'])
          employees.append(employee.__dict__)
    return json.dumps(employees)

def get_single_employee(id):
    with sqlite3.connect("./kennel.db") as conn:
      conn.row_factory = sqlite3.Row
      db_cursor = conn.cursor()

      db_cursor.execute("""
      SELECT
        e.id,
        e.name,
        e.address,
        e.location_id
      FROM employee e
      WHERE e.id = ?
      """, ( id, ))

      data = db_cursor.fetchone()

      employee = Employee(data['id'], data['name'], data['address'], data['location_id'])
      return json.dumps(employee.__dict__)
      
def get_employee_by_location(location_id):
    with sqlite3.connect("./kennel.db") as conn:
      conn.row_factory = sqlite3.Row
      db_cursor = conn.cursor()

      db_cursor.execute("""
      SELECT
        e.id,
        e.name,
        e.address,
        e.location_id
      FROM employee e
      WHERE e.location_id = ?
      """, ( location_id, ))

      employees = []
      dataset = db_cursor.fetchall()

      for row in dataset:
        employee = Employee(row['id'], row['name'], row['address'], row['location_id'])
        employees.append(employee.__dict__)
      
    return json.dumps(employees)

def create_employee(employee):
  max_id = EMPLOYEES[-1]["id"]
  new_id = max_id + 1
  employee["id"] = new_id
  EMPLOYEES.append(employee)
  return employee

def delete_employee(id):
  # Initial -1 value for employees index, in case one isn't found
  employees_index = -1

  # Iterate the EMPLOYEES list, but use enumerate() so that you
  # can access the index value of each item
  for index, employees in enumerate(EMPLOYEES):
      if employees["id"] == id:
          # Found the employees. Store the current index.
          employees_index = index

  # If the employees was found, use pop(int) to remove it from list
  if employees_index >= 0:
      EMPLOYEES.pop(employees_index)

def update_employee(id, new_employee):
  for index, employee in enumerate(EMPLOYEES):
    if employee["id"] == id:
      EMPLOYEES[index] = new_employee
      break