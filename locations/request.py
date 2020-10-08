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
