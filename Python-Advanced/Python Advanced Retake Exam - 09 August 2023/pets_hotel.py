def accommodate_new_pets(hotel_capacity, max_weight_limit, *args):

  hotel_info = {}

  def return_result(dic):
    output = ""
    for item, value in sorted(dic.items()):
      output += f"{item}: {value}\n"
    return output
      

  for pet_type, weight in args:
    if hotel_capacity == 0:
      return f"""You did not manage to accommodate all pets!
Accommodated pets:
{return_result(hotel_info)}"""

    if weight > max_weight_limit:
      continue

    if pet_type not in hotel_info:
      hotel_info[pet_type] = 0

    hotel_info[pet_type] += 1
    hotel_capacity -= 1

  return f"""All pets are accommodated! Available capacity: {hotel_capacity}.
Accommodated pets:
{return_result(hotel_info)}"""
