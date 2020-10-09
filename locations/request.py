import animals


LOCATIONS = [
    {
      "id": 1,
      "name": "Nashville North",
      "address": "8422 Johnson Pike"
    },
    {
      "id": 2,
      "name": "Nashville South",
      "address": "209 Emory Drive"
    }
]

def get_all_locations():
    return LOCATIONS

# Function with a single parameter. (id) is going to be an "id" from above hard coded data
def get_single_location(id):
    requested_location = None

    # Now iterate the LOCATIONS list above.
    for location in LOCATIONS:
        # [] notaion to find key because python BRO?!?!
        if location["id"] == id:
            requested_location = location

    return requested_location

def create_location(location):
  max_id = LOCATIONS[-1]["id"]
  new_id = max_id + 1
  location["id"] = new_id
  LOCATIONS.append(location)
  return location

def delete_location(id):
    # Initial -1 value for location index, in case one isn't found
    location_index = -1

    # Iterate the LOCATIONS list, but use enumerate() so that you
    # can access the index value of each item
    for index, location in enumerate(LOCATIONS):
        if location["id"] == id:
            # Found the location. Store the current index.
            location_index = index

    # If the location was found, use pop(int) to remove it from list
    if location_index >= 0:
        LOCATIONS.pop(location_index)

def update_location(id, new_location):
  for index, location in enumerate(LOCATIONS):
    if location["id"] == id:
      LOCATIONS[index] = new_location
      break