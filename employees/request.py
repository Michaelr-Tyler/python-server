import employees


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
    return EMPLOYEES

def get_single_employee(id):
    requested_employee = None

    for employee in EMPLOYEES:
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee

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